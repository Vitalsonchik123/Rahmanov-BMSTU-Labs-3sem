import time

class cm_timer_1: #через класс
    def __enter__(self):
        self.startTime = time.time()
        return self  # можно ничего не возвращать

    def __exit__(self, excType, excValue, traceback):
        self.endTime = time.time()
        elapsed = self.endTime - self.startTime
        print(f"time: {elapsed:.3f}")



from contextlib import contextmanager

@contextmanager
def cm_timer_2():# через библиотеку
    startTime = time.time()
    try:
        yield
    finally:
        endTime = time.time()
        elapsed = endTime - startTime
        print(f"time: {elapsed:.3f}")

import time

with cm_timer_1():
    time.sleep(5.5)

print("---")

with cm_timer_2():
    time.sleep(5.5)
