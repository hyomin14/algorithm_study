class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        # s = s[::-1] -> 공간 복잡도를 O(1)로 제한하여서 오류 발생 -> s[:] = s[::-1]
