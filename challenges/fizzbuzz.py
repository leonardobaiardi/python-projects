#print 1 .. 100.
#print "Fizz" if divisible by 3.
#print "Buzz" if divisible by 5.
#print "FizzBuzz" if divisible by 3 and 5.

for x in range (0,99):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz") 
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        pass