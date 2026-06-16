import http.server
import socketserver
import os
import webbrowser

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            content = """
            <html>
            <head>
                <title>Visualizador de Apresentacoes</title>
                <style>
                    body { font-family: sans-serif; text-align: center; padding: 50px; background: #f4f4f4; }
                    .card { background: white; padding: 20px; margin: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); display: inline-block; width: 300px; }
                    h1 { color: #333; }
                    a { text-decoration: none; color: #00B894; font-weight: bold; }
                    .ia { color: #64FFDA; }
                </style>
            </head>
            <body>
                <h1>Suas Apresentacoes Persuasivas</h1>
                <div class="card">
                    <h2>Produto 1</h2>
                    <p>Protocolo Barriga Zero</p>
                    <a href="/produto1/intro.html">Ver Apresentacao</a>
                </div>
                <div class="card">
                    <h2>Produto 2</h2>
                    <p>Mestre da IA</p>
                    <a href="/produto2/intro_ia.html" class="ia">Ver Apresentacao</a>
                </div>
                <p style="margin-top: 40px; color: #666;">Use as setas do navegador ou links internos para navegar entre os slides.</p>
            </body>
            </html>
            """
            self.wfile.write(content.encode())
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

def start_server():
    Handler = MyHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Servidor rodando em http://localhost:{PORT}")
        print("Pressione Ctrl+C para parar.")
        # Tenta abrir o navegador automaticamente
        webbrowser.open(f"http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor parado.")

if __name__ == "__main__":
    start_server()
