from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException

# Middleware to reject requests without User-Agent
class UserAgentMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if "user-agent" not in request.headers:
            raise HTTPException(400, "User-Agent header required")
        return await call_next(request)
