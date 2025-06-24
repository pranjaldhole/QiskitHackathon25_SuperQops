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

## Benchmarking

- Noise estimation at qubit level
  - The noise profiles of the physical qubits on a device vary. Therefore, Qubit routing is not only an circuit optimization issue but also error propagation issue (higher connectivity of noisy qubits propagate more errors in the circuit).
- Circuit depth as a proxy
  - Optimization should also account for circuit depth. The longer the transpiled circuit, the more error will propagated through the circuit.
