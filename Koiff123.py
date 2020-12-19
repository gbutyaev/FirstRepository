from Factorial import fact

n = int(input())
k = int(input())
z = n - k

def calc(n,k):
	C = int(fact(n) / (fact(k) * fact(z)))
	
	return C	

calc(n,k)

f=open('binomkaf.txt','r')
text=f.read()
print(text)
for i in text:
	alist=text.replace('\n','').split(' ')#создаем список
alistint=[int(item) for item in alist]
a3=alistint[2::3]
a2=alistint[1::3]
a1=alistint[::3]
print(alistint)
print(a1)
print(a2)
print(a3)
count=-1
for i in a1:#создаем список с четными индексами элементами
	count+=1
	for j in a2:
			z=a1[count]-a2[count]
			for r in a3:
				if calc(i,j)==r:
					print("That's great")
					print(calc(i,j))
				
				
