def absolute_value(x):
    if x > 0:
        return x
    elif x < 0:
        return -x
    else:
        return 0

def funky (x):
    if x<0:
        print ("negatory")
    elif x%2 == 0:
        return "I can't even"
    elif x%3 == 0:
        return "3 of a kind"

def fib(n):
    cur = 0
    nxt = 1

    i = 0

    while i < n:
        i = i + 1
        
        nxt_nxt = cur + nxt
        cur = nxt
        nxt = nxt_nxt

    return cur

