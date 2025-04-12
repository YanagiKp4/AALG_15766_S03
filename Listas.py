a =["Juan",20,1.80,True]
print(a[len(a)-1])
print(a[-1])
print(a[-2])

b=[4,2,6,3]
print(len(b))
print(max(b))
print(min(b))
print(sum(b))
print(sum(b)/len(b))

c=a+b
print(c)

for x in b:
    print(x)

#Destructuracion    
p="mesa"
q="silla"
print(p,q)
tmp=p
p=q
q=tmp
print(p,q)
p,q=q,p
print(p,q)

def sum5 (e,f):
    return e+5, f+5

x,y = sum5 (2,5)
print(x,y)


busca=5
if busca in b:
    print("Encontrado")





