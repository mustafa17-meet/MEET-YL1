n = int (input("enter some number"))
x = 0
while x <= n:
	def divisors():
		if n % x == 0:
			print(x)
			x=x+1
