#윤년구하기
A= input()
A=int(A)

if(A%4 == 0 and A%100 != 0):
    print("1")
elif(A%400 == 0):
    print("1")
else:print("0")
