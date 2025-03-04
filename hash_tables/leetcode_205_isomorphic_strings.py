class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # egg(011) <-> add(011)
        # foo(011) <-> bar(012)
        # paper(01023) <-> title(01023)
        if len(s) != len(t):
            return False
        # encode
        source_map = {}
        source_char_idx = 0
        target_map = {}
        target_char_idx = 0
        for char_s, char_t in zip(s, t):
            if char_s in source_map:
                encode_s = source_map[char_s]
            else:
                encode_s = source_char_idx
                source_map[char_s] = source_char_idx
                source_char_idx += 1

            if char_t in target_map:
                encode_t = target_map[char_t]
            else:
                encode_t = target_char_idx
                target_map[char_t] = target_char_idx
                target_char_idx += 1
            if encode_s != encode_t:
                return False
        return True
