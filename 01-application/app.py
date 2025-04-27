"""
echo-server
"""

import http.server
import os
import socket
import socketserver

hostname = socket.gethostname()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
except Exception:
    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip_address = "Unable to determine IP"


author = os.environ.get("AUTHOR", "Default Author")

PORT = 8000


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Host Info</title>
                <meta charset="UTF-8">
            </head>
            <body>
                <h1>echo-server</h1>
                <p><strong>Hostname:</strong> {hostname}</p>
                <p><strong>IP address:</strong> {ip_address}</p>
                <p><strong>Author:</strong> {author}</p>
            </body>
            </html>
            """
            self.wfile.write(bytes(html_content, "utf8"))
        else:
            self.send_error(404, "File Not Found: %s" % self.path)


handler_object = MyHttpRequestHandler

my_server = socketserver.TCPServer(("", PORT), handler_object)

print(f"Server starts at port {PORT}")
print(f"Information: Hostname={hostname}, IP={ip_address}, Author={author}")
print("To stop server press Ctrl+C")

try:
    my_server.serve_forever()
except KeyboardInterrupt:
    print("\nServer has stopped.")
    my_server.server_close()
