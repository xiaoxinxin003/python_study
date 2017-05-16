# import fibo



s = 'hello world'

print str(s)
print repr(s)

for x in range(1, 11):
     print repr(x).rjust(2), repr(x*x).rjust(3),
     # Note trailing comma on previous line
     print repr(x*x*x).rjust(4)


# print fibo.fib(1000)
#
# print fibo.fib2(100)
#
# print fibo.__name__
#
# fib = fibo.fib
#
# print fib(500)