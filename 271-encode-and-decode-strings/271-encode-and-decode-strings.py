class Codec:
    def encode(self, strs: List[str]) -> str:
        str = ""
        for i, s in enumerate(strs):
            str += s
            if i < len(strs) - 1:
                str += chr(257)
        return str
            
        """Encodes a list of strings to a single string.
        """
        

    def decode(self, s: str) -> List[str]:
        strings = s.split(chr(257))
        return strings
        """Decodes a single string to a list of strings.
        """
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))