import random
import numpy as np
import matplotlib.pyplot as plt

n = 100
trials = 500

eve_probs = np.arange(0, 1.1, 0.1)

avg_qbers = []

for eve_prob in eve_probs:

    qber_list = []

    for _ in range(trials):

        alice_bits = [random.randint(0,1) for _ in range(n)]
        alice_bases = [random.choice(['+','x']) for _ in range(n)]

        bob_bases = [random.choice(['+','x']) for _ in range(n)]

        bob_results = []

        for i in range(n):

            # Eve attacks with probability eve_prob
            if random.random() < eve_prob:

                eve_basis = random.choice(['+','x'])

                if eve_basis == alice_bases[i]:
                    transmitted_bit = alice_bits[i]
                else:
                    transmitted_bit = random.randint(0,1)

                transmitted_basis = eve_basis

            else:

                transmitted_bit = alice_bits[i]
                transmitted_basis = alice_bases[i]

            # Bob measures

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

            qber_list.append(qber)

    avg_qber = np.mean(qber_list)

    avg_qbers.append(avg_qber)

    print(
        f"Eve Probability = {eve_prob:.1f} | "
        f"Average QBER = {avg_qber:.4f}"
    )

plt.figure(figsize=(8,6))

plt.plot( eve_probs, avg_qbers,marker='o')

plt.xlabel("Eavesdropping Probability")
plt.ylabel("Average QBER")
plt.title("QBER vs Eavesdropping Probability (BB84)")
plt.grid(True)
plt.show()