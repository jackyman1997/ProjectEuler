# q2 fibonacci 
# q25, 
def fibonacci(n: int) -> int:
    '''
    creats 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    checked upto n <= 2000, ok for n > 2000
    - DP using memoization (upto 2000, any above can cause kernel dying), 
    from youtube.com/watch?v=oBt53YbR9Kk
    def fibonacci(n: int, memo={}) -> int:
        # base cases
        if n == 0:
            return 0
        if 0 < n <= 2:
            return 1 
        # check if the value is obtained before (memo in DP)
        if n in memo:
            return memo[n]
        # recusion and save
        memo[n] = Fibonacci(n-1, memo) + Fibonacci(n-2, memo)
        return memo[n]
    - lambda with Binet`s formula, for n <= 71, else precision loss (over 1474 gives overflow):
    fibonacci = lambda n: int(((0.5*(1+5**0.5))**n - (-0.5*(1+5**0.5))**-n)/(5**0.5))
    - for other good Fibonacci program, 
    read https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
    '''
    # iterative
    f0, f1 = 0, 1
    # base cases
    if n < 0:
        return 'bruh, fibonacci(-n)?'
    elif 0 <= n <= 1:
        return n
    else:
        for i in range(2, n+1):
            f = f0 + f1
            f0 = f1
            f1 = f
        return f   
def xfibonacci(n: int) -> iter:
    '''
    generator form of fibonacci, upto nth fibonacci (inclusive)
    '''
    # no -ve input 
    if n < 0:
        return 'bruh, fibonacci(-n)?'
    else:
        # base cases
        f0, f1 = 0, 1
        yield f0
        yield f1        
        for i in range(2, n+1):
            f = f0 + f1
            f0 = f1
            f1 = f
            yield f
def Fibonacci() -> iter:    # imporved from q25
    '''
    endless generator form of fibonacci
    remember breaking condition
    '''
    # infinite generator:
    def xInf():
        while True:
            yield
    # base cases
    f0, f1 = 0, 1
    yield f0
    yield f1        
    for i in xInf():
        f = f0 + f1
        f0 = f1
        f1 = f
        yield f

# q3 Prime Factors
# q47
def PrimeFactors(n: int) -> dict:
    '''
    this returns {p1: a1, p2: a2, ...}
    as Fundamental theorem of arithmetic, 
    n = p1^a1 * p2^a2 * ...
    '''
    # storage
    compositon = {}
    # divide 2 first
    while n/2 == n//2:
        n = n//2
        compositon[2] = compositon.get(2, 0) + 1   
    # play the game of getting 1
    while n != 1:
        # check only odd numbers
        for odd in range(3, n+1, 2): 
            while n/odd == n//odd:
                n = n//odd
                compositon[odd] = compositon.get(odd, 0) + 1
            if n == 1:
                break      
    return compositon
def PrimeFactors_list(n: int) -> list:
    '''
    this returns [ [p1, 1], [p2, a2], ...]
    as Fundamental theorem of arithmetic, 
    n = p1^a1 * p2^a2 * ...
    '''
    # storage
    compositon = []
    # divide 2 first
    cnt = 0
    while n/2 == n//2:
        n = n//2
        cnt += 1
    if cnt > 0:
        compositon.append((2, cnt))
    # play the game of getting 1
    while n != 1:
        # check only odd numbers
        for odd in range(3, n+1, 2): 
            cnt = 0
            while n/odd == n//odd:
                n = n//odd
                cnt += 1
            if cnt > 0:
                compositon.append((odd, cnt))
            if n == 1:
                break 
    return compositon

