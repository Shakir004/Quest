# import unittest

# from calulations import stringreverse

# class TestCalculation(unittest.TestCase):

#     # def test_addPositiveNumber(self):
#     #     result = add(50,70)
#     #     self.assertEqual(result,120)
#     # def test_addNegativeNumber(self):
#     #     self.assertEqual(add(-20,-8),-28)

#     def test_string(self):
#         self.assertEqual(stringreverse("shakir"),"rikahs")
       

# unittest.main()


# import unittest

# from calulations import intigerreverse

# class TestIntReverse(unittest.TestCase):

#     def test_intReverse(self):
#         self.assertEqual(intigerreverse(123),321)


# unittest.main()


# unittest.main()


# import unittest

# from calulations import reverse_integer

# class TestIntReverse(unittest.TestCase):

#     def test_reverseInteger(self):
#         self.assertEqual(reverse_integer(-123),-321)


# unittest.main()





import unittest

from calulations import division,div

class TestIntReverse(unittest.TestCase):

    def test_reverseInteger(self):
        self.assertEqual(division(6,2),3)

    def test_division(self):
        self.assertEqual(div(-6,2),-3)

    

unittest.main()


