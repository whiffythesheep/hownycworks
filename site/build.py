"""Build the hownycworks.org landing page.

This site is a thin umbrella: a single index page listing projects that live
on their own domains (currently just hearinghearings.nyc). No content files,
no per-page templates.
"""

import os
import shutil

from jinja2 import Environment, FileSystemLoader

ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(ROOT, "templates")
STATIC_DIR = os.path.join(ROOT, "static")
OUTPUT_DIR = os.path.join(ROOT, "output")


def build():
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    if os.path.exists(STATIC_DIR):
        shutil.copytree(STATIC_DIR, os.path.join(OUTPUT_DIR, "static"))

    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), autoescape=True)
    index_html = env.get_template("index.html").render()
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print(f"Built: index.html")
    print(f"\nSite built to {OUTPUT_DIR}")


if __name__ == "__main__":
    build()
