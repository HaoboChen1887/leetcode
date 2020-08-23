class Solution:
    # scan from both sides, if both encounter a vowel, swop
    # otherwise move pointer until both are vowels or when pointers crossover
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        vowels = "aeiouAEIOU"
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] in vowels:
                right -= 1
            else:
                left += 1
        return ''.join(s)