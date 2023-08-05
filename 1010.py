# @Jbj Zeehad 

total=0
i=0
while i<2:
    code=input()
    nu=input()
    price=format(float(input()),"0.2f")
    total=(float(price)*int(nu))+total
    i=i+1
total=format((total),"0.2f")
print("VALOR A PAGAR: R$ "+total)