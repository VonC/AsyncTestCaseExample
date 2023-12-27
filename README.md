# AsyncTestCaseExample

This project demonstrates a way to test asynchronous Python code using a custom `AsyncTestCase` class. This approach is designed to work with Python 3.11 and later, where the `asynctest.TestCase` class is no longer supported.

## Problem Statement

Context: [Stack Overflow question](https://stackoverflow.com/q/77642317/6309)

In Python 3.10 and earlier, the `asynctest.TestCase` class was commonly used for testing asynchronous code. This class provided `setUp` and `tearDown` methods that supported the initialization of dependencies and creation of test data.

However, Python 3.11 and later versions do not support `asynctest.TestCase`. The `unittest.IsolatedAsyncioTestCase` class is an alternative, but it uses a different event loop for each test. This can lead to the usage of different sessions, which may not be desirable in some cases.

## Solution

In this project, we define a custom `AsyncTestCase` class that extends `unittest.TestCase`. This class uses a single event loop for all tests, similar to `asynctest.TestCase`. It provides `setUpClass` and `tearDownClass` methods to initialize and clean up resources at the class level, and a `run_async_test` method to run asynchronous tests.

## Usage

To run a test, define a test case class that extends `AsyncTestCase` and use the `run_async_test` method to run an asynchronous test. For example:

```python
from tests.async_test_case import AsyncTestCase
from async_modules import async_add

class TestAsyncModule(AsyncTestCase):
    def test_async_add(self):
        async def coro():
            result = await async_add(5, 3)
            self.assertEqual(result, 8)

        self.run_async_test(coro())
```