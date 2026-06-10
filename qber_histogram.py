import random
import numpy as np
import matplotlib.pyplot as plt

n = 100
trials = 1000

qber_values = []

for _ in range(trials):

    alice_bits = [random.randint(0,1) for _ in range(n)]
    alice_bases = [random.choice(['+','x']) for _ in range(n)]

    bob_bases = [random.choice(['+','x']) for _ in range(n)]

    bob_results = []

    for i in range(n):

        # Eve attacks EVERY qubit
        eve_basis = random.choice(['+','x'])

        if eve_basis == alice_bases[i]:
            transmitted_bit = alice_bits[i]
        else:
            transmitted_bit = random.randint(0,1)

        transmitted_basis = eve_basis

        if bob_bases[i] == transmitted_basis:
            bob_results.append(transmitted_bit)
        else:
            bob_results.append(random.randint(0,1))

    alice_key = []
    bob_key = []

    for i in range(n):

        if alice_bases[i] == bob_bases[i]:

            alice_key.append(alice_bits[i])
            bob_key.append(bob_results[i])

    if len(alice_key) > 0:

        errors = sum(
            a != b
            for a, b in zip(alice_key, bob_key)
        )

        qber = errors / len(alice_key)

        qber_values.append(qber)

print("Mean QBER =", np.mean(qber_values))
print("Std Dev =", np.std(qber_values))

plt.figure(figsize=(8,6))

plt.hist(qber_values,bins=20)

plt.axvline(
    np.mean(qber_values),linestyle='--',label=f"Mean = {np.mean(qber_values):.3f}")

plt.xlabel("QBER")
plt.ylabel("Frequency")
plt.title("Distribution of QBER under Full Eavesdropping")
plt.legend()
plt.grid(True)

plt.show()