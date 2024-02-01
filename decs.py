# def flip(func):
#     def wrapper_func(*args, **kwargs):
#         args = args[::-1]
#         return func(*args, **kwargs)
#     return wrapper_func
#
#
# def introduce_on_debug(func):
#     def wrapp()
#
#
#
#
#
# @introduce_on_debug
# def identity(x):
#     return x
#
#
# # debug == False
# identity(239)
#
#
#
# @flip
# def div(x, y, show=False):
#     res = x / y
#     if show:
#         print(res)
#     return res
#
#
# div(2, 4, show=True)
# # ожидаемый вывод 2
















def bench(func):
    import time

    def wrapper():
        start = time.time()
        func()
        finish = time.time()
        print(f'Наша функция выполнялась {finish - start} секунд')
    return wrapper

@bench
def fetch_webpage():
    import requests
    webpage = requests.get('https://google.com')

fetch_webpage()
