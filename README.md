# URL Shortener

This is a simple URL shortener for my personal use. It consists of HTML files in `/docs` that redirect to other URLs. The shortened URLs are hosted on GitHub Pages.

## How to Build Your Own

You'll need two files:

- `links.json`: Stores pairs of shortened and long URLs (e.g., `short.com/1` and `longdomain.com/page-one`). Only the path component of the shortened URL is needed.
- `main.py`: Generates an HTML file for each entry in the JSON file. If you're using a custom domain, ensure to customize it accordingly. Otherwise, you can omit that part.

After running `main.py`, publish your GitHub Pages from the `docs` directory.
