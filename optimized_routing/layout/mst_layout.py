#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Generates a minimal spanning tree for physical qubits on device from input quantum circuit.

Author: Pranjal Dhole
E-mail: dhole.pranjal@gmail.com
'''
import numpy as np
from qiskit.transpiler.layout import Layout

def generate_mst_layout(backend, qc):
    """
    Takes input quantum circuit and the backend to generate a layout
    for mapping virtual qubits to physical qubits on the backend device.
    """
    # Sequence of physical qubit IDs mapped in the device layout
    opt_layout = np.arange(0, qc.num_qubits, 1).tolist()        # FIXME This is a dummy mapping

    # The dictionary must be a bijective mapping between virtual qubits (tuple) and physical qubits (int).
    init_layout = Layout({q: phys for q, phys in zip(qc.qubits, opt_layout)})
    return init_layout

