The exercise page: https://cryptohack.org/challenges/ecc/#

# Question

E: Y2 = X3 + 497X + 1768 mod9739 , G:(1804,5368)

For these challenges, we have used a prime p≡3 mod 4, which will help you find y from y2.

Calculate the shared secret after Alice sends you x(QA) = 4726, with your secret integer nB = 6534.

Use the decrypt.py file to decode the flag

{'iv': 'cd9da9f1c60925922377ea952afc212c', 'encrypted_flag': 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'}

# Answer

So now alice and bob didn't want to share both x and y of there public keys to keep there data transfer as efficient as posible 

But now for bob to know the shared secret he needs to complete alice public key and then calculate the shared secret (S), where this is possible because if you have x adn the curve equation you can easily compute y(where y will have 2 equal values y and -y)

enough talking lets jump into the code.
