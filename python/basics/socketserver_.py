"""
DOC: https://docs.python.org/3/library/socketserver.html
A framework for network servers
"""

import http.server
import socketserver

with socketserver.TCPServer(('127.0.0.1', 8000), http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()