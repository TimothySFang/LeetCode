class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(timestamp, value)]
        else:
            self.store[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            values = self.store[key]
            
            # bisect / binsearch

            left, right = 0, len(values) - 1
            result = ""
            while left <= right:
                middle = (left + right) // 2
                ts, val = values[middle]
                if ts <= timestamp:
                    result = val
                    #search right
                    left = middle + 1
                else:
                    right = middle - 1
            
            return result

        return ""

    
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)