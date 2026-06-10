import random
import numpy as np
import matplotlib.pyplot as plt

n = 100
trials = 500

noise_levels = np.arange(0, 0.31, 0.03)

avg_qbers = []

for noise in noise_levels:

    qber_list = []

    for _ in range(trials):

        alice_bits = [random.randint(0,1) for _ in range(n)]
        alice_bases = [random.choice(['+','x']) for _ in range(n)]

        bob_bases = [random.choice(['+','x']) for _ in range(n)]

        bob_results = []

        for i in range(n):

            transmitted_bit = alice_bits[i]

            # Channel noise flips the bit
            if random.random() < noise:
                transmitted_bit = 1 - transmitted_bit

            if alice_bases[i] == bob_bases[i]:
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
                for a,b in zip(alice_key,bob_key)
            )

            qber_list.append(
                errors / len(alice_key)
            )

    avg_qber = np.mean(qber_list)

    avg_qbers.append(avg_qber)

    print(
        f"Noise = {noise:.2f} | "
        f"Average QBER = {avg_qber:.4f}"
    )

plt.figure(figsize=(8,6))
plt.plot(noise_levels,avg_qbers,marker='o')
plt.xlabel("Channel Noise Probability")
plt.ylabel("Average QBER")
plt.title("QBER vs Channel Noise")
plt.grid(True)
plt.show()