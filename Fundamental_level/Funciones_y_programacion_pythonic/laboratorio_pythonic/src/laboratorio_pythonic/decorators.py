import time
from functools import wraps

def retry(max_retries=3, delay=1, backoff=2, exceptions=(Exception,), verbose=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay

            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if verbose:
                        print(f"Error: {e} | Intento {attempts}")

                    if attempts == max_retries:
                        raise
                    
                    time.sleep(current_delay)
                    current_delay *= backoff

        return wrapper
    return decorator