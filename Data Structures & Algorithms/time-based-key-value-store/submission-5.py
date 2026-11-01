class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        current = self.hashMap.get(key, [])
        current.append([timestamp, value])
        self.hashMap[key] = current

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap or self.hashMap[key][0][0] > timestamp:
            return ""
        
        values = self.hashMap[key]
        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2

            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        return values[right][1]
        
