# -*- coding: utf-8 -*-
"""
Project Euler Solutions
Account: DJBar

Created on Sat Oct 31 17:25:52 2015

@author: dominic


"""
###############################################################################
# Problem 1: Multiples of 3 and 5 #############################################
###############################################################################

def prblm_1():
    """If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9.  The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000"""
    #Use list comprehension
    return sum([x for x in range(0,1000) if x % 3==0 or x % 5==0])
    
    
###############################################################################
# Problem 2: Even Fibonacci numbers ###########################################
###############################################################################
# 1. Produce fibonacci numbers ################################################
# 2. Get the even ones ########################################################
# 3. Add them up ##############################################################
###############################################################################

def prblm_2():
    """find the sum of all the fibonacci sequence lower than 4000000"""
    fibseq = [1,1]
    sump = 0
    while fibseq[-1] < 4000000:
        fibseq.append(fibseq[-2] + fibseq[-1])
        if fibseq[-1] % 2 == 0:
            sump += fibseq[-1]
    return sump

###############################################################################
# Problem 3: Largest Prime Factor #############################################
###############################################################################
    
    
def lrgstprimefactors(number=600851475143,prime=[2]):
    """find the largest prime factors of 600851475143"""
    from math import sqrt
    counter = 3
    while counter < sqrt(number):
        if number != prime[-1]:
            i = 0
            j = 1
            if number % prime[-1] == 0:
                print 1
                number = number/prime[-1]
                lrgstprimefactors(number, prime)
            else:
                print 2
                while i < len(prime):
                    if int(prime[-1] + j) % prime[i] == 0:
                        j += 1
                        i = 0
                    else:
                        i += 1
                prime.append(prime[-1] + j)           
                lrgstprimefactors(number, prime)
    else:
        print prime
        return prime[-1]
        
###############################################################################
# Problem 4: Largest palindrome product #######################################
###############################################################################
        
def ispalindrome(number):
    """Check if number is a palindrome"""
    number = str(number)
    for ii in range(0,int(len(number)/2)):
        if number[ii] != number[-(ii + 1)]:
            return False
        else:
            pass
    return True        

def prblm_4(num1, num2, pali):
    """find the largest palindrome number which is the product of two three
    digit numbers"""

    
    while num1 > 100:

        multi = num1*num2
        
        if ispalindrome(multi):
            num2 -= 1
            num1 = 999
            if pali < multi:
                
                pali = multi
        else:
            num1 -= 1
    num2 -= 1
    num1 = 999
    
    if num2 < 100:
        print pali
    else:
        prblm_4(num1, num2, pali)


###############################################################################
# Problem 5: Smallest Multiple ################################################
###############################################################################

def prblm_5():
    """Find the smallest number which has all numbers from 1 to 20 as factors"""
    num = 20
    ii= 1
    while ii < 21:
        if num % ii == 0:
            ii += 1
        else:
            ii = 1
            num += 20
    return num
    
###############################################################################
# Problem 6: Sum square difference ############################################
###############################################################################
    
def prblm_6():
    """Find the difference between the sum of squares and square of sums
    of the numbers up to 100"""
    from numpy import array
    a = array(range(0,101))
    sumsqu = sum(a ** 2)
    squsum = sum(a) ** 2
    return squsum - sumsqu
    
###############################################################################
# Problem 7: 10001st prime ####################################################
###############################################################################
    
def prblm_7():
    """Find the 10001th prime number"""
    number = 11
    primes = [2,3,5,7,11]
    while len(primes) < 10002:
        ii = 0
        while ii < len(primes):
            if number % primes[ii] == 0:
                number += 2
                ii = 0
            else:
                ii += 1
        primes.append(number)
    return primes[10000]
    
###############################################################################
# Problem 8: Largest Product in series ########################################
###############################################################################
    
def prblm_8():
    """Find the largest product of 13 adjacent digits in the following series"""
    from scipy import product
    series = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450""".replace('\n','')
    serilist = [int(x) for x in series]
    heighestprod = 0
    for ii in range(0, len(serilist) - 13):
        if product(serilist[ii:ii + 13]) > heighestprod:
            heighestprod = product(serilist[ii:ii+13])
            heighestset = serilist[ii:ii+13]
    return heighestprod, heighestset
    
###############################################################################
# Problem 9: Special Pythagorean Triplet ######################################
###############################################################################
# Must fulfill conditions a<b<c a + b + c = 1000 ##############################
# Therefore: 998 > c > 334 ####################################################
############ 334 > b > 1 ######################################################
############ 333 > a > 0 ######################################################
###############################################################################

def prblm_9():
    from scipy import sqrt
    a = range(1,500)
    b = range(1,500)
    for ii in a:
        for jj in b:
            c = (ii**2) + (jj**2)
            if sqrt(c) % 1 == 0:
                #print str(ii) + ', ' + str(jj) + ', ' + str(sqrt(c))
                if ii + jj + sqrt(c) == 1000:
                    return ii*jj*sqrt(c)

###############################################################################
# Problem 10: Summation of primes #############################################
###############################################################################

def prblm_10():
    """Find the sum of prime numbers less than 2000000"""
    from numpy import array
    # Using elimination
    a = array(range(2,2000000))
    prime = 2
    sums = 0
    while prime < sqrt(2000000):
        sums += prime
        a = a[a % prime != 0]
        prime = a[0]
        sums += sum(a)
    return sums
    
    
    
    
    