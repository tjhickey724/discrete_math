# Binary Numbers
We typically use base 10 representation of numbers for historical reasons, but in computer science it is often more useful
to represent numbers in base 2 or binary mode.

## Binary representation of integers
For integers, binary representation is analagous to decimal representation except that instead of the digits 0,1,2,3,4,5,6,7,8,9
we use only two bits 0,1  and instead of having the place values increase as powers of 10 (1's, 10's, 100's, 1000's). They increase
as powers of 2.

For example
* $1011 = 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 1 * 2^0 = 8+2+1 = 10$
* $10001000 = 1 * 2^7 + 1 * 2^3 = 128+8 = 136$

Converting from binary to decimal is easy, just add up the powers of two corresponding to each 1 in the number

Converting from decimal to binary is a little trickier. There are two common approaches:

### the top down method
find the highest power of two less than or equal to the number, that gives you the leftmost bit.
Subtract that power of two from the number and continue the process until you get to zero.
For example, let $n=99$.
Then the highest power of two less than or equal to $n$ is 64 = $2^6$, and 99-64-35
* $99 = 2^6 + 35$
* $35 = 2^5 + 3$
* $3 = 2^1+2^0$

So 99 has bits 0,1,5,6 equal to 1 and the others are zero.
* $99 = 1100011$

### the bottom up method
Another approach is to generate the binary number from the lowest bit up to the highest.
The lowest bit is 0 if the number is even and 1 if the number is odd.
To find the rest of the bits, divide by two and repeat the process.
For example
* $99$ is odd so the lowest bit is 1, subtracting 1 and dividing by two we get 49
* 49 is odd so the next lowest bit is 1, subtracting 1 and dividing by two we get 24
* 24 is even so the next bit is 0, and divide by 2 to get 12
* 12 is even, so the next bit is 0, divide by 2 to get 6
* 6 is even so the next bit is 0, divide by 2 to get 3
* 3 is odd so the next bit is 1, subtract 1 and divide by 2 to get 1
* 1 is odd so the last bit is 1
* so the binary representation of 99 is 1100011

## Binary Representation of real numbers
Just as decimal numbers can be used to represent real numbers by using the tenths, hundredths, thousandths, etc. places.
we can do the same with binary numbers have the places to the right of the decimal point be negative powers of 2, so

* $5/8 = 1/2 + 1/8 = 0.101$
* $7/32 = 4/32 + 2/32 + 1/32 = 1/8 + 1/16 + 1/32 = 0.00111$

Repeating binary numbers correspond to fractions, e.g.
* $1/3 = 0.01010101\overline{01}\ldots$

Irrational numbers correspond to non-repeating binary numbers, e.g.

* $\sqrt{2} = 1.01101010000010011110...$
* $\pi = 11.00100 10000 11111 10110 10101 00010 00100 00101 10100 01100 00100 01101 00110 00100 11000 11001 10001 01000 10111 00000$



