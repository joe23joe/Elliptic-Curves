The exercise page: https://cryptohack.org/challenges/ecc/#

# Questions 

E: Y2 = X3 + 497X + 1768 mod 9739

Using the above curve, and the points P=(2339,2213), find the point Q(x,y) = [7863]P by implementing the above algorithm.

After calculating Q, substitute the coordinates into the curve. Assert that the point Q is in E(Fp).

# Answer

##### IMPORTANT : [7863]P does not mean 7863 multiply P, it means we add P to it self 7863 times

now lets get to how we are going to add P 7863 times to itself, before you panic offcourse we are not going to do it manually but we learn how the computer will make it.

#### what will happen:

convert 7863 to binary:

7863 = 1111010110111

1 (MSB) = 4096

1 = 2048

1 = 1024

1 = 512

0 = 256

1 = 128

0 = 64

1 = 32

1 = 16

0 = 8

1 = 4

1 = 2

1 (LSB) = 1

Then add all the 1 bits:

Q = 4096P + 2048P + 1024P + 512P + 128P + 32P + 16P + 4P + 2P + P

now we will need to double and add till reach the max requirment 

which means:

P + P = 2P 

2P + 2P = 4P 

4P + 4P = 8P 

.

.

.
