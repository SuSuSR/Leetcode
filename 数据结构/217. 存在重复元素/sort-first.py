"""
2021.11.04
------------------------
217. 存在重复元素

给定一个整数数组，判断是否存在重复元素。
如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
---------------------------
先list.sort()排序，再比较nums[i]和nums[i+1]是否一样
time complexity: O(NlogN)，其中 NN 为数组的长度。需要对数组进行排序。
空间复杂度：O(logN)，其中 N为数组的长度。注意我们在这里应当考虑递归调用栈的深度。

----------------------------
执行用时：32 ms
内存消耗：17.6 MB
"""


# code
def repeat_variable(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            return True
    return False


if __name__ == '__main__':
    num_list = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    repeat_variable(num_list)

