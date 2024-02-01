def palindrome(number: str) -> bool:
    l = 0
    r = len(number) - 1
    while l <= r:
        if number[l] != number[r]:
            return False
        l += 1
        r -= 1
    return True


def romanian(s: str) -> int:
    my_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    ans = 0
    # for i in range(len(s)):
    #     if (i < len(s) - 1) and (my_dict[s[i]] < my_dict[s[i + 1]]):
    #         ans -= my_dict[s[i]]
    #     else:
    #         ans += my_dict[s[i]]
    s = s.replace('IV', 'IIII').replace('IX', 'VIIII').replace('XL', 'XXXX').replace('XC', 'LXXXX')
    for i in s:
        ans += my_dict[i]
    return ans
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # my_number = 0
    # for i in range(len(s) - 1):
    #     if (s[i] == 'I') and (s[i + 1] == 'V' or s[i + 1] == 'X'):
    #         my_number -= 2
    #     if (s[i] == 'X') and (s[i + 1] == 'L' or s[i + 1] == 'C'):
    #         my_number -= 20
    #     if (s[i] == 'C') and (s[i + 1] == 'D' or s[i + 1] == 'M'):
    #         my_number -= 200
    #     my_number += my_dict[s[i]]
    # my_number += my_dict[s[len(s) - 1]]
    # return my_number

#
# n, m = map(int, input().split())
# matrix = [[0] * m for i in range(n)]
# dx, dy, x, y = 0, 1, 0, 0
# for i in range(1, n * m + 1):
#     matrix[x][y] = i
#     if matrix[(x + dx) % n][(y + dy) % m]:
#         dx, dy = dy, -dx
#     x += dx
#     y += dy
# for line in matrix:
#     print(*(f'{i:<3}' for i in line), sep=' ')















def palindrome(x: str) -> bool:
    x = x.lower()
    l = 0
    r = len(x) - 1
    while l < r:
        if x[l] != x[r]:
            return False
        l += 1
        r -= 1
    return True

print(palindrome('Шалаш'))


def romain(s: str):
    my_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    ans = 0
    for i in range(len(s) - 1):
        if my_dict[s[i]] < my_dict[s[i + 1]]:
            ans -= my_dict[s[i]]
        else:
            ans += my_dict[s[i]]
    ans += my_dict[s[len(s) - 1]]
    return ans


print(romain('I'))

def sum_digits(num):
    return sum(int(x) for x in str(num))


print(sum_digits(123))
