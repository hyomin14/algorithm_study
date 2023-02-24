# 자기 자신을 제외하고 왼쪽 곱셈 결과와 오른쪽 곱셈 결과 곱하기
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        # 자신의 왼쪽에 있는 수들의 곱
        temp = 1
        for i in range(len(nums)):
            result.append(temp)
            temp = temp * nums[i]
        # temp : 1 -> 1 -> 2 -> 6 -> 24
        # ex1의 경우 - result = [1, 1, 2, 6]

        # 자신의 오른쪽에 있는 수들의 곱
        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * temp
            temp = temp * nums[i]
        # temp : 1 -> 4 -> 12 -> 24 -> 24

        return result
