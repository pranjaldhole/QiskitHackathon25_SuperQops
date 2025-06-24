# Qiskit Hackathon 2025 

Qubit routing optimization task for World of Quantum Qiskit Hackathon 2025

## Team: SuperQops

**Members**

- Pranjal Dhole
- Hruday Divakaran
- Abhishek Racharla
- Xaiza Aniban

## Qubit routing optimization

Objective is to write a custom qubit routing algorithm that optimizes the transpiled circuit based on low depth as well as using less noisy qubits to avoid error propagation.

### Use case
- **Full Adder Gate**: [FullAdder](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.FullAdderGate)

- **Use case**: QuBO formulation with VQE solver for Travelling Salesperson Problem.

### Optimization steps

- **Circuit optimization using approximation schema**
  - Initialize the `isa_circuit` with `TrivialLayout` (level 0 optimization).
  - Apply an approximation schema to find a minimal-spanning-tree.
- **Error Suppression on noisy qubits**
  - We use `PauliTwirling` for suppressing the noise on most noisy qubits in the selected physical qubit mapping.

## Benchmarking

- Noise estimation at qubit level
  - The noise profiles of the physical qubits on a device vary. Therefore, Qubit routing is not only an circuit optimization issue but also error propagation issue (higher connectivity of noisy qubits propagate more errors in the circuit).
- Circuit depth as a proxy
  - Optimization should also account for circuit depth. The longer the transpiled circuit, the more error will propagated through the circuit.

## Installation

- Create virtual environment

```bash
mkdir .venv
```

```bash
uv venv .venv
```

- Activate the environment
```bash
source .venv/bin/activate
```

- Install package dependencies for the code base

```bash
uv pip install --upgrade pip setuptools
```

```bash
uv pip install -r requirements.txt
```

- Install the library in the developer version with following command

```bash
python setup.py develop
```
