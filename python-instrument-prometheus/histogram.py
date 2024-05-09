import http.server
import time
import random
from prometheus_client import start_http_server, Histogram


# prometheus metrics
REQUEST_RESPOND_TIME = Histogram(
    'app_response_latency_seconds',
    'The response latency by seconds',
    ['app_name', "environment", 'endpoint'],
    buckets=[0.1, 0.5, 1, 2, 3, 4, 5, 10])

APP_PORT = 8000
METRICS_PORT = 8001

class HandleRequests(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        now = time.time()
        time.sleep(random.randint(0, 3))
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to our first Prometheus-Python application.</center></h2></body></html>", "utf-8"))
        self.wfile.close()
        later = time.time()
        difference = int(later - now)   
        REQUEST_RESPOND_TIME.labels('promth-python', 'dev', self.path).observe(difference)

if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('localhost', APP_PORT), HandleRequests)
    server.serve_forever()
