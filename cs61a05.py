#Higher-Order Functions
from math import pi, sqrt

# def area(r, shape_constant)
#     assert r>0, 'A length should be positive'
#     return r*r* shape_constant

# def area_square(r):
#     return area(r,1)

# def area_circle(r):
#     return area(r,pi)

# def area_hexagon(r):
#     return area(r, 3*sqrt(3)/2)

# def summation(n, term):
#     total , k = 0 , 1
#     while k<=n:
#         total , k = total + term(k), k+1
#     return total

# def identity(x):
#     return x

# def cube(x):
#     return pow(x, 3)

# def sum_naturals(n):
#     """Sum the first N natural numbers.

#     >>> sum_naturals(5)
#     15
#     """

#     # total , k = 0 , 1
#     # while k <= n:
#     #     total , k = total + k, k + 1
#     return summation(n, lambda x : x)

# def sum_cubes(n):
#     """ Sum the first N cubes.

#     >>> sum_cubes(5)
#     225
#     """
#     # total , k  = 0 , 1
#     # while k <=n:
#     #      total, k = total + pow(k,3), k+1
#     return summation(n, lambda x : pow(x,3))

# def make_adder(n):
#     def adder(k):
#         return k+n
#     return adder

def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n+k)
    return next_sum

print_sums(1)(3)(5)