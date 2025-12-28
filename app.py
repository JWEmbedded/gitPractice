from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import os

PORT = 8000
DATA_FILE = 'portfolio.json'

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/get_data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, 'r', encoding='utf-8') as f:
                    self.wfile.write(f.read().encode())
            else:
                self.wfile.write(json.dumps([]).encode())
        else:
            return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/save_data':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            with open(DATA_FILE, 'w', encoding='utf-8') as f:
                f.write(post_data.decode('utf-8'))
            self.send_response(200)
            self.end_headers()

print(f"서버 시작: http://localhost:{PORT}")
HTTPServer(('localhost', PORT), MyHandler).serve_forever()