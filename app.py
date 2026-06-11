import streamlit as st
import random

def run_bb84(n, eve_prob, noise_prob):

    alice_bits = [random.randint(0,1) for _ in range(n)]
    alice_bases = [random.choice(['+','x']) for _ in range(n)]

    bob_bases = [random.choice(['+','x']) for _ in range(n)]

    bob_results = []

    for i in range(n):

        transmitted_bit = alice_bits[i]
        transmitted_basis = alice_bases[i]

        # Eve attack
        if random.random() < eve_prob:

            eve_basis = random.choice(['+','x'])

            if eve_basis == transmitted_basis:
                transmitted_bit = transmitted_bit
            else:
                transmitted_bit = random.randint(0,1)

            transmitted_basis = eve_basis

        # Channel noise
        if random.random() < noise_prob:
            transmitted_bit = 1 - transmitted_bit

        # Bob measurement
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

    key_length = len(alice_key)

    if key_length == 0:
        return 0, 0

    errors = sum(
        a != b
        for a, b in zip(alice_key, bob_key)
    )

    qber = errors / key_length

    return qber, key_length

st.title("Quantum Cryptography Simulator")
st.markdown("""
This simulator demonstrates the BB84 Quantum Key Distribution protocol.

Features:
- Quantum key generation
- Eavesdropping detection
- Channel noise simulation
- QBER analysis
""")
st.info(
    "BB84 Security Threshold: QBER < 11%"
)

n = st.slider("Number of Qubits",10,1000,100)

eve_prob = st.slider("Eve Probability",0.0,1.0,0.3)

noise_prob = st.slider("Noise Probability",0.0,0.3,0.05)

tab1, tab2 = st.tabs(
    [
        "Simulator",
        "Theory",
    ]
)

with tab1:

    run = st.button("Run Simulation")

    if run:

        qber, key_length = run_bb84(
            n,
            eve_prob,
            noise_prob
        )

        st.subheader("Simulation Results")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "QBER",
                f"{qber*100:.2f}%"
            )

        with col2:
            st.metric(
                "Secret Key Length",
                key_length
            )

        if qber < 0.11:
            st.success("✅ Secure Channel")
        else:
            st.error("⚠️ Channel Compromised")

with tab2:

    st.header("BB84 Quantum Key Distribution")

    st.markdown("""
### Overview

BB84 is the first quantum key distribution protocol,
proposed by Charles Bennett and Gilles Brassard in 1984.

It enables two parties (Alice and Bob) to generate
a shared secret key while detecting the presence
of an eavesdropper (Eve).

### Protocol Steps

1. Alice generates random bits.
2. Alice chooses random bases (+ or ×).
3. Bob measures using random bases.
4. Matching bases form the secret key.
5. QBER is calculated to verify security.

### Quantum Bit Error Rate (QBER)

QBER = Errors / Key Length

### Security Threshold

QBER < 11% → Secure Channel

QBER > 11% → Possible Eavesdropping or Excessive Noise

### Why Quantum Cryptography?

Any attempt to measure a quantum state disturbs it,
allowing eavesdroppers to be detected.
""")


