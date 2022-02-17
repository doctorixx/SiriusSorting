from numba import njit

@njit(fastmath=True)
def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1, lenstr1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, lenstr2 + 1):
        d[(-1, j)] = j + 1

    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,  # deletion
                d[(i, j - 1)] + 1,  # insertion
                d[(i - 1, j - 1)] + cost,  # substitution
            )
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + 1)  # transposition

    return d[lenstr1 - 1, lenstr2 - 1]

# def check2(a,b):
#     dist = int(damerau_levenshtein_distance(a,b))
#
#
#     #Сравнение масивов
#     #введена лишняя буква спереди или сзади
#     if not len(a) == len(b):
#         for i in range(len(a)):
#             c = a
#             c[i] = ''
#             if damerau_levenshtein_distance(c,b) < dist:
#                 return f"{a} {dist} {c} {b}"
#
#
#         return 0
#
#