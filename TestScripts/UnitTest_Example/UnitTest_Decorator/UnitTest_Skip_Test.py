import unittest


class suiteTest(unittest.TestCase):
    a = 40
    b = 60

    def testadd(self):
        """Add"""
        result = self.a + self.b
        print(result)
        self.assertEqual(result, 100)

    @unittest.skipIf(a > b, "Skip over this routine")
    def testsub(self):
        """sub"""
        result = self.a - self.b
        print(result)
        self.assertTrue(result == -20)

    @unittest.skipUnless(b == 60, "Skip over this routine")
    def testdiv(self):
        """div"""
        result = self.a / self.b
        print(result)
        self.assertTrue(result == 0.6666666666666666)

    if __name__ == '__main__':
        unittest.main()