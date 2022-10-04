import sys
from io import StringIO
import unittest

def resolve():
  N = int(input())
  s = f'{N:02x}'
  print(s.upper())
  
class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """99"""
        output = """63"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """12"""
        output = """0C"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0"""
        output = """00"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """255"""
        output = """FF"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
