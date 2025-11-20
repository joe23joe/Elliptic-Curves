The exercise page: https://cryptohack.org/challenges/ecc/#

# Question

E: Y2 = X3 + 497X + 1768 mod9739 , G:(1804,5368)

Calculate the shared secret after Alice sends you QA=(815,3190), with your secret integer nB=1829.

Generate a key by calculating the SHA1 hash of the x coordinate (take the integer representation of the coordinate and cast it to a string). The flag is the hexdigest you find.

# Answer

So know alice and bob want to create a key to encrypt and decrypt there messages. nA is alice secret and nB is bob's secret.

where QA and QB are alice and bob public keys where anyone can see but no one can ever now there secret because of the discrete logarithm problem

where QA = [nA]G

it's impossible to know nA if you have QA and G

#### That's enough let's get into the work

In our case there is a secret shared by alice and bob, where this secret can be know by using your secret in combine with his public key which means

S = [nA]QB = [nA]QA

S is the shared secret.

so now we want to calculate the shared secret and then hash this secrect (which is the x coordinate of the shared secret)
