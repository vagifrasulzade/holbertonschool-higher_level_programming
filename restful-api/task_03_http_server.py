#!/usr/bin/python3
"""
Docstring for restful-api.task_03_http_server
"""

from asyncio import run
import http
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import socketserver

dict_sample = {"name": "John", "age": 30, "city": "New York"}
json_sample = json.dumps(dict_sample)


sub = http.server.SimpleHTTPRequestHandler

class Handler(sub):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)  
            self.send_header("Content-type", 'text/plain') 
            self.end_headers()  
            self.wfile.write(b'Hello, this is a simple API!')  
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_sample.encode())
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


PORT = 8000
server = socketserver.TCPServer(('', PORT), Handler)
server.serve_forever()

if __name__ == "__main__":
    run()
