class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        visited = {}
        for num in nums:
            visited[num] = visited.get(num, 0) + 1  # cleaner way

        # Sort items by frequency (value), descending
        sorted_items = sorted(visited.items(), key=lambda item: item[1], reverse=True)

        # Grab the top k keys
        return [item[0] for item in sorted_items[:k]]


            