def fact(n):#Функция подсчета факториала
    if n==0:
        return 1
    else:
        return n * fact(n-1)

f=open("C:\\testi.txt","r")#считываем файл
text=f.read()#считываем файл
f.close()
for i in text:
	alist=text.replace('\n','').split(' ')#создаем список

print((alist))


alistint= [ int(item) for item in alist]#делаем элементы списка целыми числа
print(alistint)
a1= alistint[::2]#создаем список с четными индексами элементами
a2=alistint[1::2]#создаем список с нечетными индексами элементами
print(a2)
print(a1)
for i in a1:#создаем список с четными индексами элементами
	for j in a2:
		if fact(i)==j:
			print(fact(i))
			print("That's great")
			
	

		
			
		



#file = open("data.txt","r")
#values = file.read().split("\n")

#for i in values:
#	print(i*2)

#f.close()
