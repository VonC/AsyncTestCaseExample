import asyncio
import unittest


class AsyncTestCase(unittest.TestCase):
    loop = None

    @classmethod
    def setUpClass(cls):
        print("Setting up test case class")
        cls.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(cls.loop)

    @classmethod
    def tearDownClass(cls):
        print("Tearing down test case class")
        cls.loop.close()
        asyncio.set_event_loop(None)

    def run_async_test(self, coro):
        print(f"Running async test: {self._testMethodName}")
        return self.loop.run_until_complete(coro)
