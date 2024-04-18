"""
    CONSTANTE - "Variáveis" que não vão mudar
    O python não proibe de incluir novos valores para constante, é
    apenas para sinalizar para outros devs que não se deve alterar o valor.
    Basta criar uma variável com letra maiúscula.
    
    Muitas condições no mesmo if(RUIM)
    <- Contagem de complexidade (RUIM)
"""

velocidade = 60  # velocidade atual do carro
local_carro = 99  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  #A distância onde o radar pega

range_superior_radar_1 = LOCAL_1 + RADAR_RANGE
range_inferior_radar_1 = LOCAL_1 - RADAR_RANGE

carro_acima_range_inferior = local_carro >= range_inferior_radar_1
carro_abaixo_range_superior = local_carro <= range_superior_radar_1

if velocidade > RADAR_1:
    if carro_acima_range_inferior and carro_abaixo_range_superior:
        print('Multa aplicada!!!')
    else:
        print('Caro fora do range do radar!')
else:
    print('Carro não foi multado, está dentro da variável permitida!')