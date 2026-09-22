class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count_map={}
        for num in nums1:
            count_map[num]=count_map.get(num,0)+1
        result = []
        for num in nums2:
            if num in count_map and count_map[num]>0:
                result.append(num)
                count_map[num] -= 1
        return result
        