class Solution:
    def isPalindrome(self, s: str) -> bool:
        # exceptions
        if len(s) <= 1:
            return True

        # set two pointers
        left_idx, right_idx = 0, len(s) - 1
        left_char = right_char = ""

        print(left_idx, right_idx)
        for _ in range(len(s)):
            # move left idx
            while left_idx < right_idx:
                if s[left_idx].isalnum():
                    break
                left_idx += 1
            left_char = s[left_idx].lower()

            # move right idx
            while right_idx > left_idx:
                if s[right_idx].isalnum():
                    break
                right_idx -= 1
            right_char = s[right_idx].lower()

            # compare
            if left_char != right_char:
                return False

            if left_idx >= right_idx:
                break

            # next idx
            left_idx += 1
            right_idx -= 1

        return True
