The exercise page: https://cryptohack.org/challenges/ecc/#

# Question

E:Y2 = X3 + 497X + 1768 mod9739

Using the above curve, and the points P=(493,5564), Q=(1539,4742), R=(4403,5202), find the point S(x,y)= P + P + Q + R by implementing the above algorithm.

After calculating S, substitute the coordinates into the curve. Assert that the point S is in E(Fp).

# Answer

In this example we will learn how the addition is made from mathematical pov and then we will write it's code (for you to understand the code you should atleast understand the math from high-level pov)

actually this can be solved in several orders but for our case I chose this order to cover the doubling of points case.

so know we will divide the problem and then construct it which mean:

u = P + P

v = Q + R

then S = u + v

## first Q + R: 

To get Q + R = (x3, y3)

we need to fisrt get the slope:

m = (y2 - y1) / (x2 - x1)

which will result in m = 115 * (716^-1) mod(9739) = 4448

Then:

x3 = ( m^2 - x1 - x2) modp

y3 = (m (x1 - x3) - y1) modp

so: Q + R = (8592, 2572) 

## Second P + P:

the same thing will happen here but the way we calculate the slope will differ 

m = ( (3 * x1^2 + a) / 2 * y1)

## Third u + v:

we will do the same thing we made in the first step

