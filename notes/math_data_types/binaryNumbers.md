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

## Counting base 2
The sequence of base 2 numbers corresponding to the natural numbers 0,1,2,3..... has an easy to understand pattern,
and can be used to count to 1023 on your two fingers, where up = 0 and down = 1!

Here are the binary representations of the first 16 natural numbers. Notice how this is similar to the way we
write the rows of a truth table!

We call the four bit sequences **nibbles** and eight bit sequences are called **bytes**
```
0000  0
0001  1
0010  2
0011  3
0100  4
0101  5
0110  6
0111  7
1000  8
1001  9
1010  10   A
1011  11   B
1100  12   C
1101  13   D
1110  14   E
1111  15   F
```

## Hexadecimal numbers
The last six nibbles are sometimes represented by the latters A,B,C,D,E,F
and this allows us to write binary numbers in **hexadecimal**, i.e. in base 16
where we group the bits in groups of four, and then replace them with their hexadecimal symbol,
e.g.

* CAFEBABE = 11001010111111101011101010111110

and this is the first four bytes of the code for a java program compiled to bytes.

## Unicode
Binary numbers are also used to represent characters.

[UNICODE](https://home.unicode.org/) uses 16 bits (2 bytes) to represent characters in all alphabets including math, music, and emojis.
For example, here are the [unicode charts](https://www.unicode.org/charts/)

[ASCII code](https://www.unicode.org/charts/PDF/U0000.pdf) uses 8 bits (1 byte) for each character in the Latin alphabet

## Novels
Since a text file is nothing more than a sequence of characters, we can see that a novel in any language can be viewed as a sequence of unicode characters, each of which is 16 bits long, so the entire novel is a very long bit string and which can be viewed as a very large integer! With this interpretation the set of every possible novel that could ever be written in any current language, can be viewed as a subset of the integers!

When you write a text file on the computer, it is typically stored using either ASCII or Unicode as a sequence of characters.

## Audio and Video
Binary encoding is also used for audio files and video files, but we won't get into that now. The point here is that every movie file (mp4 or mpeg or avi ...) is just a long sequence of bytes and so can be viewed as a very large integer! The same for audio files.

# Binary Representation of real numbers
Just as decimal numbers can be used to represent real numbers by using the tenths, hundredths, thousandths, etc. places.
we can do the same with binary numbers have the places to the right of the decimal point be negative powers of 2, so

* $5/8 = 1/2 + 1/8 = 0.101$
* $7/32 = 4/32 + 2/32 + 1/32 = 1/8 + 1/16 + 1/32 = 0.00111$

Repeating binary numbers correspond to fractions, e.g.
* $1/3 = 0.01010101\overline{01}\ldots$

Irrational numbers correspond to non-repeating binary numbers, e.g.

* $\sqrt{2} = 1.01101010000010011110...$
* $\pi = 11.00100 10000 11111 10110 10101 00010 00100 00101 10100 01100 00100 01101 00110 00100 11000 11001 10001 01000 10111 00000$

## Bit strings and reals
Let ${\cal B}^\omega$ be the set of infinite bit strings $(b_1,b_2,\ldots )$ where each $b_i \in\\{0,1\\}$,
and let $[0,1] = \\{x\in\mathbb{R}: 0\le x \le 1\\}$,
then there is a surjection

$f:B \twoheadrightarrow [0,1]\subseteq\mathbb{R}$

which sends

$(b_1,b_2,b_3, \ldots) \ \mapsto\  b_1/2  + b_2/4 + b_3/8 + ... + b_k/2^k + \ldots$

It is not 1-1 because for example
$0.1 = f((1,0,0,0,0,0,\ldots) = f((0,1,1,1,1,1,\ldots) = 0.0111\overline{1}$

just as 0.1 and $0.0999999\overline{9}\ldots$ represent the same real number 0.1


