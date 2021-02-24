def doc_import(filename: str):
    '''
    this function helps import the provide projecteuler text file,
    using os
    '''
    # check lib os imported
    if 'os' not in dir():
        import os
    # init
    FolderName = 'data'
    Folderpath = os.path.join(os.path.abspath(''), FolderName)
    # file path, check if the input is string
    try: 
        filepath = os.path.join(Folderpath, filename)
    except AttributeError:
        print('filename must be in string')
        pass
    # read the file, check if it exists
    try:
        with open(filepath, mode='r') as data:
            print('###file import done, use .split() or .replace() to extract numbers###')
            return data.read()
    except FileNotFoundError:
        print('file not found')
        pass

def factorial(n: int):
    '''
    my own version of factorial, just for fun
    '''
    # regulate input to int
    try:
        if type(n) is not int or n < 0:
            n = int(abs(n))
            print('ur n is either not an int or -ve, but i int() for u :D')
    except (TypeError, ValueError, NameError) as e:    # or just except:
        return print('ur input messed up')
    # recusion
    if n == 0:    # base case
        return 1
    else:
        return n * factorial(n-1)

def divisor_finder(n: int, self_include = True):
    '''
    this returns a list of divisors of n: int, 
    if self_include = True, includes n itself
    i tested it is faster to use just list rather than np.array, 
    but i think numpy is always faster, can someone test and tell me?
    from q12
    ''' 
    divisor = []
    if self_include:
        for i in range(1, int(n**0.5) + 1):
            if n/(i) == n//(i):    # check if int after division
                if i == n//(i):    # if n is square number, pair repeated
                    divisor.append(i)
                else:    # a pair of divisors
                    divisor.append(i)
                    divisor.append(n//(i))
    else: 
        divisor.append(1)
        for i in range(2, int(n**0.5) + 1):
            if n/(i) == n//(i):    # check if int after division
                if i == n//(i):    # if n is square number, pair repeated
                    divisor.append(i)
                else:    # a pair of divisors
                    divisor.append(i)
                    divisor.append(n//(i))
    # sort (optional)
    #divisor.sort()
    return divisor

def divisor_counter(n: int):
    '''
    this returns the number of divisors of int n,
    just count the length of the above divisor_finder function
    from q12
    '''
    return len(divisor_finder(n))

def collatz(n: int):
    '''
    to calculate the number of steps to get to one, 
    using recusion,
    from q14
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

def digit_sum(n: int):
    '''
    this function gives the digit sum of the given int,
    from q16
    '''
    # regulate input to int
    try:
        if type(n) is not int or n < 0:
            n = int(abs(n))
            print('ur n is either not an int or -ve, but i int() for u :D')
    except (TypeError, ValueError, NameError) as e:    # or just except:
        return print('ur input messed up')
    
    # using string method and list loopie
    n = str(n)
    return sum( int(i) for i in n )

def digit_factorial_sum(n: int):
    '''
    this function gives the digit factorial sum of the given int,
    from q74
    '''
    # regulate input to int
    try:
        if type(n) is not int or n < 0:
            n = int(abs(n))
            print('ur n is either not an int or -ve, but i int() for u :D')
    except (TypeError, ValueError, NameError) as e:    # or just except:
        return print('ur input messed up')
    
    # using string method and list loopie
    n = str(n)
    
    # map [0,1,2,...,9] to their factorial (save as a list)
    pre_factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    
    return sum( pre_factorial[int(i)] for i in n )

def Fibonacci(n: int, memo={}) -> int:
    '''
    from youtube.com/watch?v=oBt53YbR9Kk
    a recusive and DP way of doing Fibonacci
    using a dictionary to save the calculated results
    so no more repeated computations
    0: 1, 
    1: 1, 
    2: 1, 
    3: ...
    '''
    # check if the value is obtained before (in dict)
    if n in memo:
        return memo[n]
    else: # recusion and save
        memo[n] = Fibonacci(n-1, memo) + Fibonacci(n-2, memo)
    # base cases
    if n <= 2:
        return 1  

def Fibonacci(n: int):
    '''
    this function is to obtain n-th Fibonacci (F0 = 0, F1 = 1, F2 = 1), 
    for lower n, use lambda and Fibonacci formula (Binet`s formula), 
    phi = (1+5**0.5)/2;
    Fibonacci = lambda n: int((phi**n - (-phi)**(-n)) / 5**0.5)')
    if n > 4000, the formula causes overflow
    from q2
    '''
    # init
    f0, f1 = 0, 1
    # loop
    if n == 0:
        return f0
    for i in range(n):
        # next Fibonacci
        f2 = f0 + f1
        # construction for next Fibonacci
        f0, f1 = f1, f2
    
    return f2

def Fibonacci_DP_recusive(n: int, memo={}) -> int:
    '''
    from youtube.com/watch?v=oBt53YbR9Kk
    a recusive and DP way of doing Fibonacci
    using a dictionary to save the calculated results
    so no more repeated computations
    0: 1, 
    1: 1, 
    2: 1, 
    3: ...
    '''
    # base cases
    if n <= 2:
        return 1 
    # check if the value is obtained before (memo in DP)
    if n in memo:
        return memo[n]
    # recusion and save
    memo[n] = Fibonacci(n-1, memo) + Fibonacci(n-2, memo)
    return memo[n]

def gen_Fibonacci(n: int):
    '''
    this function return a generator of Fibonacci number
    '''
    # init, F0 = 0
    yield 0
    # for loop
    f0, f1 = 0, 1
    for i in range(n):
        # calculate fn
        f2 = f0 + f1
        # next
        f0, f1 = f1, f2
        # yield F(N+1)
        yield f2

def alphabet_score(word: str):
    '''
    just a alphabet to number conversion,
    from q22
    '''
    scorelist = ['A','B','C','D','E',\
                 'F','G','H','I','J',\
                 'K','L','M','N','O',\
                 'P','Q','R','S','T',\
                 'U','V','W','X','Y','Z']
    return sum( scorelist.index(i)+1 for i in word )

def gcd(a,b):
    a, b = min(a, b), max(a, b)
    while b%a != 0:
        a , b = b%a , a
    return a

def gcd_v2(a: int, b:int):
    # case with 0 
    if a == 0 or b == 0:
        return max(a, b)
    if a < b:
        a, b = b, a
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)
    
def totient(n: int):
    # need gcd function
    def gcd(a: int, b:int):
        # case with 0 
        if a == 0 or b == 0:
            return max(a, b)
        if a < b:
            a, b = b, a
        if a%b == 0:
            return b
        else:
            return gcd(b, a%b)
    # check gcd == 1 loop
    coprime_cnt = 0
    for i in range(n):
        if gcd(n, i) == 1:    # if coprime
            coprime_cnt += 1
    return coprime_cnt

def totient_v2(n: int):
    '''
    modify ver for q69
    '''
    # need gcd function
    def gcd(a: int, b:int):
        # case with 0 
        if a == 0 or b == 0:
            return max(a, b)
        if a < b:
            a, b = b, a
        if a%b == 0:
            return b
        else:
            return gcd(b, a%b)
    # check gcd == 1 loop
    coprime_cnt = 0
    # if even, check only odd numbers
    if n%2 == 0:
        for i in range(1, n, 2):
            if gcd(n, i) == 1:    # if coprime
                coprime_cnt += 1
        return coprime_cnt
    else:
        for i in range(n):
            if gcd(n, i) == 1:    # if coprime
                coprime_cnt += 1
        return coprime_cnt
    
def sudoku_solver():
    def number_possible(x: int, y: int, n: int):
        '''
        this function checks whether:
        - the number n can fit in the grid position(x,y)
        - there are 3 checks according to standard Sudoku (9x9) rules:
        1. horizontal (x)
        2. vertical (y)
        3. in fixed location 3x3 squares
        '''
        global grid    # so that the input Sudoku grid can to change both in/out of the function

        # horizontal check
        for j in range(9):
            if grid[x][j] == n:    # if no
                return False

        # vertical check
        for i in range(9):
            if grid[i][y] == n:    # if no
                return False

        # 3x3 check
        x_3x3 = (x//3) * 3    # this is to get which 3x3 square it is in
        y_3x3 = (y//3) * 3    # same
        for i_3x3 in range(3):
            for j_3x3 in range(3):
                if grid[x_3x3 + i_3x3][y_3x3 + j_3x3] == n:
                    return False    # if no

        # if all tests passed
        return True
    '''
    using recusion
    this returns None, so need a output capture function
    '''
    global grid    # so that the input Sudoku grid can to change both in/out of the function

    for i in range(9):    # horizontal position
        for j in range(9):    # vertical position
            if grid[i][j] == 0:    # if it is empty
                for n in range(1, 9+1):    # check n from 1 to 9
                    if number_possible(i,j,n):    # if can put n
                        grid[i][j] = n    # write it down first
                        
                        # recusion
                        sudoku_solver()
                        '''
                        recusion as calling this function (self) again:
                        if any possible n can be put it an empty,
                        write it down first,
                        by calling self again,
                        this will check the next position,
                        as the last empty was assigned some possibe n

                        '''
                        
                        # a 'ctrl + z'
                        grid[i][j] = 0
                        ''' 
                        if the last recusion (loop) was out, 
                        this means from where the last recusion was started, 
                        the guess was wrong, 
                        so that position has to be assigned back to 0,
                        indicating 'no solved yet'
                        '''

                # if end up here, it means a guess has been rejected, 
                # this return is to kinda like stopping the for loop returning anything in the middle,
                # unless the scan is finished
                return
    
    # if the loop can ever get to here, meaning that the scan is finished
    return print(grid)

def polynomial_product(coef1: list, coef2: list) -> list:
    '''
    this is to multiplying 2 polynomial and obtain the coefficients,
    list index is the power, list element corresponding to it is the coefficient
    '''
    new_coef_get = {}
    for power1, c1 in enumerate(coef1):
        for power2, c2 in enumerate(coef2):
            new_coef_get[power1+power2] = new_coef_get.get(power1+power2, 0) + c1*c2      
    # to list
    new_coef = []
    for power in new_coef_get:
        new_coef.append(new_coef_get[power])        
    return new_coef

def integer_partition(n: int) -> int:
    '''
    this is to do integer_partition, based on q31 and the youbube vid:
    https://www.youtube.com/watch?v=VLbePGBOVeg&ab_channel=Mathologer
    '''
    def polynomial_product(coef1: list, coef2: list) -> list:
        '''
        this is to multiplying 2 polynomial and obtain the coefficients,
        list index is the power, list element corresponding to it is the coefficient
        '''
        new_coef_get = {}
        for power1, c1 in enumerate(coef1):
            for power2, c2 in enumerate(coef2):
                new_coef_get[power1+power2] = new_coef_get.get(power1+power2, 0) + c1*c2      
        # to list
        new_coef = []
        for power in new_coef_get:
            new_coef.append(new_coef_get[power])        
        return new_coef

    # required list
    below_int = [j for j in range(1, n+1)]
    # store all required polynomial
    polynomial_set = dict()
    for i in below_int: 
        coef_poly = [1 if j%i == 0 else 0 for j in range(0, n+1)]
        polynomial_set[i] = polynomial_set.get(i, coef_poly)    
    # multiply polynomial
    new_polynomial = [1]
    for polynomial in polynomial_set:
        new_polynomial = polynomial_product(new_polynomial, polynomial_set[polynomial])   
    return new_polynomial[n]

def fraction_simplify(norminator: int, denominator: int): 
    '''
    simplify fraction
    '''
    # check input
    try: 
        top, bottom = int(norminator), int(denominator)
        # find gcd
        to_divide = gcd(top, bottom)
        # divide
        top, bottom = int(norminator)//to_divide, int(denominator)//to_divide
        # print
        print('%i/%i = %i/%i'%(int(norminator), int(denominator), top, bottom))
        pass
    except (ZeroDivisionError, NameError) as error:
        print('bruh check your input, only int input and no 0 in denominator!')
        pass

# for print() output capturing
'''
from: 
https://stackoverflow.com/questions/16571150/how-to-capture-stdout-output-from-a-python-function-call
'''
from io import StringIO 
import sys
class Capturing(list):
    '''
    usage:
    with Capturing() as output:
        method()

    'output is the Captured printed data in list'
    '''
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout
