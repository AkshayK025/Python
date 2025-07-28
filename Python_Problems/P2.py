#Print numbers from 1 to 100. For multiples of 3, print "Fizz"; 
# for multiples of 5, print "Buzz"; for both, print "FizzBuzz".

# for i in range(1,100+1):
#     if i%3==0 and i%5==0:
#         print(i,"FizzBuzz")
#     if i%3==0:
#         print(i,"Fizz")
#     elif i%5==0:
#         print(i,"Buzz")
#     else:
#         print(i)


def fiz(i):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
    # return i

fiz(90)