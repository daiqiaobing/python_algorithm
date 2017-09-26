# -*- coding: utf-8 -*-
def binary_chop(data, size, number):
    """
    二分法查找对应的元素的所在位置
    :param data:
    :param size:
    :param number:
    :return:
    """
    if size == 1:
        if data[0] == number:
            return 0
        return -1
    if size == 0:
        return -1
    split_size = int(size/2)
    data1 = data[0:split_size]
    data2 = data[split_size:size]
    result1 = binary_chop(data=data1, size=len(data1), number=number)
    if result1 != -1:
        return result1
    result2 = binary_chop(data=data2, size=len(data2), number=number)
    if result2 != -1:
        return result2 + split_size
    return -1


if __name__ == '__main__':
    pos = binary_chop(data=[2, 13, 4, 1, 3, 3, 44, 13], size=8, number=44)
    print pos
