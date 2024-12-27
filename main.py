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

def atualiza_tudo():
    # Calcula a força resultante em cada uma das cargas
    for carga1 in Cargas:
        for carga2 in Cargas:
            if carga1 != carga2:
                carga1["f"] += calcula_forca(carga1["q"], carga2["q"], carga1["pos"], carga2["pos"])

    #calcula a acelaração e a velocidade e atualiza a posição da particula
    for carga in Cargas:
        aceleracao = carga["f"]/carga["massa"]
        carga["vel"] += aceleracao * dt                  # v = vo + at
        carga["pos"] += carga["vel"] * dt                # s = so + vt
    
def main():
    plt.figure("Trabalho de Eletromag 1")
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    
    for carga in Cargas:
        x = plt.scatter(carga["pos"][0], carga["pos"][1])

    
    for i in range(100):
        atualiza_tudo()
        for i,carga in enumerate(Cargas):
            print(f"Posição da Carga {i} {carga['pos'][0]}, {carga['pos'][1]}")
        plt.pause(0.001)
        
    plt.show()

if __name__ == "__main__":
    main()