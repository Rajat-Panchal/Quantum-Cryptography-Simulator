import random

n = 20

# Alice
alice_bits = [random.randint(0,1) for _ in range(n)]
alice_bases = [random.choice(['+','x']) for _ in range(n)]

# Eve
eve_bases = [random.choice(['+','x']) for _ in range(n)]
eve_results = []

for i in range(n):

    if eve_bases[i] == alice_bases[i]:
        eve_results.append(alice_bits[i])

    else:
        eve_results.append(random.randint(0,1))

# Bob
bob_bases = [random.choice(['+','x']) for _ in range(n)]
bob_results = []

for i in range(n):

    if bob_bases[i] == eve_bases[i]:
        bob_results.append(eve_results[i])

    else:
        bob_results.append(random.randint(0,1))

alice_key = []
bob_key = []

for i in range(n):

    if alice_bases[i] == bob_bases[i]:

        alice_key.append(alice_bits[i])
        bob_key.append(bob_results[i])

# QBER calculation
errors = 0

for a,b in zip(alice_key,bob_key):

    if a != b:
        errors += 1

if len(alice_key) > 0:
    qber = errors/len(alice_key)
else:
    qber = 0

print("Alice Key:", alice_key)
print("Bob Key:  ", bob_key)

print("\nKey Length:", len(alice_key))
print("Errors:", errors)
print("QBER:", round(qber*100,2), "%")

if qber > 0.11:
    print("\n⚠️ EAVESDROPPER DETECTED")
else:
    print("\n✅ CHANNEL APPEARS SECURE")