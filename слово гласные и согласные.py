slovo=input('Введите слово ')
ag=slovo.count('a')
eg=slovo.count('e')
ig=slovo.count('i')
og=slovo.count('o')
ug=slovo.count('u')
d=len(slovo)
g=ag+eg+ig+og+ug
print('всего гласных',g)
s=d-g
print('Явсего согласных',s)
if ag==0:
    print('a=false')
else:
    print('a=',ag)
if eg==0:
    print('e=false')
else:
    print('e=',eg)
if ig==0:
    print('i=false')
else:
    print('i=',ig)
if og==0:
    print('o=false')
else:
    print('o=',og)
if ug==0:
    print('u=false')
else:
    print('u=',ug)



