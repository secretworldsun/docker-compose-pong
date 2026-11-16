import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", "8080"))
BODY = os.environ.get("RESPONSE", "Pong") + "\n"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = BODY.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        print("request from %s: %s" % (self.address_string(), fmt % args), flush=True)


if __name__ == "__main__":
    print("listening on 0.0.0.0:%d, response=%r" % (PORT, BODY.strip()), flush=True)
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
