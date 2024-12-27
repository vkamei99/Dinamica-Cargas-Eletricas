import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

###########   Configurações Iniciais e Constantes   ##########

Eo = 8.854e-12 #Permissibilidade Elétrica

#P = {Carga, Posição, Massa}
Cargas = [
    {"q": 2e-6,  "massa": 1e-3, "pos": np.array([2.0, 3.0]), "vel": np.array([0.0, 0.0]), "f": np.array([0.0, 0.0])},
    {"q": -3e-6, "massa": 1e-3, "pos": np.array([5.0, 7.0]), "vel": np.array([0.0, 0.0]), "f": np.array([0.0, 0.0])},
    {"q": 4e-6,  "massa": 1e-3, "pos": np.array([9.0, 2.0]), "vel": np.array([0.0, 0.0]), "f": np.array([0.0, 0.0])}
]


#Variaveis para simulação
dt = 0.01

def calcula_forca(q1, q2, r1, r2):
    '''
    Essa função calcula a força sofrida na carga "1" pela "2" 
    '''
    r21 = r1 - r2
    R = np.linalg.norm(r21) 
    ar = r21 / R  # Vetor unitário
    forca = (1 / (4 * np.pi * Eo)) * (q1 * q2) / R**2 * ar
    return forca

def atualiza_forca():
    pass

def main():
    # Calcula a força resultante em cada uma das cargas
    for i,carga1 in enumerate(Cargas):
        for j,carga2 in enumerate(Cargas):
            if i != j:
                carga1["f"] += calcula_forca(carga1["q"], carga2["q"], carga1["pos"], carga2["pos"])

    print(Cargas[0]["f"], Cargas[1]["f"], Cargas[2]["f"])

    #plt.figure("Trabalho de Eletromag 1")
    #plt.xlim(0, 10)
    #plt.ylim(0, 10)
    #plt.show()

if __name__ == "__main__":
    main()