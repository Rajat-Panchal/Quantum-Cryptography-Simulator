import random

n = 20

# Alice generates random bits
alice_bits = [random.randint(0, 1) for _ in range(n)]

# Alice chooses random bases
alice_bases = [random.choice(['+', 'x']) for _ in range(n)]

# Bob chooses random bases
bob_bases = [random.choice(['+', 'x']) for _ in range(n)]

bob_results = []

for i in range(n):

    if alice_bases[i] == bob_bases[i]:
        bob_results.append(alice_bits[i])

    else:
        bob_results.append(random.randint(0, 1))

shared_key = []

for i in range(n):

    if alice_bases[i] == bob_bases[i]:
        shared_key.append(alice_bits[i])

print("Alice Bits:")
print(alice_bits)

print("\nAlice Bases:")
print(alice_bases)

print("\nBob Bases:")
print(bob_bases)

print("\nBob Results:")
print(bob_results)

print("\nShared Secret Key:")
print(shared_key)

print("\nKey Length:", len(shared_key))

efficiency = len(shared_key)/n

print("Protocol Efficiency:", round(efficiency*100,2), "%")
