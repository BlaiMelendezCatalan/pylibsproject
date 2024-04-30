"""API decorators."""
import functools
import logging
import time
from typing import Any, Callable


def benchmark(logger: logging.Logger) -> None:
    """Log the time consumed by the decorated function.

    Parameters
    ----------
    logger : logging.Logger
        Logger passed from the api main script.

    Returns
    -------
    func : Callable
        Decorator that includes the Logger.

    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.monotonic()
            result = func(*args, **kwargs)
            run_time = time.monotonic() - start_time
            logger.debug(f"Function '{func.__name__}' ran for {run_time}")
            return result

        return wrapper

    return decorator
