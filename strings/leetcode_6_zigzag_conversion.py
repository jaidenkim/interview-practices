class Solution:
    """zigzag pattern
    |  /|  /|
    | / | / |
    |/  |/  |...
    """

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        zigzag_str = ""
        interval = 2 * (numRows - 1)
        length = len(s)

        for row_num in range(numRows):
            next_idx = row_num
            cnt = 0
            while next_idx < length:
                zigzag_str += s[next_idx]
                if row_num > 0 and row_num < numRows - 1:
                    if cnt == 0:
                        next_idx += interval - row_num * 2
                        cnt += 1
                    else:
                        next_idx += row_num * 2
                        cnt -= 1
                else:
                    next_idx += interval
        return zigzag_str
