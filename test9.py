a=input("please enter your name : ")
b=input("please enter your last name : ")
c=float(input("please enter your first lesson : "))
d=float(input("please enter your second lesson : "))
e=float(input("please enter your third lesson : "))
avg=float(c+d+e)/3
if avg>=17:
    result = "Grate"
if avg<17 :
    result = "Normal"
if avg<12: 
    result= "Fail"
print("name : ",a,"\tlastname : ",b,"\taverage : " ,avg,"\tstatus : ",result)
