"""Mini-Webserver fuer TaskLite (Demo-Zweck, kein Produktionscode)."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

import tasks


class TaskHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/tasks":
            body = json.dumps(tasks.open_tasks()).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()


def main(port=8000):
    HTTPServer(("", port), TaskHandler).serve_forever()


if __name__ == "__main__":
    main()
