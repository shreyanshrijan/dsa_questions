from __future__ import annotations

def longestPalindrome(s: str) -> str:
        lst_s = [x for x in s]
        i = 0
        j = 0
        final_string = []
        max_length = []
        while j < len(lst_s):
            if unique_list(lst_s[i:j + 1]):
                final_string.append(lst_s[j])
                j = j +1
            else:
                max_length.append(len(final_string))
                i = sum(max_length)
                final_string = []

        return max(max_length)
                

def unique_list(lst):
    if len(set(lst)) == len(lst):
        return True
    else:
        return False
    

if __name__ == "__main__":
    s= "abcabcbb"
    print(longestPalindrome(s))
