class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counts = {}
        max_count = 0
        # max_freq is the most common char in the string
        max_freq = 0
        for r in range(len(s)):

            # update counts
            if s[r] in counts:
                counts[s[r]] += 1
            else:
                counts[s[r]] = 1

            # check for update max_freq
            max_freq = max(max_freq, counts[s[r]])

            # check if string has too many replacements
            if (r - l + 1 - max_freq) > k:
                counts[s[l]] = counts[s[l]] - 1
                l += 1
            else:
                max_count = max(max_count, r - l + 1)
        return max_count