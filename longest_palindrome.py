class Solution:
    def longestPalindrome(s: str) -> str:
        letter_count = len(s)
        for i in range(2, letter_count + 1):
            sub_word = [s[k:k + i] for k in range(0, letter_count - i + 1)]
            a = [(x, Solution.check_palindrome(x)) for x in sub_word]
            for word, status in a:
                if status:
                    longest_palindrome_word = word
        return longest_palindrome_word

    def check_palindrome(s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    s = 'banab'
    print(Solution.longestPalindrome(s))
