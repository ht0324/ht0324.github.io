# frozen_string_literal: true

# Monkey-patch jekyll-minifier so interrupted write syscalls are retried.
require 'jekyll-minifier'

module Jekyll
  module Compressor
    def output_file(dest, content)
      FileUtils.mkdir_p(File.dirname(dest))

      attempts = 0
      begin
        attempts += 1
        File.open(dest, 'w') { |f| f.write(content) }
      rescue Errno::EINTR, Errno::EAGAIN, Errno::EWOULDBLOCK, Errno::ETIMEDOUT
        sleep(0.05 * attempts)
        retry if attempts < 5
        raise
      end
    end
  end
end
