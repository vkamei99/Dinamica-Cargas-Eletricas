import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

###########   Configurações Iniciais e Constantes   ##########

Eo = 8.854e-12 #Permissibilidade Elétrica

#P = {Carga, Posição, Massa}
Cargas = [
    {"q": 2e-6,    "massa": 1e-3,   "pos": np.array([3.0, 3.0]), "vel": np.array([0.0, 0.0]), "f": np.array([0.0, 0.0]), "trajetoria": [[], []]},
    {"q": -3e-6,   "massa": 1.5e-3, "pos": np.array([6.0, 7.0]), "vel": np.array([0.0, 0.0]), "f": np.array([0.0, 0.0]), "trajetoria": [[], []]},
    {"q": 1.5e-6,  "massa": 1.2e-3, "pos": np.array([8.0, 2.0]), "vel": np.array([0.0, 0.0]), "f": np.array([0.0, 0.0]), "trajetoria": [[], []]}
]

pontos = []
linhas = []

#Variaveis para simulação
dt = 0.01

def calcula_forca(q1, q2, r1, r2):
    '''
    Essa função calcula a força sofrida na carga "1" pela "2" 
    '''
    r21 = r1 - r2
    R = np.linalg.norm(r21) 
    if R < 0.1:
        R = 0.1
    ar = r21 / R  # Vetor unitário
    forca = (1 / (4 * np.pi * Eo)) * (q1 * q2) / R**2 * ar
    return forca

def atualiza_tudo(frame):
    '''
    Atualiza as posições das cargas
    '''
    # Zera a força antes do cálculo
    for carga in Cargas:
        carga["f"] = np.array([0.0, 0.0])

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
    
        # Atualiza a trajetoria
        carga["trajetoria"][0].append(carga["pos"][0])
        carga["trajetoria"][1].append(carga["pos"][1])

    # Atualiza os pontos no gráfico usando a função set_offsets
    for i,carga in enumerate(Cargas):
        pontos[i].set_offsets(carga["pos"])
        linhas[i].set_data(carga["trajetoria"][0], carga["trajetoria"][1])

    return pontos + linhas

def main():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    for carga in Cargas:
        linha, = ax.plot([], [], ls = '--')
        linhas.append(linha)

        ponto = ax.scatter(carga["pos"][0], carga["pos"][1], label=f"q = {carga['q']}C")
        pontos.append(ponto)
        
    animation = FuncAnimation(fig=fig, func=atualiza_tudo, frames=1000, interval=dt * 1000)
    
    #animation.save('Render.mp4')
    ax.legend()    
    plt.show()

if __name__ == "__main__":
    main()