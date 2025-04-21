''' RSA implementation in Python '''

from random import randint
import math

def gcd(a,b):
    ''' returns tuple (d,m,n)
        where gcd(a,b)=d and
        d = m*a+n*b
    '''
    if b==0:
        return (a,1,0)
    else:
        c = a%b
        (d,m1,n1) = gcd(b,c)
        # by induction we know that
        # m1*b + n1*c = d
        # and by definition of // and %
        # a = (a//b)*b+ c
        # so c = a - (a//b)*b
        # so m1*b + n1*a -n1*(a//b)*b = d
        # so m = n1 n=m1-n1*(a//b)
        return (d,n1,m1-n1*(a//b))

def power(x,n,m):
    ''' return x^n mod m
        We introduce a variable p, initially 1
        with the invariant on (p,x,n,m) that (p*x^n)%m is constant
        at the top of the loop. When n=0 we return p%m which
        is equal to (x^n)%m
    '''
    p = 1
    while n>0:
        # invariant on (p,x,n,m) is p* x^n mod m at top of the loop
        if n%2==0:
            #x^n= x^(2r)=(x^2)*r
            x = (x*x)%m
            n = n//2
        else:
            # p*x^n = 
            # p*x^(2r+1)=
            # (p*x)*(x^2)^r
            p = (p*x)%m
            x = (x*x)%m
            n = (n-1)//2
    
    return p

def prime_test(p,n):
    ''' return true p passes prime test n times '''
    for i in range(n):
        x = randint(2,p-1)
        if power(x,p-1,p)!=1:
            return False
    return True

def generate_prime(d):
    ''' return next probable prime with d digits '''
    n = randint(10**d,10**(d+1))
    while not prime_test(n,100):
        n=n+1
    return n

def generate_e(m):
    ''' returns e with m/2<e<3m/4 and
        gcd(e,m)=1
    '''
    e = randint(m//2,3*m//4)
    while gcd(e,m)[0]!=1:
        e=e+1
    return e


def generate_keypair(d):
    ''' generate public/private key pair
        (n,e,f,p,q,m)
        for primes p,q, with at least d digits
        '''
    p = generate_prime(d)
    q = generate_prime(d+1)
    n = p*q
    m = (p-1)*(q-1)
    e = generate_e(m)
    (_,f1,_) = gcd(e,m)
    f = f1 % m  # make f positive by adding a multiple of m
    return({'n':n,'e':e,'f':f,'p':p,'q':q,'m':m})

def encode(num,ppk):
    ''' encode as x|-> (x^e)%n '''
    return power(num,ppk['e'],ppk['n'])

def decode(num,ppk):
    ''' decode as x|-> (x^f)%n '''
    return power(num,ppk['f'],ppk['n'])


def encode_string(text, pkc):
    ''' encode the text with a public key cryptosystem '''
    nums = string_to_nums(text,n_to_bytes(pkc['n']))
    codes = [encode(num,pkc) for num in nums]
    return codes

def decode_nums(nums,pkc):
    ''' decode a list of numbers using a public key cryptosystem '''
    
    decodes = [decode(num,pkc) for num in nums]
    text = nums_to_string(decodes)
    return text

def n_to_bytes(n):
    ''' get upper bound on number of bytes
        that can always be converted to a number < n
    '''
    return round(math.log2(n)/16)-1

def string_to_nums(text,b):
    ''' convert a string of unicode characters to
        a lists of integers, by decomposing the string
        into substrings with at most b bytes, and then
        interpreting each of those substrings as a binary
        number with b*16 bits
    '''
    strings = decompose_string(text,b)
    numbers = convert_strings_to_numbers(strings)
    return numbers

def nums_to_string(nums):
    ''' convert a list of integers into a string
        by viewing it as a list of binary numbers
        and converting each two a unicode string
        then joining them together
        '''
    strings = nums_to_strings(nums)
    text = strings_to_string(strings)
    return text



def string_to_num(s):
    ''' convert a string s of unicode values to a number '''
    nums = [ord(c) for c in s]
    n = 0
    p = 256**2
    for i in range(len(nums)):
        n += nums[i]*p**i
    return n

def num_to_string(n):
    ''' convert a number to a string of unicode characters '''
    s=""
    p=256**2
    while n>0:
        s += chr(n%p)
        n = n//p
    return s


def decompose_string(text,bytes):
    ''' convert a string into a list of strings of length bytes or less'''
    words = []
    while len(text)>0:
        words.append(text[:bytes])
        text = text[bytes:]
    return words

def convert_strings_to_numbers(strings):
    ''' convert a list of unicode strings to a list of numbers '''
    numbers = [string_to_num(s) for s in strings]
    return numbers

    
def encode_numbers(nums,n,e):
    ''' encode a list of numbers 
        as x|-> (x^e)%n 
    '''
    code = [power(x,e,n) for x in nums]
    return code

def decode_numbers(nums,n,f):
    ''' decode a list of numbers 
        as x|-> (x^f)%n
    '''
    code = [power(x,f,n) for x in nums]
    return code

def nums_to_strings(code):
    ''' convert a list of numbers to a list of strings '''
    vals = [num_to_string(v) for v in code]
    return vals

def strings_to_string(vals):
    ''' convert a list of strings into a single string '''
    return "".join(vals)


def run_demo():
  kp = (generate_keypair(2))
  print('here is a keypair',kp)
  x=1111
  y = encode(x,kp)
  z = decode(y,kp)
  print('results of encoding and decoding',x,y,z)

def test_encoding():
    '''test encoding/decoding'''
    print("Demo of the RSA algorithm!")
    d = int(input("Enter number of digits for primes p, q: "))
    pkc = generate_keypair(d)
    print('The key pair (n,e,f) is =',pkc)
    text = input("Enter the plaintext to be encrypted: ")
    nums = encode_string(text,pkc)
    print('-'*20)
    print('The string has been encoded as follows:')
    for num in nums:
        print(num,end=' ')
    text2 = decode_nums(nums,pkc)
    print('-'*20)
    print('Decoding those numbers gives')
    print(text2)

test_encoding()
