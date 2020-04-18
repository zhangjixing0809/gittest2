import threading
import time
import queue
import requests
from multiprocessing import Process, Lock, Queue

# 多线程
# q = queue.Queue()
# lock = threading.Lock()
#
#
# def get_url_code():
#     """
#     获取url状态码
#     """
#     res = requests.get(i)
#     code = res.status_code
#     return f'获取的url是:{i}，状态码为{code}'
#
#
# def productor_url(idnum, url_code):
#     """
#     队列消息推送
#     """
#
#     q.put(f'线程{idnum}生产的数据：{url_code}')
#
#
# def consumer(idnum):
#     """
#     队列消息消费
#     """
#     while True:
#         try:
#             data = q.get(block=False)
#         except queue.Empty:
#             break
#         with lock:
#             print(f'消费线程{idnum}消费的数据是》》》', data)
#         time.sleep(.1)
#         q.task_done()
#
#
# def get_url_code_thread(n):
#     for i in range(n):
#         re = threading.Thread(target=productor_url, args=(i, get_url_code()))
#         re.start()
#
#
# def consumer_thread(n):
#     for i in range(n):
#         re = threading.Thread(target=consumer, args=(i,))
#         re.start()
#
#
# if __name__ == '__main__':
#
#     url = ['https://www.baidu.com/', 'https://www.163.com/', 'https://www.sina.com/']
#     for i in url:
#         get_url_code_thread(10)
#         consumer_thread(10)
#         q.join()


# 多进程

def get_url_code():
    res = requests.get(i)
    code = res.status_code
    return f'获取的url是:{i}，状态码为{code}'


def productor_url(idnum, url_code, q):
    """
    队列消息推送
    """

    q.put(f'进程{idnum}生产的数据：{url_code}')


def consumer(idnum, q, lock):
    """
    队列消息消费
    """
    while True:
        try:
            data = q.get(block=False)
        except queue.Empty:
            break
        with lock:
            print(f'消费进程{idnum}消费的数据是》》》', data)
        time.sleep(.1)


def get_url_code_process(n):
    for i in range(n):
        re = Process(target=productor_url, args=(i, get_url_code(), q))
        re.daemon = False
        re.start()


def consumer_process(n):
    for i in range(n):
        re = Process(target=consumer, args=(i, q, lock))
        re.daemon = False
        re.start()


if __name__ == '__main__':
    q = Queue()
    lock = Lock()
    url = ['https://www.baidu.com/', 'https://www.163.com/', 'https://www.sina.com/', 'https://www.tingyun.com/']
    for i in url:
        get_url_code_process(3)
        consumer_process(3)

