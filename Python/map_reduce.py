from functools import reduce
def normalize(name):
    return name.lower().capitalize()
    
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)    
    
def prod(L):
    def A_B(a,b):
        return a*b
    return reduce(A_B,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    
def str2float(s):
    s = s.split('.')
    def mul1(x, y):
        return x * 10 + y
    def mul2(x, y):
        return x / 10 + y
    return reduce(mul1, map(int, s[0])) + reduce(mul2, map(int, s[1][::-1])) / 10    