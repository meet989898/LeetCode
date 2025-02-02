class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append((timestamp, value))
        else:
            self.timeMap[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.timeMap:
            return ""

        res = 0
        times = self.timeMap[key]

        left, right = 0, len(times) - 1

        while left <= right:
            mid = (left + right) // 2

            if times[mid][0] <= timestamp:
                left = mid + 1

                res = times[mid][1]

            else:
                right = mid - 1

        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
