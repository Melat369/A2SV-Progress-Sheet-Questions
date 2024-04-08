class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        result = []
        morse_code= [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            morse = ""
            for char in word:
                morse += morse_code[ord(char)-97]
            if morse not in result:
                result.append(morse)
        return len(result)
                    