import http.server
import functools
import os

directory = os.path.dirname(os.path.abspath(__file__))
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=directory)
httpd = http.server.HTTPServer(("", 8788), handler)
httpd.serve_forever()
