"""
Geo Sushi Bar — local preview server.

This site is plain HTML/CSS/JS, so it doesn't need Python to run.
This tiny script just serves the folder locally so you can preview it
in a browser before uploading it to real hosting.

Usage:
    python3 server.py
Then open:
    http://localhost:8000
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"Serving Geo Sushi Bar at {url}  (Ctrl+C to stop)")
        try:
            webbrowser.open(url)
        except Exception:
            pass
        httpd.serve_forever()
