from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()
print(qc.draw())

aer_sim = AerSimulator()
result = aer_sim.run(qc, shots=1000).result()
counts = result.get_counts(qc)
print(counts)
