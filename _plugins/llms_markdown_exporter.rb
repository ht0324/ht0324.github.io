# frozen_string_literal: true

require "fileutils"

module Jekyll
  module LlmsSupport
    # Writes a clean markdown companion file for each published post.
    class MarkdownExporter
      def initialize(site)
        @site = site
      end

      def export!
        @site.posts.docs.each do |post|
          next if skip?(post)

          content = build_content(post)
          next if content.nil?

          destination = destination_for(post)
          FileUtils.mkdir_p(File.dirname(destination))
          File.write(destination, content, mode: "w", encoding: Encoding::UTF_8)
        end
      end

      private

      def skip?(post)
        post.data["draft"] || post.data["exclude_from_llms_md"]
      end

      def build_content(post)
        body = post.content.to_s.lstrip
        return nil if body.empty?

        fragments = []

        title = post.data["title"].to_s
        fragments << "# #{title}" unless title.empty?

        published_at = post.data["date"]
        if published_at.respond_to?(:strftime)
          fragments << "_Published: #{published_at.strftime('%Y-%m-%d')}_"
        end

        tags = Array(post.data["tags"]).map(&:to_s).reject(&:empty?)
        fragments << "_Tags: #{tags.join(', ')}_" unless tags.empty?

        categories = Array(post.data["categories"]).map(&:to_s).reject(&:empty?)
        fragments << "_Categories: #{categories.join(', ')}_" unless categories.empty?

        source_url = source_url_for(post)
        fragments << "_Original: #{source_url}_" if source_url

        fragments << ""
        fragments << body

        fragments.join("\n").gsub(/\r\n?/, "\n").strip + "\n"
      end

      def destination_for(post)
        relative = normalized_url(post)
        relative = relative.empty? ? "" : relative
        path = File.join(relative, "index.html.md")
        @site.in_dest_dir(path)
      end

      def normalized_url(post)
        post.url.to_s.gsub(%r{^/}, "")
      end

      def source_url_for(post)
        site_url = @site.config["url"].to_s
        baseurl = @site.config["baseurl"].to_s
        path = post.url.to_s
        return nil if site_url.empty? && baseurl.empty?

        "#{site_url}#{baseurl}#{path}"
      end
    end
  end

  Hooks.register :site, :post_write do |site|
    LlmsSupport::MarkdownExporter.new(site).export!
  end
end
