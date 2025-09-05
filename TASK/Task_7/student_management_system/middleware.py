import time
from pathlib import Path
from starlette.middleware.base import BaseHTTPMiddleware

LOG_FILE = Path("requests.log")

class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = int((time.time() - start) * 1000)

        line = f"{request.client.host} {request.method} {request.url.path} {response.status_code} {duration}ms\n"
        with LOG_FILE.open("a") as f:   
            f.write(line)

        return response
