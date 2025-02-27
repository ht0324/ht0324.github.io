#!/usr/bin/env python3
import re
import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime
from groq import Groq

def generate_markdown():
    # Get the blog writing from the text widget
    blog_content = text_widget.get("1.0", tk.END).strip()
    if not blog_content:
        messagebox.showerror("Error", "Please enter your blog writing content.")
        return

    # Construct the prompt for the LLM with an example YAML header included.
    prompt = f"""Please generate a YAML header (front matter) for the following blog writing. The YAML header must be enclosed by triple hyphens (---) at the beginning and end, and must contain the following keys:

- **layout:** Must be exactly "post".
- **title:** Generate a short, concise title based solely on the blog writing content. The title should be in Title Case.
- **date:** Use a placeholder for the date and time in the format "YYYY-MM-DD HH:MM:SS". Use placeholders "{{DATE}}" for the date and "{{TIME}}" for the time.
- **description:** Write a short, concise sentence summarizing the content.
- **tags:** Choose one or more tags from: AI, Sci-Fi, life. (Separate multiple tags with spaces.)
- **categories:** Choose one or more categories from: blog, thoughts, link, papers. (Separate multiple categories with spaces.)

Below is an example for guidance:
---
layout: post
title: AI Girlfriend
date: 2023-03-15 14:40:16
description: A concise description of the writing’s content.
tags: AI Sci-Fi
categories: blog thoughts
---
--- Do not include any text besides the YAML header.

Blog writing content:
{blog_content}
"""

    # Call the LLM API using the provided Groq client.
    client = Groq()
    yaml_header = ""
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt},
            ],
            temperature=0,
            max_completion_tokens=2048,
            top_p=1,
            stream=True,
            stop=None,
        )

        # Stream and collect the YAML header output.
        for chunk in completion:
            yaml_header += (chunk.choices[0].delta.content or "")
    except Exception as e:
        messagebox.showerror("API Error", f"An error occurred while contacting the LLM API:\n{e}")
        return

    # Replace the date/time placeholders with the current date and time.
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    yaml_header = yaml_header.replace("{DATE}", current_date)
    yaml_header = yaml_header.replace("{TIME}", current_time)

    # Extract the generated title from the YAML header.
    title_match = re.search(r'^title:\s*(.+)$', yaml_header, re.MULTILINE)
    if title_match:
        generated_title = title_match.group(1).strip()
    else:
        generated_title = "Error-Untitled"

    # Create the filename using the pattern YYYY-MM-DD-abbreviated-title.md.
    abbreviated_title = re.sub(r'[^a-z0-9]+', '-', generated_title.lower()).strip('-')
    filename = f"{current_date}-{abbreviated_title}.md"

    # Combine the YAML header and the formatted blog content.
    final_markdown = f"{yaml_header}\n\n{formatted_content}"

    # Write the final markdown to a file.
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(final_markdown)
        messagebox.showinfo("Success", f"Markdown file created: {filename}")
    except Exception as e:
        messagebox.showerror("File Error", f"Could not write file:\n{e}")

# --- Tkinter GUI Setup ---
root = tk.Tk()
root.title("Blog Markdown Generator")

# Label instructing the user
label = tk.Label(root, text="Enter your blog writing content:")
label.pack(pady=5)

# Scrolled text widget for blog writing input
text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
text_widget.pack(padx=10, pady=5)

# Submit button to trigger the markdown generation
submit_button = tk.Button(root, text="Generate Markdown", command=generate_markdown)
submit_button.pack(pady=10)

root.mainloop()