import unittest
import minelaying

class MyTestCase(unittest.TestCase):
    def test_mined_number(self):
        rows, cols = (8, 8)
        mine_num = 10
        except_place = (2, 2)
        test_array = [['-' for i in range(cols)] for j in range(rows)]
        minelaying.lay_mine_random_place(test_array, mine_num, except_place)
        get_m = 0
        for line in test_array:
            get_m += line.count('m')
        self.assertEqual(get_m, mine_num)


if __name__ == '__main__':
    unittest.main()
