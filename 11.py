date=input("請輸入月及日為:").split()
a=list(map(int,date))
for i in range(len(a)):
    x=a[0]
    y=a[1]
if(x==1):
    if(y>20):
        print("星座為:Aquarius")
    else:
        print("星座為:Capricorn")
elif(x==2):
    if(y>18):
        print("星座為:Pisces")
    else:
        print("星座為:Aquarius")
elif(x==3):
    if(y>20):
        print("星座為:Aries")
    else:
        print("星座為:Pisces")
elif(x==4):
    if(y>20):
        print("星座為:Taurus")
    else:
        print("星座為:Aries")
elif(x==5):
    if(y>21):
        print("星座為:Gemini")
    else:
        print("星座為:Taurus")
elif(x==6):
    if(y>21):
        print("星座為:Cancer")
    else:
        print("星座為:Gemini")
elif(x==7):
    if(y>22):
        print("星座為:Leo")
    else:
        print("星座為:Cancer")
elif(x==8):
    if(y>23):
        print("星座為:Virgo")
    else:
        print("星座為:Leo")
elif(x==9):
    if(y>23):
        print("星座為:Libra")
    else:
        print("星座為:Virgo")
elif(x==10):
    if(y>23):
        print("星座為:Scorpio")
    else:
        print("星座為:Libra")
elif(x==11):
    if(y>22):
        print("星座為:Sagittarius")
    else:
        print("星座為:Scorpio")
elif(x==12):
    if(y>21):
        print("星座為:Capricorn")
    else:
        print("星座為:Sagittarius")