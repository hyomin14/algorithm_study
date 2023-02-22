class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        # s 자체가 palindrome이거나 s의 길이가 1 이하이면 바로 return
        if s == s[::-1] or len(s) <= 1:
            return s
        # 문자열의 시작 인덱스와 끝 인덱스 조절하면서 생긴 substring으로 판단
        # i : start index
        for i in range(len(s)):
            # j : end index
            for j in range(len(s), i, -1):
                # i부터 j까지 substring 생성
                substring = s[i:j]
                # 뒤집었을 때도 같으면 substring은 palindrome임
                if substring == substring[::-1]:
                    # 길이를 기준으로 max 값 구함
                    result = max(result, substring, key=len)
        return result

# runtime : 6092 ms


'''
# 책 풀이
class Solution:
    def longestPalindrome(self, s: str) -> str:

        # 투 포인터가 중앙을 중심으로 확장하는 형태
        # 2칸, 3칸으로 구성된 투 포인터가 슬라이딩 윈도우처럼 앞으로 전진
        # 윈도우에 들어온 문자열이 palindrome이면 그 자리에서 멈추고 투 포인터가 확장
        # -> 짝수나 홀수 길이 palindrome 모두 판별 가능

        # palindrome 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        # 해당 사항이 없으면 바로 return
        if len(s) <= 1 or s == s[::-1]:
            return s

        result = ''

        # 슬라이딩 윈도우 우측으로 이동
        for i in range(0, len(s) - 1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        
        return result

# runtime : 111 ms        
'''
