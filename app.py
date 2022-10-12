def test():
    return 'test 2'
def suma(num):
    a = 0
    for i in num: a+=i
    
    return a
    
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i

    return fact

"""
"""

#numeros = [1,2,3,4,5,6,7,8,9,10]
#print( test() )
#print('nueva rama')
#print( suma(numeros) )

print(factorial(5))


    