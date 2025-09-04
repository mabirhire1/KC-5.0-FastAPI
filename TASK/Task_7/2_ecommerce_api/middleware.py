import time
from starlette.middleware.base import BaseHTTPMiddleware

# Middleware to measure request processing time
class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()
        response = await call_next(request)
        duration_ms = int((time.time() - start) * 1000)
        response.headers["X-Process-Time-ms"] = str(duration_ms)
        return response
