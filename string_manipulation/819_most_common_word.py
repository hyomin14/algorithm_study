class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = [word for word in re.sub(r'[^a-zA-Z0-9]', ' ', paragraph).lower().split()
                     if word not in banned]
        # print(paragraph)
        counter = collections.Counter(paragraph)
        return counter.most_common(1)[0][0]
