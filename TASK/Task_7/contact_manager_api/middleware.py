from starlette.middleware.base import BaseHTTPMiddleware
import logging

logger = logging.getLogger("uvicorn")


class LogIPMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        client_ip = request.client.host
        logger.info(f"Request from {client_ip}")
        response = await call_next(request)
        return response