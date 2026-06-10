# Quantum Cryptography Simulator using BB84 Protocol

## Overview

This project implements the BB84 Quantum Key Distribution (QKD) protocol and provides an interactive simulator for studying secure quantum communication. The simulator demonstrates how two parties can establish a shared secret key while detecting the presence of an eavesdropper through Quantum Bit Error Rate (QBER) analysis.

The project includes protocol implementation, eavesdropping simulation, channel noise modeling, statistical analysis, and an interactive Streamlit dashboard.

---

## Features

* BB84 Quantum Key Distribution Protocol
* Eavesdropping (Intercept-Resend) Attack Simulation
* Quantum Bit Error Rate (QBER) Analysis
* Channel Noise Modeling
* Secret Key Generation and Efficiency Analysis
* Interactive Streamlit Dashboard
* Statistical Validation through Monte Carlo Simulations

---

## Project Structure

```text
Quantum-Cryptography-Simulator/

├── bb84.py
├── eve_attack.py
├── qber_analysis.py
├── qber_histogram.py
├── key_length_analysis.py
├── noise_analysis.py
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## The BB84 Protocol

1. Alice generates a random sequence of bits.
2. Alice encodes each bit using randomly selected bases (+ or ×).
3. Bob measures each qubit using randomly selected bases.
4. Alice and Bob publicly compare bases.
5. Bits corresponding to matching bases form the shared secret key.
6. QBER is calculated to verify channel security.

---

## Security Analysis

The simulator models an intercept-resend attack where an eavesdropper (Eve) measures transmitted qubits using randomly chosen bases.

Since quantum measurements disturb the quantum state, Eve's presence introduces errors that increase the Quantum Bit Error Rate (QBER).

### Security Criterion

* QBER < 11% → Secure Communication
* QBER > 11% → Potential Eavesdropping or Excessive Noise

---

## Results

### QBER vs Eavesdropping Probability

The simulation reproduces the theoretical BB84 result where the QBER approaches approximately 25% under a full intercept-resend attack.

### QBER Distribution

Monte Carlo simulations show a QBER distribution centered near the theoretical value of 25%.

### Key Length Analysis

The average secret key length scales approximately as N/2, where N is the number of transmitted qubits.

### Noise Analysis

Channel noise introduces errors that increase QBER approximately linearly with noise probability.

### Comparison Analysis

The effects of eavesdropping and channel noise are compared using QBER as a common security metric.

---

## Streamlit Dashboard

The project includes an interactive dashboard allowing users to:

* Select the number of transmitted qubits
* Configure eavesdropping probability
* Configure channel noise probability
* Generate secure keys
* Evaluate communication security using QBER

Run the dashboard using:

```bash
streamlit run app.py
```

---

## Technologies Used

* Python
* Streamlit
* NumPy
* Matplotlib

---

## Future Improvements

* Entanglement-Based QKD (E91 Protocol)
* Decoy-State BB84
* Quantum Error Correction
* Photon Loss Modeling
* Quantum Network Simulation

---

## References

* Bennett, C. H., & Brassard, G. (1984). Quantum Cryptography: Public Key Distribution and Coin Tossing.
* Nielsen, M. A., & Chuang, I. L. Quantum Computation and Quantum Information.
* IBM Quantum Learning Resources.

```
```
