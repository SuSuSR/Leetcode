"""
2021.11.04
------------------------
217. 存在重复元素

给定一个整数数组，判断是否存在重复元素。
如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
------------------------
直接用list.set()函数，把重复的整合了，看整体的length

------------------------
执行用时：40 ms
内存消耗：19.7 MB
"""


def set_repeat(nums_list):
    return len(nums_list) != len(set(nums_list))


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    set_repeat(nums)
