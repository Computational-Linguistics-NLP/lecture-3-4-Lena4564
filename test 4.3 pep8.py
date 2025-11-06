a = int(input())
if a % 400 == 0:
    print("да")
if a % 4 == 0 and a % 100 != 0:
    print("да")
if a % 400 != 0 and (a % 4 != 0 or a % 100 == 0):
    print("нет")
