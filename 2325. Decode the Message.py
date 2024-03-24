class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        given = {' ':' '}
        i = 0
        res = ''
        key = key.replace(' ','')

        letter = string.ascii_lowercase

        for char in key:
            if char not in given:
                given[char] = letter[i]
                i += 1

        for char in message:
            res += given[char]

        return res