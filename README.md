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

## 📁 Project Files (Permalinks)

These files are linked to a specific commit for reproducibility:

- [`Pauli_Twirling_General_Customized_TSP.ipynb`](https://github.com/pranjaldhole/QiskitHackathon25_SuperQops/blob/0bb366a84ad0f0dd8c73399ed379fa3b5b4038e9/notebooks/Pauli_Twirling_General_Customized_TSP.ipynb)  
  *(Location: `notebooks/Pauli_Twirling_General_Customized_TSP.ipynb`)*

- [`layout_optimization_with_MST_approximation_schema.ipynb`](https://github.com/pranjaldhole/QiskitHackathon25_SuperQops/blob/0bb366a84ad0f0dd8c73399ed379fa3b5b4038e9/layout_optimization_with_MST_approximation_schema.ipynb)  
  *(Location: `layout_optimization_with_MST_approximation_schema.ipynb`)*
  
### Use case
- **Full Adder Gate**: [FullAdder](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.FullAdderGate)

- **Use case**: QuBO formulation with VQE solver for Travelling Salesperson Problem.

### Optimization steps

- **Circuit optimization using approximation schema**
  - Initialize the `isa_circuit` with `TrivialLayout` (level 0 optimization).
  - Apply the MST approximation schema to find a minimal-spanning-tree with Christofides algorithm that has optimization guarrantees.
- **Error Suppression on noisy qubits**
  - We use `PauliTwirling` for suppressing the noise on most noisy qubits in the selected physical qubit mapping.

## Notes

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
