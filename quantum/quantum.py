from qiskit import *
from qiskit.visualization import array_to_latex
from math import pi

i = input("Qubit(s): ")

def oracle(inputOracle):  
    oracle = QuantumCircuit(len(inputOracle))
    x = []

    for it in range(len(inputOracle)):
        if (int(inputOracle[it]) == 0):
            x.append(abs(it - len(inputOracle) + 1))
            
    if len(x):
        oracle.x(x)
        
    oracle.mcrz(pi, list(range(len(inputOracle)))[:-1], len(inputOracle) - 1)
    
    if len(x):
        oracle.x(x)
        
    return oracle

hs = QuantumCircuit(len(i))
hs.h(list(range(len(i))))

ora = oracle(i)

grover = hs + ora

backend = Aer.get_backend('unitary_simulator')
job = execute(grover, backend)
result = job.result()
print(result.get_unitary(grover, decimals=3))

grover.measure_all()  
sim = Aer.get_backend('aer_simulator')
print(sim.run(grover).result().get_counts())

print(grover.draw())   
