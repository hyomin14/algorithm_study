# pair의 min 합산했을 때 최대가 되려면 min() 값이 되도록 커야함 -> 오름차순 정렬하면 항상 최대 min() 페어 유지 가능
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        nums.sort()

        # pair에 대해 일일이 계산하지 않고 짝수 번째 값을 더하면 됨
        for i in range(0, len(nums), 2):
            result += nums[i]

        return result
        # runtime : 283ms


'''
# pythonic way
def arrayPairSum(self, nums: List[int]) -> int:
    return sum(sorted(nums)[::2])
'''
