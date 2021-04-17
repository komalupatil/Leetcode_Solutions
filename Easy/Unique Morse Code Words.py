#leetcode 804. Unique Morse Code Words

#Solution1
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--.."}
        result = set()
        for word in words:
            m = []
            for ch in word:
                m.append(codes[ch])
            morse = "".join(m)
            if morse not in result:
                result.add(morse)
        return len(result)

#Solution2

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        return len({''.join(d[ord(i) - ord('a')] for i in w) for w in words})
