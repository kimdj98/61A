# def wears_jacket_with_if(temp, raining):
#     """
#     >>> wears_jacket_with_if(90, False)
#     False
#     >>> wears_jacket_with_if(40, False)
#     True
#     >>> wears_jacket_with_if(100, True)
#     True
#     """
#     if temp < 60 or raining:
#         return True
#     else:
#         return False
    
# def wears_jacket(temp, raining):
#     return temp < 60 or raining

# def is_prime(n):
#     """
#     >>> is_prime(10)
#     False
#     >>> is_prime(7)
#     True
#     """
#     "*** YOUR CODE HERE ***"
#     i = n-1
#     while (i>1):
#         if n%i==0:
#             return False
#         i-=1
#     return True

def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result == None
    True
    """
    "*** YOUR CODE HERE ***"

    i=1
    while i<=n:
        if i%15==0:
            print("fizzbuzz")
            i+=1
        elif i%3==0:
            print("fizz")
            i+=1
        elif i%5==0:
            print("buzz")
            i+=1
        else:
            print(i)
            i+=1
    