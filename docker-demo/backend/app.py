
import os
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

APP_ENV = os.environ.get("APP_ENV", "development")
DATA_DIR = "/app/data"
FILE_PATH = os.path.join(DATA_DIR, "starts.txt")

os.makedirs(DATA_DIR, exist_ok=True)

if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r") as file:
        count = int(file.read())
else:
    count = 0

count += 1

with open(FILE_PATH, "w") as file:
    file.write(str(count))


class BackendHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = {
                "status": "healthy",
                "service": "nxttrendz-backend",
                "environment": APP_ENV,
                "starts": count
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()


server = HTTPServer(("0.0.0.0", 8000), BackendHandler)

print("NxtTrendz backend running on port 8000", flush=True)

server.serve_forever()
