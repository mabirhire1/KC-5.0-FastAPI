from starlette.middleware.base import BaseHTTPMiddleware

# Simple middleware that counts total requests
class RequestCounterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.counter = 0

    async def dispatch(self, request, call_next):
        self.counter += 1
        print(f"👉 Total requests so far: {self.counter}")  # Beginner-friendly logging
        response = await call_next(request)
        response.headers["X-Total-Requests"] = str(self.counter)  # Send back in header
        return response
