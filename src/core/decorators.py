import asyncio
from functools import wraps
from logging import getLogger
from typing import Any, Callable, Coroutine, ParamSpec, TypeVar

T = TypeVar("T")
P = ParamSpec("P")

logger = getLogger(__name__)


def retry(
    max_attempts: int, backoff: float, max_backoff: float = 30.0
) -> Callable[
    [Callable[P, Coroutine[Any, Any, T]]], Callable[P, Coroutine[Any, Any, T]]
]:
    def decorator(
        func: Callable[P, Coroutine[Any, Any, T]],
    ) -> Callable[P, Coroutine[Any, Any, T]]:
        @wraps(func)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> Any:
            for attempt in range(max_attempts):
                try:
                    result = await func(*args, **kwargs)
                    return result
                except Exception as e:
                    should_retry = getattr(e, "is_retryable", False)
                    if not should_retry or attempt == max_attempts - 1:
                        raise

                    wait_time = min(backoff * (2**attempt), max_backoff)
                    logger.warning(f"Retrying in {wait_time}s...")
                    await asyncio.sleep(wait_time)

        return wrapper

    return decorator
