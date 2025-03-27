class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        s = ""
        for i,v in enumerate(strs):
            
            s = s + v
            if i != len(strs)-1:  
                s = s + "©"
        
        return s

        
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        s = s.split("©")
        return s


        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))