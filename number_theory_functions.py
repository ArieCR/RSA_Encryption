from random import randrange
def gcd(a,b):
    """
    returns the gcd of a and b
    """
    if a==b:
        return a
    return gcd(b,a%b)

def extended_gcd2(a,b):
    """
    Returns the extended gcd of a and b

    Parameters
    ----------
    a : Input data.
    b : Input data.
    Returns
    -------
    (d, x, y): d = gcd(a,b) = a*x + b*y
    """
    def abs(x):
        if(x>0):
            return x
        return -x
    def max(c,d):
        if c>d:
            return c
        return d
    A = abs(a)
    B = abs(b)
    my_list = list()
    MAX = max(A,B)
    MIN = A+B-MAX
    while MIN != 0:
        arg1 = MAX
        arg2 = MAX//MIN
        arg3 = MIN
        arg4 = MAX%MIN
        my_list.append((arg1,arg2,arg3,arg4))
        MAX = MIN
        MIN = arg4
    my_list = my_list[:-1]
    pass     

def extended_gcd(a,b):
    """
    Returns the extended gcd of a and b

    Parameters
    ----------
    a : Input data.
    b : Input data.
    Returns
    -------
    (d, x, y): d = gcd(a,b) = a*x + b*y
    """
    if b==0:
        return (a,1,0)
    else:
        d,x,y = extended_gcd(b,a%b)
        x0 = y
        y0 = x-(a//b)*y
        return (d,x0,y0)
    
def modular_inverse(a,n):
    """
    Returns the inverse of a modulo n if one exists

    Parameters
    ----------
    a : Input data.
    n : Input data.

    Returns
    -------
    x: such that (a*x % n) == 1 and 0 <= x < n if one exists, else None
    """
    d,x,y = extended_gcd(a,n)
    while x<0:
        x = x+n
    if (d!=1):
        return None
    return x
    
def modular_exponent(a, d, n):
    """
    Returns a to the power of d modulo n

    Parameters
    ----------
    a : The exponential's base.
    d : The exponential's exponent.
    n : The exponential's modulus.

    Returns
    -------
    b: such that b == (a**d) % n
    """
    a = a%n
    res,a_pow2 = 1,a
    while d > 0:
        ind = d%2
        res = (res*(a_pow2**ind))%n
        return 0
        a_pow2 = (a_pow2**2)%n
        d = d//2
    return res

def miller_rabin(n):
    """
    Checks the primality of n using the Miller-Rabin test

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a 3/4 chance at least to be False
    """
    a = randrange(1,n)
    k = 0
    d = n-1
    while d % 2 == 0:
        k = k + 1
        d = d // 2
    x = modular_exponent(a, d, n)
    if x == 1 or x == n-1:
        return True
    for _ in range(k):
        x = (x * x) % n
        if x == 1:
            return False
        if x == n-1:
            return True
    return False

def is_prime(n):
    """
    Checks the primality of n

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a chance of less than 1e-10 to be True
    """
    for _ in range(10):
        if not miller_rabin(n):
            return False
    return True

def generate_prime(digits):
    for i in range(digits * 10):
        n = randrange(10**(digits-1), 10**digits)
        if is_prime(n):
            return n
    return None
