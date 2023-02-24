class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# brute-force : O(n^2)
# runtime : 3889ms


'''
# 최적화 1. 모든 조합 비교하지 않고 target에서 첫번째 값을 뺀 값이 nums에 존재하는지 탐색
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            sub = target - n
            if sub in nums[i+1:]:
                return [i, nums[i+1:].index(sub) + (i+1)] 
# runtime : 620ms
# 시간복잡도는 O(n^2)이지만 in 연산이 파이썬 레벨에서 매번 값을 비교하는 것보다 빠름


# 최적화 2.target에서 첫번쨰 값을 뺀 결과 '키'를 조회하는 방식
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        # index와 값을 바꾸어서 딕셔너리에 저장
        for i, n in enumerate(nums):
            nums_dict[n] = i

        # target에서 첫번째 수를 뺀 결과를 key로 조회
        for i, n in enumerate(nums):
            # target - n 이라는 key 값이 dictionary에 있고 n과 같은 index가 아니면
            if (target - n) in nums_dict.keys() and i != nums_dict[target - n]: 
                return [i, nums_dict[target - n]]      
# runtime : 71ms
# 딕셔너리는 해시 테이블로 구현되어 있고, 평균적으로 O(1)


# 최적화 3. 위 방법에서 조회 구조 개선
# 저장과 조회를 2개의 for문으로 처리한 방식을 하나의 for문으로
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i, n in enumerate(nums):
            if (target - n) in nums_dict.keys():
                return [nums_dict[target - n], i]
            nums_dict[n] = i
# runtime : 57ms
# 위 방식에 비해 성능상 큰 이점 없음
        
'''
