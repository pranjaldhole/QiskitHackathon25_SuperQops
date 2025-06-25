# Pauli Twirling Adventure

**Pauli twirling** is a quantum error mitigation technique designed to convert coherent errors—those with predictable, systematic behavior—into stochastic (random) errors that are easier to model and suppress. This is particularly useful for noisy intermediate-scale quantum (NISQ) devices, where two-qubit gates tend to introduce significant noise. The core idea of Pauli twirling is to surround a noisy two-qubit gate with carefully chosen single-qubit Pauli operations before and after, such that their net effect cancels out and the intended gate operation is preserved. While the functional behavior of the gate remains unchanged, the path through which noise propagates is randomized. This randomized noise has more favorable statistical properties, enabling better averaging across repeated circuit executions. As a result, Pauli twirling serves as a valuable tool for enhancing the reliability of quantum computations on real hardware.

A **normal Pauli twirling algorithm**, as implemented in the `PauliTwirl` transpiler pass, randomly inserts pairs of Pauli operations around each selected two-qubit gate (such as `CX` or `ECR`) in a quantum circuit. For each such gate, a pair of two-qubit Pauli gates is chosen so that the overall effect on the quantum state is equivalent to applying the original gate alone—this preserves the computation while randomizing the error channels. The algorithm constructs a small subcircuit (a "mini DAG") containing the left Pauli, the original two-qubit gate, and the right Pauli, then substitutes this for the original gate in the circuit's directed acyclic graph (DAG). Over multiple runs, this randomization helps transform coherent errors into stochastic ones, improving their suppressibility through averaging.

![image](https://github.com/user-attachments/assets/48ca9f86-50b5-46f9-8972-4f40650795ae)


```python
from graphviz import Digraph
from IPython.display import display
import IPython

# Create a flowchart with standard flowchart notation
dot = Digraph()
dot.attr(rankdir='TB', size='8')

# Flowchart shapes
dot.node('A', 'Start', shape='oval')
dot.node('B', 'Identify 2-qubit gates to twirl\n(e.g., CX, ECR)', shape='parallelogram')
dot.node('C', 'Loop over each such gate', shape='diamond')
dot.node('D', 'Randomly select Pauli pair\n(P_L, P_R) that preserves the gate', shape='rectangle')
dot.node('E', 'Create mini-DAG:\nP_L -> Gate -> P_R', shape='rectangle')
dot.node('F', 'Substitute gate in DAG with mini-DAG', shape='rectangle')
dot.node('G', 'More gates to twirl?', shape='diamond')
dot.node('H', 'Return modified DAGCircuit', shape='parallelogram')
dot.node('I', 'End', shape='oval')

# Define edges with control flow
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D', label='Yes')
dot.edge('D', 'E')
dot.edge('E', 'F')
dot.edge('F', 'G')
dot.edge('G', 'C', label='Yes')
dot.edge('G', 'H', label='No')
dot.edge('H', 'I')

# Display graph directly in the notebook
display(IPython.display.Image(dot.pipe(format='png')))

```

**Our Unique Approach:**

In quantum computing, not all qubits are equal—some are significantly noisier than others. At SuperQOps, we leverage this insight by taking a targeted approach rather than applying Pauli twirling uniformly across all two-qubit gates (like CX and ECR). Instead of blindly twirling every gate, we selectively apply twirling only to those acting on the noisiest qubits. This strategy reduces unnecessary overhead, lowering the overall circuit depth while still achieving effective—if not improved—error mitigation. The approach is outlined below:

```python
from graphviz import Digraph
from IPython.display import display
import IPython

# Create the flowchart for ConditionalPauliTwirlPass
dot = Digraph()
dot.attr(rankdir='TB', size='8')

# Define nodes with standard flowchart shapes
dot.node('A', 'Start', shape='oval')
dot.node('B', 'Initialize new DAG\nCopy qubit and classical registers', shape='rectangle')
dot.node('C', 'Loop over topological nodes', shape='diamond')
dot.node('D', 'Is gate a CX?', shape='diamond')
dot.node('E', 'Check if either qubit is in bad_qubits', shape='diamond')
dot.node('F', 'Insert random Pauli gates\nP1, P2 before CX', shape='rectangle')
dot.node('G', 'Apply CX gate', shape='rectangle')
dot.node('H', 'Insert inverse Pauli gates\nP1⁻¹, P2⁻¹ after CX', shape='rectangle')
dot.node('I', 'Apply CX gate as-is', shape='rectangle')
dot.node('J', 'Apply non-CX gate as-is', shape='rectangle')
dot.node('K', 'More nodes?', shape='diamond')
dot.node('L', 'Return new DAGCircuit', shape='parallelogram')
dot.node('M', 'End', shape='oval')

# Connect nodes
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E', label='Yes')
dot.edge('D', 'J', label='No')
dot.edge('E', 'F', label='Yes')
dot.edge('F', 'G')
dot.edge('G', 'H')
dot.edge('H', 'K')
dot.edge('E', 'I', label='No')
dot.edge('I', 'K')
dot.edge('J', 'K')
dot.edge('K', 'C', label='Yes')
dot.edge('K', 'L', label='No')
dot.edge('L', 'M')

# Display in notebook
display(IPython.display.Image(dot.pipe(format='png')))

```

**What We're Proud Of**

Using our Modified Pauli Twirling technique, we significantly reduced the number of operations in the circuit—from 2046 (with standard Pauli Twirling) to just 1263. This reduction in gate count is a meaningful step toward more efficient quantum circuits—something we're genuinely excited about!

**Next Steps**

Due to time constraints, we weren’t able to run full error rate benchmarks. However, we already have a function in place for this analysis. If you're as curious as we are, give it a try—we’re hopeful that the Modified Pauli Twirl will deliver comparable or even better error mitigation performance.
