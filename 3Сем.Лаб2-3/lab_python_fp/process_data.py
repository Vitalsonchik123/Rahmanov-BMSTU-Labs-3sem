import json
import sys
import random
from time import time

def print_result(func):
    def wrapped(arg):
        print(func.__name__)
        res = func(arg)
        if isinstance(res, list):
            for item in res:
                print(item)
        else:
            print(res)
        return res
    return wrapped

class cm_timer_1:
    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f'time: {time() - self.start}')

path = r"C:\Users\Счастливый\Desktop\Отчёты по проге\Питон\lab_python_fp\data_light.json"

with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(list({str.lower(d['job-name']): d['job-name'] for d in arg}.values()), key=str.lower)

@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))

@print_result
def f4(arg):
    salaries = [random.randint(100000, 200000) for _ in arg]
    return [f"{prof}, зарплата {sal} руб." for prof, sal in zip(arg, salaries)]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
