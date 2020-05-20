from http.server import HTTPServer, CGIHTTPRequestHandler


PORT = 8000

httpd = HTTPServer(("", PORT), CGIHTTPRequestHandler)
print("server at port", PORT)

httpd.serve_forever()
