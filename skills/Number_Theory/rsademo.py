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

pk0 = {'n': 20825675357, 
        'e': 12833058067, 
        'f': 9460924507, 
        'p': 53269, 
        'q': 390953, 
        'm': 20825231136}

pk1 =  {'n': 8421663493176891322498950739696866341843215824743352211189347130281236796544479527637108268074251754077347702437852550457794386160587462827198765742649519431193479094644776897904549487325973994253623497327082946357503974051084460848407191515644659018768655572816591846139144131401034779540155158763974571830287525364396812110773195723575620184812655521184350892148071769161744020245512191438054905429763, 
        'e': 5747520641800598648409191776976058522264347385498691507414228924645098265861741398301729730317770712454838462422586132261410512275360733830291604242732814164551816559817120518881310731868814888385458146627064473731851776644703903349583101603876044345391916936723418751921433314448823771748630358988927400061793417490612299450772953823508376516495467326722672523394126863998691904436301214573909476290097, 
        'f': 5063636910193747920834753527174890298184786427121288692885637179904401599773753112795433291368158245232874348918892929118881002736715996629998460631499414816732277633205170050549060708435498463632675451760741115591714241801893004828641905790171179520499268693317311178390751482542548342378916012222822204478734498855938647785385218542176844900054527922085378350762618375453361066281017476714733975057481, 
        'p': 968866072660804793746580830708899764307584308006841603047781438648087256770916901161247267281521168135126792563015003125972342641568492057356159397461800359108810699855302387515340938487704756299285949, 
        'q': 8692288574052766876262595485512173904135285774913515288643611660342539712806912795966348470995922198510694841710326640279063772449749606441446590274890876025489670735097186386384188517884564952895357887, 
        'm': 8421663493176891322498950739696866341843215824743352211189347130281236796544479527637108268074251754077347702437852550457794386160587462827198765742649519431193479094644776897904549487325973994253623487665928299643932304041908144627333523072774576098411763881423492855512174553571337651944416881320607926008653252022753407074658104405477121382062983168507966293666636816672970120716055819168345710785928}

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



def test_text_to_numbers():
    text = input("Enter the plaintext to be encrypted: ")
    bytes = int(input("Size of numbers"))
    nums = string_to_nums(text,bytes)
    print('converting',text,'to numbers gives')
    print(nums)

def encode_demo(pkc):
    public_key = {'n':pkc['n'],'e':pkc['e']}
    private_key = {'n':pkc['n'],'f':pkc['f']}
    print('The public key pair (n,e) is')
    print(public_key)
    text = input("Enter the plaintext to be encrypted: ")
    nums = encode_string(text,public_key)
    print('-'*20)
    print('The string has been encoded as follows:')
    for num in nums:
        print(num,end=' ')
    print()

def decode_demo(pkc):
    public_key = {'n':pkc['n'],'e':pkc['e']}
    private_key = {'n':pkc['n'],'f':pkc['f']}
    print('The key pair (n,e,f) is =',private_key)
    text = input("Enter the numbers to be encrypted: ")
    nums = [int(x) for x in text.split(' ')]
    print('the numbers to be decoded are:')
    print(text)
    text2 = decode_nums(nums,private_key)
    print('-'*20)
    print('Decoding those numbers gives')
    print(text2)  

# use keypair as a small public/private key pair
# use pk1 for a more realistic communication demo
#test_text_to_numbers()
encode_demo(pk0)
#decode_demo(pk0)
#test_encoding()


