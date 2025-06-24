#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Utility functions to extract information about the backend.

Author: Pranjal Dhole
E-mail: dhole.pranjal@gmail.com
'''

import rustworkx as rx
import numpy as np

def get_qubit_noise_from_backend(backend):
    """
    Parameter: backend
    Returns: Noise_dict which is qubit-level noise dict[qubit_ID): Noise
    """
    backend_name = backend.name
    num_qubits = backend.num_qubits
    cmap = backend.coupling_map
    two_q_error_map = {}
    Noise_dict = {}
    single_gate_errors = [0] * num_qubits
    read_err = [0] * num_qubits
    cx_errors = []
    for gate, prop_dict in backend.target.items():
        if prop_dict is None or None in prop_dict:
            continue
        for qargs, inst_props in prop_dict.items():
            if inst_props is None:
                continue
            if gate == "measure":
                if inst_props.error is not None:
                    read_err[qargs[0]] = inst_props.error
                    Noise_dict[f"{qargs[0]}"] = inst_props.error
            elif len(qargs) == 1:
                if inst_props.error is not None:
                    single_gate_errors[qargs[0]] = max(
                        single_gate_errors[qargs[0]], inst_props.error
                    )
            elif len(qargs) == 2:
                if inst_props.error is not None:
                    two_q_error_map[qargs] = max(two_q_error_map.get(qargs, 0), inst_props.error)
    return Noise_dict, two_q_error_map

def get_coupling_map_from_backend(backend):
    graph = rx.PyDiGraph()
    backend.num_qubits
    graph.add_nodes_from(np.arange(0, backend.num_qubits, 1))
    two_qubit_gate='ecr'
    graph.add_edges_from(
        [
            (
                edge[0],
                edge[1],
                backend.properties().gate_error(gate=two_qubit_gate, qubits=(edge[0], edge[1]))
            )
            for edge in backend.coupling_map
        ]
    )

    return graph
