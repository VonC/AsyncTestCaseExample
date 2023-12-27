# tests/test_async_module.py
from tests.async_test_case import AsyncTestCase
from async_modules import async_add


class TestAsyncModule(AsyncTestCase):
    def test_async_add(self):
        print("Starting test_async_add")

        async def coro():
            print("Starting coroutine in test_async_add")
            result = await async_add(5, 3)
            print("Finished awaiting in test_async_add")
            self.assertEqual(result, 8)

        self.run_async_test(coro())
        print("Finished test_async_add")

    def test_dummy(self):
        print("Running test_dummy")
        self.assertTrue(True)
