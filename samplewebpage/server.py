"""
PyFlow Studio — Local Development Server
Run this script to test the web application locally before hosting on Netlify.

Usage:
    py server.py
"""

import http.server
import socketserver
import os
import sys

DEFAULT_PORT = 8080

class PyFlowHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS and modern headers for WebAssembly
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

def run(port=DEFAULT_PORT):
    # Ensure current working directory is the folder of server.py
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Try finding an open port if 8080 is in use
    for p in range(port, port + 20):
        try:
            with socketserver.TCPServer(("", p), PyFlowHandler) as httpd:
                print("\n" + "=" * 60)
                print("[*] PyFlow Studio - Local Development Server")
                print("=" * 60)
                print(f"[>] Local URL: http://localhost:{p}")
                print(f"[*] Serving:   {os.getcwd()}")
                print("=" * 60)
                print("Press Ctrl+C to stop the server at any time.\n")
                httpd.serve_forever()
                break
        except OSError as e:
            if "Address already in use" in str(e) or getattr(e, 'winerror', 0) == 10048:
                continue
            else:
                raise e

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\n[Server stopped gracefully]")
        sys.exit(0)