# q12 divisors 
# q21, 23
def divisor(n: int, proper: bool=False, count: bool=False):
    '''
    using set, somehow list is a bit faster
    proper: proper divisors, not including n itself, default False (including n)
    count: return how many divisors instead of list of divisors, default False (return list)
    '''
    # set and setup
    d = set()
    d.add(1)    # 1 is divisor of all integers
    # proper divisor (not including n itself)
    if not proper:
        d.add(n)
    # loop
    for i in range(2, int(n**0.5)+1):
        if n/i == n//i:    # if n divides i (checking if int, or (n/i)%1 == 0)
            d.add(i)
            d.add(n//i)    # a pair of divisors, repeated if n is square
    # counting only
    if count:
        return len(d)
    else:
        return [i for i in d]    # or list(d)
def divisor_old( n: int, self_include: bool=True, sort: bool=False, count: bool=False):
    '''
    self_include: includes n itself (not proper divisors), default True (including n)
    sort: sort at the end, default False (not sort)
    count: return how many divisors instead of list of divisors, default False (return list)
    ''' 
    divisor = []
    if self_include:
        for i in range(1, int(n**0.5)+1):
            if n/(i) == n//(i):        # check if int after division
                if i == n//(i):        # if n is square number, pair repeated
                    divisor.append(i)
                else:                  # a pair of divisors
                    divisor.append(i)
                    divisor.append(n//(i))
    else: 
        divisor.append(1)
        for i in range(2, int(n**0.5)+1):
            if n/(i) == n//(i):        # check if int after division
                if i == n//(i):        # if n is square number, pair repeated
                    divisor.append(i)
                else:                  # a pair of divisors
                    divisor.append(i)
                    divisor.append(n//(i))
    # only counts
    if count:
        return len(divisor)
    # sort
    if sort:
        divisor.sort()
    return divisor

# q14 collatz
def collatz(n: int) -> int:
    '''
    to calculate the number of steps to get to one using recusion
    '''
    # set cnt
    cnt = 0
    # try recusion, so base case
    if n == 1:
        return cnt
    else:
        # if even n, cnt is 1 more than collatz(n/2)
        if n%2 == 0:
            cnt = collatz(n//2) + 1
            return cnt
        # if odd n, then even 3n+1, 2 more steps than collatz((3n+1)/2) 
        elif n%2 == 1:
            cnt = collatz((3*n+1)//2) + 2
            return cnt
        '''
        the reason of using // but not / is:
        i dun give fucks to floats, i want int
        if use /, the number becomes float (even i know they are defo int)
        for larger numbers, this will cause precision loss
        '''

# q15 factorial and related functions
# q20, 34
def factorial(n: int) -> int:
    '''
    my own version of factorial, just for fun
    '''
    # regulate input to int
    try:
        n = int(n)
    except (TypeError, ValueError, NameError) as e:    # or just except:
        pass
    # recusion
    if n == 0:    # base case
        return 1
    else:
        return n * factorial(n-1)
def nCr(n: int, r: int) -> int:
    '''
    or using lambda function
    nCr = lambda n, r: factorial(n)//(factorial(r)*factorial(n-r))
    '''
    return factorial(n)//(factorial(r)*factorial(n-r))
def nPr(n: int, r: int) -> int:
    '''
    nPr = n!*nCr (or generally, nCr = nPr/nPn)
    or using lambda function
    nPr = lambda n, r: factorial(n)//(factorial(n-r))
    '''
    return factorial(n)//(factorial(n-r))
def nHr(n: int, r: int) -> int:
    '''
    nHr = (r+n-1)C(n-1) \n
    or using lambda function
    nCr = lambda n, r: factorial(n)//(factorial(r)*factorial(n-r))
    from youtube.com/watch?v=C5TJwX9kflE (cantonese)
    or read https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics), https://faculty.math.illinois.edu/~jinto/combinations%20counting%20multiplicity.pdf
    '''
    return factorial(r+n-1)//(factorial(n-1)*factorial(r))

# q21 amicables numbers
def isAmicables(n: int) -> bool:
    a = sum(divisor(n, proper=True))
    b = sum(divisor(a, proper=True))
    return n == b

# q23 perfect, abundant, deficient numbers
def isPerfect(n: int) -> bool:
    '''
    Perfect number: sum of its proper divisors == itself
    '''
    return sum(divisor(n, proper=True)) == n
def isAbundant(n: int) -> bool:
    '''
    Abundant number: sum of its proper divisors > itself
    '''
    return sum(divisor(n, proper=True)) > n
def isDeficient(n: int) -> bool:
    '''
    Deficient number: sum of its proper divisors < itself
    '''
    return sum(divisor(n, proper=True)) < n

# q33 gcd and reduced fractions
def gcd_recu(a: int, b: int) -> int:
    '''
    recusion
    '''
    # base case with 0 
    if a == 0 or b == 0:
        return max(a, b)
    if a < b:
        a, b = b, a
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)   
def gcd(a: int, b: int) -> int:
    '''
    iterative
    '''
    a, b = min(a, b), max(a, b)
    while b%a != 0:
        a , b = b%a , a
    return a
def ReducedFraction(norminator: int, denominator: int) -> tuple:
    '''
    simplify fraction in the form of p/q
    '''
    try:
        p, q = int(norminator), int(denominator)
        common_divisor = gcd(p, q)
        p, q = p//common_divisor, q//common_divisor
        return (p, q)
    except (ZeroDivisionError, NameError) as error:
        print('bruh check your input, only int input and no 0 in denominator!')
        pass

# q35 digit rotation (permutation?)
def DigitRotation(n: int) -> iter:
    for i in str(n):
        n_rotation = ''.join( (str(n)[1:], str(n)[0]) )
        n = int(n_rotation)
        yield n

# q41 pandigital 
def isPandigital(n: int, excludeZero: bool=False) -> bool:
    if excludeZero:
        if set(str(n))&set('0') or len(str(n)) != len(set(str(n))):
            return False
        else:
            return True
    else:
        if len(str(n)) == len(set(str(n))):
            return True
        else:
            return False
def isPandigital_q41(n: int) -> bool:
    '''
    this is specific for q41, a slightly different version of Pandigital
    '''
    return set(str(n)) == set( str(i) for i in range(1, len(str(n))+1) )

# q42 triangle number
def triangle(n: int) -> int:
    return n*(n+1)//2
def isTriangular(n: int) -> bool:
    return (1+8*n)**0.5%1 == 0

# q44 pentagon number
def pentagon(n: int) -> int:
    return n*(3*n-1)//2
def isPentagonal(k: int, generalised: bool=False) -> bool:
    '''
    generalised: check if n is generalised pentagonal number (default False)
    '''
    delta = (1+24*k)**0.5
    if generalised:
        return delta%1 == 0
    else:
        if delta%1 == 0:
            return delta%6 == 5
        else:
            return False

# q55 palindromic, Lychrel numbers
def isPalindromic(n: int) -> bool:
    return int( str(n)[::-1] ) == n
def isLychrel(n: int, maxIter: int=50) -> bool:
    cnt = 0
    while cnt <= maxIter: 
        cnt += 1
        n += int( str(n)[::-1] )
        if isPalindromic(n):    
            # checking Palindromic has to be after 
            # since there are palindromic numbers that are themselves Lychrel numbers
            return False
    return True

# q32, q76 partition and coin change problem