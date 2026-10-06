# counting method
# def is_anagram(a, b):
#     if len(a) != len(b):
#         return False
#     counts = {}
#     for ch in a:
#         if ch in counts:
#             counts[ch] += 1
#         else:
#             counts[ch] = 1
#     for ch in b:
#         if ch not in counts:
#             return False
#         counts[ch] -= 1
#         if counts[ch] < 0:
#             return False
#     return True
# print(is_anagram("listen", "silent"))  # True
# print(is_anagram("hello", "world"))    # False


#sorded method
# a = input("1st word: ")
# b = input("2nd word: ")
# print(sorted(a) == sorted(b))
