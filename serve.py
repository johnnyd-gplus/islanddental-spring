import http.server
import os

os.chdir("/Users/johndeluca/Downloads/The Claude Files/islanddental-spring")

handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(("", 8788), handler)
httpd.serve_forever()
