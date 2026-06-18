class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result= defaultdict(list) #defaultdict lets us use append when dict is empty

        for s in strs:
            key = [0]*26
            for i in s:
                key[ord(i) - ord('a')] += 1
            result[tuple(key)].append(s) #cannot use list as a key so need to put tuple

        return list(result.values())