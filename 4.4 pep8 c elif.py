year = int(input())

if year % 400 == 0:
    print("да")
elif year % 100 == 0:
    print("нет")
elif year % 4 == 0:
    print("да")
else:
    print("нет")
