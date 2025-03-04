class Solution:
    def maxNumberOfBalloonsFirstTry(self, text: str) -> int:
        count = {
            "b": 0,
            "a": 0,
            "l": 0,  # 2x
            "o": 0,  # 2x
            "n": 0,
        }
        for char in text:
            if char in count:
                count[char] += 1

        # check the maximum number of ballon
        nums = []
        for char, val in count.items():
            if char in ("l", "o"):
                nums.append(val // 2)
            else:
                nums.append(val)
        return min(nums)

    def maxNumberOfBalloons(self, text: str) -> int:
        count = {
            "b": 0,
            "a": 0,
            "l": 0,  # 2x
            "o": 0,  # 2x
            "n": 0,
        }
        for char in text:
            if char in ("l", "o"):
                count[char] += 1 / 2
            elif char in count:
                count[char] += 1

        return int(min(count.values()))
