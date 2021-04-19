# q15 factorial and related functions
# q20, 34
def factorial(n: int) -> int:
    '''
    my own version of factorial, just for fun, dun go too big
    '''
    # regulate input to int
    try:
        n = int(n)
    except (TypeError, ValueError, NameError) as e:    # or just except:
        print('brah gimme int')
        pass
    # recusion
    if n == 0:    # base case
        return 1
    else:
        return n * factorial(n-1)

def nCr(n: int, r: int) -> int:
    '''
    or using lambda function \n
    nCr = lambda n, r: factorial(n)//(factorial(r)*factorial(n-r))
    '''
    return factorial(n) // (factorial(r) * factorial(n-r))

def nPr(n: int, r: int) -> int:
    '''
    nPr = n!*nCr (or generally, nCr = nPr/nPn) \n
    or using lambda function \n
    nPr = lambda n, r: factorial(n)//(factorial(n-r))
    '''
    return factorial(n) // factorial(n-r)

def nHr(n: int, r: int) -> int:
    '''
    nHr = (r+n-1)C(n-1) \n
    or using lambda function \n
    nCr = lambda n, r: factorial(n)//(factorial(r)*factorial(n-r)) \n
    from youtube.com/watch?v=C5TJwX9kflE (cantonese) \n
    or read https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics), https://faculty.math.illinois.edu/~jinto/combinations%20counting%20multiplicity.pdf
    '''
    return factorial(r+n-1) // (factorial(n-1) * factorial(r))