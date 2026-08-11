import http.server
import socketserver

PORT = 8000

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"http://localhost:{PORT}")
    httpd.serve_forever()
    
    
#docker run -p 8000:8000 test-app:latest