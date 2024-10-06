from __future__ import annotations

def wildcard_matching(s: str, p: str) -> bool:
    if p == '*':
        return True
    
    if len(s) != len(p):
        return False

    for letter in range(len(s)):
        if p[letter] == '*':
            return True
        if (s[letter] != p[letter]) & (p[letter] != '?'):
            return False
    return True


if __name__ == "__main__":
    s = 'aa'
    p = '?a'
    print(wildcard_matching(s, p))