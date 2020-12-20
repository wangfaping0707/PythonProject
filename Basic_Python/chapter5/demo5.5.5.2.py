# while True:
#     word = input("Please enter your name:")
#     if not word:
#         break
#     print('The word is', word)

from math import sqrt

for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Don't find it !")
