import threading
import time
import unittest


class LeakTest:
    def __init__(self):
        self.orig_threads = {}

    def check_for_leaks(self, timeout=5):
        self.orig_threads = threading.enumerate()
        time.sleep(timeout)  # allow other threads to finish
        curr_threads = threading.enumerate()
        leaked_threads = [t for t in curr_threads if t not in self.orig_threads]

        for t in leaked_threads:
            print(f'Leaked Thread: {t}')


class MyTest(unittest.TestCase):
    def setUp(self):
        self.leaktest = LeakTest()

    def test_that_may_leak_threads(self):
        # .. your test code here that may leak threads
        pass

    def tearDown(self):
        # This will print any new threads (leaked) started by test method
        self.leaktest.check_for_leaks()
