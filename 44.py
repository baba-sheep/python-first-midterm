month = int(input("請輸入月份："))
day = int(input("請輸入日期："))
a = (month*2 + day) % 3
if a == 0:
    print("普通")
elif a == 1:
    print("吉")
elif a == 2:
    print("大吉")
