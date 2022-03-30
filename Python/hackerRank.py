'''
n = int(input())
if n % 2:
    print("Weird")
    print("1")
else:
    if n in (2, 4):
        print("Not weird")
        print("2")
    elif n in range(6, 20):
        print("Weird")
        print("3")
    elif n > 20:
        print("Not Weird")
        print("4")
'''

c = "cdcdcjfkjd"
print(len(c))
