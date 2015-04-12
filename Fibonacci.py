a0 = 1
a1 = 1
a2 = 2
fib = list()
while a1 < 4000000:
   a0 = a1
   a1 = a2
   a2 = a1 + a0
   if a0 % 2 == 0:
      fib.append(a0)
	  
print sum(fib)
