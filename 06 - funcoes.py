# 01) (Conversão de tempo) Faça uma função que receba 3 números inteiros como parâmetro, representando horas, minutos e segundos, e os converta em segundos. 
 
def convert_time(n1:int, n2:int, n3:int)->int:  
    n1 *= 3600 
 
    n2 *= 60 
 
    soma = n1 + n2 + n3 
 
    return soma 
 
# 02) (Conversão de temperatura) Faça uma função que receba uma temperatura em graus Celsius e retorne-a convertida em graus Fahrenheit. A fórmula de conversão é: F = C ∗ (9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius 
 
def convert_temp(C:float)->float: 
    F = C * (9.0/5.0) + 32.0 
 
    return F 
 
# 03) (Triângulos) Crie uma função que receba três valores (obrigatoriamente maiores que zero), representando as medidas dos três lados de um triângulo. Elabore funções para: 
# (a) Determinar se eles lados formam um triângulo, sabendo que: 
# - O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados. 
# (b) Determinar e mostrar o tipo de triângulo, caso as medidas formem um triângulo. Sendo que: 
# - Chama-se equilátero o triângulo que tem três lados iguais. 
# - Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais. 
# - Recebe o nome de escaleno o triângulo que tem os três lados diferentes. 
 
def triangulo(a:float, b:float, c:float)-> str: 
    if a < b + c and b < a + c and c < a + b: 
        if a == b == c: 
            return('É um triângulo equilátero') 
 
        else: 
            if a == b or a == c or b == c: 
                return('É um triângulo isósceles') 
             
            else: 
                return('É um triângulo escaleno') 
             
    else: 
        return('As medidas recebidas não formam um triângulo') 
 
# 04) (Classificação de seguro de veículo) Dado um veículo com idade, valor de mercado e tipo (passeio, carga, luxo), escreva uma função que devolva a classificação do risco: 
# Regras: 
# Se o valor for > 100.000 e tipo for "luxo", → Risco Alto 
# Se o veículo tiver mais de 15 anos → Risco Alto 
# Se o tipo for "carga" e valor > 80.000 → Risco Médio 
# Se tipo for "passeio" e valor < 50.000 → Risco Baixo 
# Caso contrário → Risco Moderado 
 
def carro(idade:int, valor:float, tipo:str)->str: 
    if (valor > 100000 and tipo == 'luxo') or idade > 15: 
        return 'Risco Alto' 
     
    else: 
        if tipo == 'carga' and valor > 80000: 
            return 'Risco Médio' 
         
        else: 
            if tipo == 'passeio' and valor < 50000: 
                return 'Risco Baixo' 
             
            else: 
                return 'Risco Moderado' 
             
# 05) (Sistema de prioridade de atendimento médico) Crie uma função que recebe idade, sintomas (“dor no peito”, “febre”, “tontura” ou “fraqueza”) e pressão arterial e devolve a prioridade do atendimento, conforme as regras a seguir: 
# Pressão ≥ 180 ou sintomas incluem “dor no peito” → Prioridade Máxima 
# Idade ≥ 65 e sintomas incluem “febre” → Alta Prioridade 
# Sintomas incluem “tontura” ou “fraqueza” → Prioridade Média 
# Caso contrário → Baixa Prioridade 
 
def atendimento_medico (idade:int, sintomas:str, pressao:int)->str: 
    if pressao >= 180 or sintomas == 'dor no peito': 
        return 'Prioridade Máxima' 
     
    else: 
        if idade >= 65 and sintomas == 'febre': 
            return 'Alta Prioridade' 
         
        else: 
            if sintomas == 'tontura' or sintomas == 'fraqueza': 
                return 'Prioridade Média' 
             
            else: 
                return 'Baixa Prioridade' 
             
# 06) (Análise do perfil do investidor) Crie uma função que receba idade, renda mensal e tolerância a risco ("alta", "média", "baixa") e retorne o perfil do investidor, segundo as regras: 
# Renda ≥ 10000 e tolerância = "alta" → Perfil Agressivo 
# Renda ≥ 5000 e tolerância = "média" → Perfil Moderado 
# Idade ≥ 60 e tolerância = "baixa" → Perfil Conservador 
# Renda < 2000 → Perfil Iniciante 
# Caso contrário → Perfil Neutro 
 
