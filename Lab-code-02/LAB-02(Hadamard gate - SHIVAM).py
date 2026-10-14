from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


qc=QuantumCircuit(1,1)
qc.h(0)
qc.measure(0,0)
sim=AerSimulator()
job=sim.run(qc, shots=1024)#circuit koe simulator mein bhejta hai aur usse 1024 times run krwa ke uska object return krta hai
result=job.result()#result function uss job object se result nikalta hai yani bit string result
counts=result.get_counts()
print(qc)
print(counts)