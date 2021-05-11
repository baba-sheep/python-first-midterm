chi=int(input("國文:"))
eng=int(input("英文:"))
mat=int(input("微積:"))
phy=int(input("體育:"))
com=int(input("程設:"))
dict1={chi:"國文",eng:"英文",mat:"微積",phy:"體育",com:"程設"}
list1 = [chi,eng,mat,phy,com]
avg = (chi+eng+mat+com+phy)/5
print("平均分數:",avg)
m = min(list1)
M = max(list1)
m1 = dict1[m]
M1 = dict1[M]
print("最高分科目:",M1,M,"分")
print("最低分科目:",m1,m,"分")
