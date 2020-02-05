n=int(input("enter the number:"))
a=list(map(int,str(n)))
y=len(a)
b=list(map(lambda x:x**y,a))
if(sum(b)==n):
   print("number is armstrong")
else:
   print("number is not armstrong")
