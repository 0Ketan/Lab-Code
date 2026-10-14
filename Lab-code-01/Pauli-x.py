from qiskit import QuantumCircuit
qc = QuantumCircuit(1, 1)
qc.x(0)
qc.measure(0, 0)
print(qc.draw())