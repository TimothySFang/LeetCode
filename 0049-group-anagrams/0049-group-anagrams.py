class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}
        for string in strs:
            curr_str = [0] * 26
            for c in string:
                curr_str[ord(c) - ord('a')] += 1
            curr_str = tuple(curr_str)
            
            if curr_str in grouped_anagrams:
                grouped_anagrams[curr_str].append(string)
            else:
                grouped_anagrams[curr_str] = [string]

        res = []
        for key in grouped_anagrams:
            res.append(grouped_anagrams[key])
        return res