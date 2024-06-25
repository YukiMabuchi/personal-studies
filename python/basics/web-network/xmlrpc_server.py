"""
DOC: https://docs.python.org/3/library/xmlrpc.html
     https://docs.python.org/3/library/xmlrpc.server.html#module-xmlrpc.server
     https://docs.python.org/3/library/xmlrpc.client.html#module-xmlrpc.client

現在はRESTの方が好まれる
社内インフラなど簡易的なものにはよい
"""
from xmlrpc.server import SimpleXMLRPCServer

with SimpleXMLRPCServer(('127.0.0.1', 8000)) as server:
    def add_num(x, y):
        return x + y
    
    server.register_function(add_num, 'add_num')
    server.serve_forever()
    