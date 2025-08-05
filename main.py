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

        elif self.path == '/pagina1':
            self.send_response(200)
            self.send_header("Content-Type", "text/html;charset=utf-8")
            self.end_headers()
            self.wfile.write("<p>Eu acho o cauã muito gente boa.</p>".encode())

        elif self.path == '/index':
            self.send_response(200)
            self.send_header("Content-Type", "text/html;charset=utf-8")
            self.end_headers()
            res_body = open("index.html", 'r').read().format_map({"PORT": PORT})
            self.wfile.write(res_body.encode())

        else:
            self.send_error(418)

app = MyWebServer(ManuseioHttpRequest)

if __name__ == "__main__":
    app.run()
