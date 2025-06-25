import time
import matplotlib.pyplot as plt
from qiskit.transpiler import PassManager

def benchmark_pauli_twirling(qc, twirl_pass, seed_range=range(0, 101)):
    """
    Benchmarks the effect of a transpiler pass (e.g., PauliTwirl) on a given quantum circuit,
    by sweeping over different transpiler seeds and recording transpilation time and resulting circuit depth.

    Parameters:
    ----------
    qc : QuantumCircuit
        The input quantum circuit to be transpiled.

    twirl_pass : transpiler pass (e.g., PauliTwirl())
        The pass to apply using PassManager. Pass an *instance* (not class name).

    seed_range : iterable of int, optional (default: range(0, 101))
        Range of seed_transpiler values to sweep over.

    Returns:
    -------
    None
        The function directly plots the transpilation time and circuit depth as a function of seed.

    Example usage:
    --------------
    from qiskit import QuantumCircuit
    from qiskit.transpiler.passes import PauliTwirl

    # Create GHZ state
    qc_n_GHZ = QuantumCircuit(3)
    qc_n_GHZ.h(0)
    qc_n_GHZ.cx(0, 1)
    qc_n_GHZ.cx(1, 2)

    # Call the benchmark function
    benchmark_pauli_twirling(qc_n_GHZ, PauliTwirl(), seed_range=range(0, 50))

    Note: For options on twirl_pass, see Abhi's functions for Pauli's Twirld or Pranjal's custom PassManager
    """

    times = []
    depths = []

    for seed in seed_range:
        pm = PassManager([twirl_pass])  # Create new PassManager for each seed
        start = time.time()
        isa_qc = pm.run(qc)
        dt = time.time() - start
        times.append(dt)
        depths.append(isa_qc.depth())

    # Plotting
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(seed_range, times, marker='o', linestyle='-', color='blue')
    plt.title('Transpilation Time vs Seed')
    plt.xlabel('Seed')
    plt.ylabel('Time (sec.)')

    plt.subplot(1, 2, 2)
    plt.plot(seed_range, depths, marker='x', linestyle='-', color='green')
    plt.title('Circuit Depth vs Seed')
    plt.xlabel('Seed')
    plt.ylabel('Depth')

    plt.tight_layout()
    plt.show()
