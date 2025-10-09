class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            string_array = []
            for c in s:
                string_array.append(c)
            
            string_array = sorted(string_array, key=lambda x: ord('a') - ord(x))
            anagram_key = ""
            for c in string_array:
                anagram_key += c

            if anagram_key in groups:
                groups[anagram_key].append(s)
            else:
                groups[anagram_key] = [s]
        result = []
        for lists in groups:
            result.append(groups[lists])

        return result