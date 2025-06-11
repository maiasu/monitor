import http.server
import socketserver
import os

PORT = 8000

os.chdir(os.path.dirname(__file__))
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving on http://localhost:{PORT}")
    httpd.serve_forever()
