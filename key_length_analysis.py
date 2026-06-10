import random
import numpy as np
import matplotlib.pyplot as plt

qubit_counts = [50, 100, 200, 500, 1000, 2000]

trials = 500

avg_key_lengths = []

for n in qubit_counts:

    key_lengths = []

    for _ in range(trials):

        alice_bases = [
            random.choice(['+','x'])
            for _ in range(n)
        ]

        bob_bases = [
            random.choice(['+','x'])
            for _ in range(n)
        ]

        matches = 0

        for i in range(n):

            if alice_bases[i] == bob_bases[i]:
                matches += 1

        key_lengths.append(matches)

    avg_key_lengths.append(
        np.mean(key_lengths)
    )

    print(
        f"n = {n} | "
        f"Average Key Length = {np.mean(key_lengths):.2f}"
    )

plt.figure(figsize=(8,6))
plt.plot(qubit_counts,avg_key_lengths,marker='o')
plt.xlabel("Number of Transmitted Qubits")
plt.ylabel("Average Secret Key Length")
plt.title("Secret Key Length vs Number of Qubits")
plt.grid(True)
plt.show()