'''

Constate = 'Variaveis' que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)

'''

velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distancia onde o radar pega

posicao_radar = (LOCAL_1 - RADAR_RANGE)

vel_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= posicao_radar
posicao_carro = local_carro <= (local_carro + RADAR_RANGE)

if vel_carro_passou_radar_1:
    print('Velocidade do carro passou do radar')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_passou_radar_1 and posicao_carro:
    print('Carro multado em radar 1')