'''
二分查找，统计在左右两边，小于等于mid的个数cnt
当cnt 大于mid时，重复值在左边，[left,mid]，否则在右边，[mid+1,right]
'''
class Solution(object):
    def findDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #字典 哈希表
        table = set()
        for num in nums:
            if num not in table:
                table.add(num)
            else:
                return num

    def findDuplicate2(self, nums):
        #inplace 交换，改变原数组的顺序 T(n) = n  O(n) = o(l)
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                #注意下面的交换顺序
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp

    def findDuplicate(self, nums):
        # 排序，二分查找
        #不改变原数组的顺序，T(n) = n  O(n) = o(l)
        size = len(nums)
        left, right = 1, size - 1
        while left < right:
            mid = (left + right) >> 1
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1

            if cnt > mid:
                right = mid
            else:
                left = mid + 1
        return left


