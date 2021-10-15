import sys
from qat.core import Circuit

if len(sys.argv) < 2:
    print("Please provide a circuit file")
    sys.exit(0)

circuit_name = sys.argv[1]
circuit = Circuit.load(circuit_name)
for gate_name, gate_parameters, qbits in circuit.iterate_simple():
    print(gate_name, gate_parameters or "", qbits)
print(circuit.statistics())
