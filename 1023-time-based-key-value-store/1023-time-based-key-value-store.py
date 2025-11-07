class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)  # key -> [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # timestamps are guaranteed to be non-decreasing
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store.get(key, [])
        if not arr:
            return ""

        # find index of first element with timestamp > given timestamp
        # we add chr(127) to ensure correct tuple comparison
        i = bisect_right(arr, (timestamp, chr(127)))

        # if i == 0, all timestamps are greater than target -> return ""
        if i == 0:
            return ""

        # otherwise, the answer is at i-1
        return arr[i - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)