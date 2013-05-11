'''
unittest`ы похабру с использованием декоратора
'''
import unittest

def run_once(f):
    """
    Мемоизация. Не зависит от аргументов.
    """
    def _f(*args, **kwargs):
        if not hasattr(_f, "_retval"):
            _f._retval = f(*args, **kwargs)
        return _f._retval
    return _f


class Test(unittest.TestCase):
    def test_run_once(self):
        @run_once
        def inc(n):
            return n + 1

        # это результат вызова функции inc()...
        self.assertEqual(inc(7), 8)
        # ...а это -- сохраненное значение
        self.assertEqual(inc(2), 8)

if __name__ == "__main__":
    unittest.main()