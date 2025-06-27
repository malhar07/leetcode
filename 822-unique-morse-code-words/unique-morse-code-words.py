class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_set = set()
        for word in words:
            word_to_morse = [] 
            for char in word:
                ind = ord(char) - ord('a')
                word_to_morse.append(morse[ind])
            morse_set.add("".join(word_to_morse))
        return len(morse_set)
            
