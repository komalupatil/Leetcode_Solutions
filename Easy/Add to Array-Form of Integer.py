class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        final_list = []
        output = str(int("".join(map(str, A))) + K)
        for i in output:
            final_list.append(int(i))
        return final_list