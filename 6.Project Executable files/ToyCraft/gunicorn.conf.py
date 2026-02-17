import multiprocessing
import os

bind = f"0.0.0.0:{os.getenv('PORT', '10000')}"

# Keep defaults conservative for Render starter instances.
workers = int(os.getenv("WEB_CONCURRENCY", "1"))
threads = int(os.getenv("GUNICORN_THREADS", "2"))
worker_class = "gthread"

timeout = int(os.getenv("GUNICORN_TIMEOUT", "60"))
graceful_timeout = 30
keepalive = 5

# Recycle workers periodically to avoid long-run memory growth.
max_requests = 1000
max_requests_jitter = 100

errorlog = "-"
accesslog = "-"
loglevel = os.getenv("LOG_LEVEL", "info")
