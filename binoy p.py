d={'apple':10,'milk':50}
t=0
while True:
	a=input("enter item")
	b=d.get(a)
	v=int(input("entrr qty"))
	c=b*v
	t=t+c
	s=input("enter continue or not")
	if s in 'nN':
		break
print("total cost",t)




l=[]
for i in range(5):
		a=int(input("enter marks"))
		l.append(a)
avg=sum(l)/5
print(avg)
if avg>89:
	print("avg=",avg," grade = A")
elif avg>=70 and avg<90:
	print("avg=",avg," grade = B")
elif avg>=50 and avg<70:
	print("avg=",avg ," grade = C")
else:
	print("avg=",avg,"grade=F")
