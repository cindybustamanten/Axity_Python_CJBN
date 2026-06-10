import time
from contextlib import contextmanager

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        end = time.time()
        print(f"⏱ Tiempo: {end - self.start:.4f} s")


@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"⏱ Tiempo: {end - start:.4f} s")