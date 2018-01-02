# -*- coding: utf-8 -*-
import copy


def bubble(arr):
    """冒泡排序"""
    cur = copy.deepcopy(arr)
    for i in range(len(cur) - 1):
        for j in range(i + 1, len(cur)):
            if cur[j] < cur[i]:
                tmp = cur[j]
                cur[j] = cur[i]
                cur[i] = tmp
    return cur


def choose(arr):
    """选择排序"""
    cur = copy.deepcopy(arr)
    for i in range(len(cur) - 1, 0, -1):
        k = 0
        for j in range(1, i + 1):
            if cur[j] > cur[k]:
                k = j
        if k != i:
            tmp = cur[k]
            cur[k] = cur[i]
            cur[i] = tmp
    return cur


def insert(arr):
    """插入排序"""
    cur = copy.deepcopy(arr)
    for i in range(1, len(cur)):
        j = i
        tmp = cur[i]
        while j > 0 and cur[j - 1] > tmp:
            cur[j] = cur[j - 1]
            j = j - 1
        cur[j] = tmp
    return cur
