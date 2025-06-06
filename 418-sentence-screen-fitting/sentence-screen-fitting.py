class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:

        s = " ".join(sentence) + " "
        L = len(s)
        
        ptr = 0
        
        for _ in range(rows):
            ptr += cols

            if s[ptr % L] == " ":
                ptr += 1
            else:

                while ptr > 0 and s[(ptr - 1) % L] != " ":
                    ptr -= 1
        
        # 4. After all rows, 'ptr // L' tells us how many full copies of s fit.
        return ptr // L