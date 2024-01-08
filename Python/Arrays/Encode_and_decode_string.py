class Codec:
    #  use a delimiter, which is a special character or sequence of characters that we insert between each string when we combine them into one.
    # non-ASCII delimiter 
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return 'π'.join(strs)
        # join() method takes all items in an iterable and joins them into one string.
        # Syntax
        # string.join(iterable)


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split('π')
        # split() method splits a string into  alist
        # Syntax
        # string.split(separator, maxsplit)
        # separator specifies when to split the string, by default any whitespace is a separator
        #max split is how many splits to do , default is -1, all occurences

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
