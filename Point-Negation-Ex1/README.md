The exercise page: https://cryptohack.org/challenges/ecc/#

# Question:

E: Y2 = X3 + 497X + 1768 mod9739

Using the above curve, and the point P(8045,6936), find the point Q(x,y) such that P + Q = O.

# Answer:

Acutally this question don't need to be coded it can be solved easily by math which we will do. 

I believe that you already know that any EC point added to it's inverse will generate the infinit point so:

since P + Q = O

and since P + (-P) = O

then Q = -P

where if P = (x,y) then -P = (x, -y)

then -P = (8045, -6936 mod(9739))

then -P = Q = (8045, 2803)


- if you didn't get where that "P = (x,y) then -P = (x, -y)" came from I suggest you to go back to https://rareskills.io/post/elliptic-curve-addition
