from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.
    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b >= 0:
        return a + b
    
    else :
        return a - b

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.
    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a * a + b * b + c * c - min(a, b, c) ** 2

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.
    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    i =n-1
    while i > 0:
        if n%i==0:
            return i
        i -=1




def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.
    >>> if_function(True, 2, 3)
    2`
    >>> if_function(False, 2, 3)`
    3`
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result
    


def with_if_statement():
    """
    >>> result = with_if_statement()
    61A
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    Welcome to
    61A
    >>> print(result)
    None
    """
    print("Welcome to")
    print("61A")

    return if_function(cond(), true_func(), false_func())

# def if_function(, true_func(), false_func())
#     if cond():
#         return true_func()
#     else :
#         return false_func()

def cond():
    "*** YOUR CODE HERE ***"
    return 1
def true_func():
    "*** YOUR CODE HERE ***"

def false_func():
    "*** YOUR CODE HERE ***"


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
def hailstone(n):
    count = 1
    print(n)
    while n > 1:
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
        print(n)
        count = count + 1
    
    return count