def investidor(idade:int, renda:float, risco:str)->str: 
    if renda >= 10000 and risco == 'alta': 
        return 'Perfil Agressivo' 
     
    else: 
        if renda >= 5000 and risco == 'média': 
            return 'Perfil Moderado' 
         
        else: 
            if idade >= 60 and risco == 'baixo': 
                return 'Perfil Concervador' 
             
            else: 
                if renda < 2000: 
                    return 'Perfil iniciante' 
                 
                else: 
                    return 'Perfil Neutro' 
                 
# 07) (Sistema de Classificação Climática) Crie uma função que receba temperatura (°C), umidade (%) e vento (km/h), e retorne a classificação do clima conforme as regras: 
# Temperatura > 35 e umidade < 30 → Alerta de Onda de Calor 
# Temperatura < 5 e vento > 30 → Alerta de Frio Intenso 
# Umidade > 90 → Alerta de Tempestade 
# Vento > 50 → Alerta de Ventania 
# Caso contrário → Clima Normal 
 
def clima(temperatura:float, umidade:float, vento:float)->float: 
    if temperatura > 35 and umidade < 30: 
        return 'Alerta de Onda de Calor' 
     
    else: 
        if temperatura < 5 and vento > 30: 
            return 'Alerta de Frio Intenso' 
 
        else: 
            if umidade > 90: 
                return 'Alerta de Tempestade' 
             
            else: 
                if vento > 50: 
                    return 'Alerta de Ventania' 
                 
                else: 
                    return 'Clima Normal'
                 
# 08) (Sistema de Diagnóstico Clínico) Crie uma função que receba: 
 
# Temperatura corporal (30 a 45) 
# Sintomas (“tosse seca”, “falta de ar”, “dor de cabeça”, “náusea”) 
# Histórico de doenças crônicas (sim ou não) 
# Idade 
 
# e devolva o diagnóstico conforme as regras (em ordem de prioridade): 
 
# Temperatura ≥ 39 e "tosse seca" e histórico → "Suspeita de COVID Grave" 
# "falta de ar" e temperatura ≥ 38 → "Emergência Respiratória" 
# Temperatura < 35 e idade > 65 → "Hipotermia com Risco" 
# "dor de cabeça" e "náusea" → "Suspeita de Enxaqueca" 
# Caso contrário → "Avaliação Padrão” 
 
def diagnostico (temperatura:float, sintoma:str, historico:bool, idade:int)->str: 
    if sintoma == 'tosse seca' and temperatura >= 39 and historico == True: 
        return 'Suspeita de COVID Grave' 
     
    else: 
        if sintoma == 'falta de ar' and temperatura >= 38: 
            return 'Emergência Respiratória' 
         
        else: 
            if temperatura < 35 and idade > 65: 
                return 'Hipotermia com Risco' 
             
            else: 
                if sintoma == 'dor de cabeça' or sintoma == 'náusea': 
                    return 'Suspeita de Enxaqueca' 
                 
                else: 
                    return 'Avaliação Padrão' 
 
# # 09) (Sistema de Análise de Perfil de Risco Financeiro) Crie uma função que receba:
# Score de crédito (0 a 1000)
# Dívida total
# Saldo em conta
# Renda mensal
# e retorne a classificação de risco segundo as regras, avaliadas em ordem de prioridade:
# Dívida > 2×renda e saldo < 100 → "Inadimplente Crítico"
# Score < 400 ou dívida > 1.5×renda → "Alto Risco"
# Score entre 400 e 700 e saldo < 500 → "Risco Médio"
# Score ≥ 700 e saldo > 1000 → "Risco Baixo"
# Caso contrário → "Risco Indefinido”

def risco_financeiro(score:int, divida:float, saldo:float, renda:float)->str:
    if divida > 2 * renda and saldo < 100: 
        return 'Inadimplente Crítico' 
     
    else: 
        if score < 400 or divida > 1.5 * renda: 
            return 'Alto Risco' 
         
        else: 
            if 400 <= score <= 700 and saldo < 500: 
                return 'Risco Médio' 
             
            else: 
                if score >= 700 and saldo > 1000: 
                    return 'Risco Baixo' 
                 
                else: 
                    return 'Risco Indefinido'
