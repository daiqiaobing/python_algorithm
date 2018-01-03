# -*- coding: utf-8 -*-
import unittest

import copy

from algorithm.basic.binary_chop import binary_chop
from algorithm.basic.find_repeate_str import FirstRepeat, Coder
from algorithm.basic.sort import bubble, choose, insert, quick
from algorithm.constant import FIND_REPEAT_STR_CODER, SORT_ARR, SORT_SMALL_LARGE, SORT_LARGE_SMALL, SORT_ARR1, \
    SORT_SMALL_LARGE1, SORT_LARGE_SMALL1


class TestBasic(unittest.TestCase):

    def test_binary_chop(self):
        pos = binary_chop(data=[2, 13, 4, 1, 3, 3, 44, 13], size=8, number=44)
        assert not pos == -1

    def test_find_repeat(self):
        FirstRepeat().findFirstRepeat('sadasas', 7)
        coder = FIND_REPEAT_STR_CODER
        result = Coder().findCoder(coder, 24)
        assert result is not None

    def test_bubble(self):
        result = bubble(SORT_ARR)
        assert result == SORT_SMALL_LARGE or result == SORT_LARGE_SMALL

    def test_choose(self):
        result = choose(SORT_ARR)
        assert result == SORT_SMALL_LARGE or result == SORT_LARGE_SMALL

    def test_insert(self):
        result = insert(SORT_ARR)
        assert result == SORT_SMALL_LARGE or result == SORT_LARGE_SMALL

    def test_quick(self):
        result = quick(copy.deepcopy(SORT_ARR1), 0, len(SORT_ARR)-1)
        assert result == SORT_SMALL_LARGE1 or result == SORT_LARGE_SMALL1


if __name__ == '__main__':
    unittest.main()
