class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = dict()
        for idx, st in enumerate(strs):
            st = ''.join(sorted(st))
            if st in count.keys():
                count[st].append(idx)
            else:
                count[st] = list()
                count[st].append(idx)
        result = []
        for key in count.keys():
            result.append([strs[i] for i in count[key]])
        return result
