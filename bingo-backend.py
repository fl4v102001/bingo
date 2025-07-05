from http.server import BaseHTTPRequestHandler, HTTPServer

class AutoRefreshApp(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            try:
                with open("numeros.txt", "r") as f:
                    content = f.read()
            except FileNotFoundError:
                content = "(file not found)"

            script = '''

            <div id="dataHora"></div>
            <script>
                const agora = new Date();
                const formatada = agora.toLocaleString('pt-BR', {
                    hour: '2-digit',
                    minute: '2-digit',
                    second: '2-digit'
                });
                document.getElementById("dataHora").textContent = "Agora: " + formatada;
            </script>
            '''


            html = f'''
            <html>
            <head>
                <meta http-equiv="refresh" content="5">
            </head>
            <body>
                <pre>{content}</pre>
                {script}
            </body>
            </html>
            '''
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("Access-Control-Allow-Origin", "*")  # Permite qualquer origem
            self.end_headers()
            self.wfile.write(html.encode())
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length).decode()

        if self.path == '/input':
            with open("numeros.txt", "w") as f:
                f.write(body)
            self.send_response(204, "Processado")
            self.send_header("Access-Control-Allow-Origin", "*")  # Permite qualquer origem
            self.end_headers()
        else:
            self.send_error(404, "Not Found")

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

if __name__ == "__main__":
    # Descobre o IP local automaticamente
    print(f"Servidor rodando ... (Ctrl+C para parar)")
    HTTPServer(('0.0.0.0', 8000), AutoRefreshApp).serve_forever()
