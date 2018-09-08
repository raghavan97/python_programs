import concurrent.futures
import requests
import time

requests.packages.urllib3.disable_warnings()


class MyThreadPoolExample(object):
    def __init__(self):
        self.url_list = [
            'https://www.ucsc.edu',
            'http://www.riptideio.com',
            'https://raghavan97.github.io/',
            'https://news.google.com'
        ]
        self.completed_count = 0

    def my_callback(self, future):
        resp = future.result()
        if resp:
            print 'completed with status={}'.format(resp.status_code)
        self.completed_count += 1

    def load_url(self, url):
        try:
            resp = requests.get(url)
            return resp
        except Exception as e:
            print 'exception [{}] for url={}'.format(e, url)
            return None


    def run(self):
        tp_executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)

        for url in self.url_list:
            future = tp_executor.submit(self.load_url, url)
            future.add_done_callback(self.my_callback)

        while self.completed_count < len(self.url_list):
            time.sleep(2)

        print 'Completed all the requests'

tp = MyThreadPoolExample()
tp.run()
