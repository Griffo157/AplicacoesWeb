from my_webserver import MyWebServer
from http.server import SimpleHTTPRequestHandler
import os

PORT = int(os.getenv("PORT", 3001)) # Porta Padrão

class ManuseioHttpRequest(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-Type", "text/html;charset=utf-8")
            self.end_headers()
            self.wfile.write("<p>Ola Mundo!</p>".encode())

app = MyWebServer(ManuseioHttpRequest)

if __name__ == "__main__":
    app.run()