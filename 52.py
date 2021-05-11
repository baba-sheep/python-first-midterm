dict1 = {}
n = int(input("輸入n值："))
for i in range (1,n+1):
    name = input("請輸入姓名：")
    email = input("請輸入電子郵件：")
    dict1[name] = email
surch = input("請輸入查詢電子郵件的姓名：")
if surch in dict1:
    print(surch + " 電子郵件帳號為 " + dict1[surch])
