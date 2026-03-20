
import random
import statistics

def fii(capital_inicial: float, aportes: float, prazo: int, rentabilidadeFII: float) -> tuple:
    rentabilidadeFII /= 100

    montante = capital_inicial * (1 + rentabilidadeFII) ** prazo + aportes * ((1 + rentabilidadeFII) ** prazo - 1) / rentabilidadeFII

    variacao = (random.random() * 0.06 - 0.03)
    
    valorFinal1 = montante * (1 + variacao)

    variacao = (random.random() * 0.06 - 0.03)
    
    valorFinal2 = montante * (1 + variacao)
    
    variacao = (random.random() * 0.06 - 0.03)
    
    valorFinal3 = montante * (1 + variacao)    
    
    variacao = (random.random() * 0.06 - 0.03)

    valorFinal4 = montante * (1 + variacao)    
    
    variacao = (random.random() * 0.06 - 0.03)

    valorFinal5 = montante * (1 + variacao)    

    return f'{statistics.mean([valorFinal1, valorFinal2, valorFinal3, valorFinal4, valorFinal5]):.2f}', f'{statistics.median([valorFinal1, valorFinal2, valorFinal3, valorFinal4, valorFinal5]):.2f}', f'{statistics.stdev([valorFinal1, valorFinal2, valorFinal3, valorFinal4, valorFinal5]):.2f}'
