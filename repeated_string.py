def repeatedString(s, n):
    # # n = input()
    # # s = list(input())
    # s_new = s
    # while len(s_new) < n:
    #     s_new = s_new + s
    #     return s_new
    # print
    return (s.count('a') * (n//len(s)) + s[:n%len(s)].count('a'))
    a = []
    a.extend()


s = input()
n = int(input())
print(repeatedString(s, n))

