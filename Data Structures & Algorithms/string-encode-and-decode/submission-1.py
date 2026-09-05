class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            length = len(s)
            result += str(length) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        position = 0
        while position < len(s):
            delimiter_pos = s.find("#", position)
            length_str = s[position:delimiter_pos]
            length = int(length_str)
            string_start = delimiter_pos + 1
            actual_string = s[string_start:string_start + length]
            result.append(actual_string)
            position = string_start + length
        return result