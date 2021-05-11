poker=[]
for i in range(5):
  a = input()
  if a == "A":
    a = 1
  if a == "J":
    a = 11
  if a == "Q":
    a = 12
  if a == "K":
    a = 13
  poker.append(int(a))
print(sum(poker))  
