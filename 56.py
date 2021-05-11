meal = {"1A":"127","2A":"117","3A":"137","4A":"99","5A":"115",
        "1B":"140","2B":"130","3B":"150","4B":"112","5B":"128"}
order = input("請選擇主餐及升級的套餐:")
if order in meal:
    a = int(meal[order])
drink = input("是否升級成大杯飲料:")
if drink == "是":
    b = a + 7
else :
    b = a
fries = input("是否升級成大署:")
if fries == "是":
    c = b + 13
else :
    c = b
print("總共為",str(c),"元")