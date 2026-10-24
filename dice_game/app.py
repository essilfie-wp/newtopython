
import sys
import json
import random
from pathlib import Path
from http.server import BaseHTTPRequestHandler, HTTPServer

BASE_DIR = Path(__file__).resolve().parent

#Game scores
scores = {"player": 0, "computer": 0, "ties": 0}

class DiceHandler(BaseHTTPRequestHandler):
    def _send(self, content: bytes, content_type: str, status: int = 200):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self):
        path = self.path.split("?")[0]
        if path in ("/","/index.html"):
            file_path = BASE_DIR / "index.html,  charset=utf-8"
            self._send(file_path.read_bytes(), "text/html")
        elif path == "/stlye.css":
            file_path = BASE_DIR / "stlye.css"
            self._send(file_path.read_bytes(), "text/css,  charset=utf-8")
        else:
            self._send(b"Page not found", "text/plain", 404) 

    def do_POST(self):
      global scores
      path = self.path.split("?")[0]
      if path == "/roll":
        p1, p2 = random.randint(1, 6), random.randint(1, 6)
        c1, c2 = random.randint(1, 6), random.randint(1, 6)
        p_tot = p1 + p2
        c_tot = c1 + c2

        if p_tot > c_tot:
            winner = "Player"
            scores["player"] += 1
            message = "You Win!"
        elif c_tot > p_tot:
            winner = "Computer"
            scores["computer"] += 1
            message = "Computer Wins!"
        else:
            winner = "Tie"
            scores["ties"] += 1
            message = "It's a Tie!"

        payload = {
            "player_dice": [p1, p2],
            "computer_dice": [c1, c2],
            "player_total": p_tot,
            "computer_total": c_tot,
            "winner": winner,
            "scores": scores,
            "message": message
        }
        
        self._send(json.dumps(payload).encode("utf-8"), "application/json")

      elif path == "/reset":
        scores["player"] = 0
        scores["computer"] = 0
        scores["ties"] = 0
        self._send(json.dumps({"scores": scores}).encode("utf-8"), "application/json")
      else:
        self._send(b"Not Found", "text/plain", 404)

def main(port: int = 5000):
    server = HTTPServer(("0.0.0.0", port), DiceHandler)
    print(f"Server running on http://localhost:{port}")
    print("Press Ctrl+C to stop the server")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    main(port)