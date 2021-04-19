def prime_ver1(m):

    # libs
    if 'np' not in dir():
        import numpy as np

    # init/setup
    n = np.arange(m) + 1

    # 1 dosen't count, so remove
    n = np.delete(n,0)

    checkpos = 0
    while n[checkpos] < np.sqrt(m):  
        # only difference, rather than checking every single number, 
        # check only upto sqrt of n
        check = n%(n[checkpos])

        # keep the checking number
        check[np.where(n==n[checkpos])[0]] = 1

        # delete where on the list is 0, as above the number which can be divided is set to be 0
        n = np.delete(n,np.where(check==0)[0])

        # go to the next number on the list
        checkpos += 1

    # int32 will show error and compute a worng answer, so change to int64
    n = np.array(n,dtype='int64')

    return n

def prime_ver2(m):

    # libs
    if 'np' not in dir():
        import numpy as np
    if 'math' not in dir():
        import math

    # init/setup
    n = np.arange(start=3, stop=m+1, step=2)

    pos = 0
    while n[pos] < math.sqrt(m):  
        
        # remainder indicate primes, if 0 -> not prime
        remainder = n%n[pos]
        
        # excluding itself, self % self = 0
        remainder[pos] = n[pos]
        
        # delete where remainder = 0, in n
        n = np.delete(n, np.where(remainder==0)[0])

        # check next
        pos += 1
    
    # remember the special prime 2
    n = np.append(2, n)

    # int64
    n = np.array(n, dtype='int64')
    
    return n

def prime_no_libs(m):
    
    n = range(3, m+1, 2)

    pos = 0
    while n[pos] < (m)**0.5:

        # this check is to find all elements divides n[pos], label as 0
        check = [i%n[pos] for i in n]
        # as the n[pos] divides itself so change it from 0 to something else
        check[ n.index(n[pos]) ] = n[pos]

        n = [p for p, i in zip(list(n), check) if i != 0]

        pos += 1

    n[:0] = [2]    # same as append() to the left, append() is a[len(a):] = [v]
    return n


def nthprime(nth: int): 
    n = 3
    prime_set = [2]
    while len(prime_set) < nth:
        if 0 not in set([n%i for i in prime_set]):
            prime_set.append(n)
        n += 2    
    return prime_set