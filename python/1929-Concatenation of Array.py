class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        array=nums.copy()
        for i in range (0, len (nums)):
          array.append(nums[i])
        return array 