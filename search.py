from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class SearchHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/search'):
            query = parse_qs(self.path[7:])['q'][0]
            # Perform search logic here based on the query
            # Return search results as HTML or JSON response
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f"Search results for: {query}".encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SearchHandler)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
