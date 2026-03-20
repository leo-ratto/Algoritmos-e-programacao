def digitos_iguais(n):
    n = str(n)
    
    if len(n) == 1:
        return True
    
    if len(n) == 2:
        if n[0] == n[1]:
            return True
        
        else:
            return False
        
    if len(n) == 3:
        if n[0] == n[1] == n[2]:
            return True
        
        else:
            return False
        
    if len(n) == 4:
        if n[0] == n[1] == n[2] == n[3]:
            return True
        
        else:
            return False

def ordem_crescente(n):
    n = str(n)
    
    if int(n[0]) < int(n[1]) < int(n[2]):
        return True

    else:
        return False
    
def data_valida(data):
    data = str(data)
    
    dia = int(data[0] + data[1])
    mes = int(data[2] + data[3])
    ano = int(data[4] + data[5] + data[6] + data[7])
    
    if 0 < mes > 12:
        return False
    
    if ano <= 0:
        return False
    
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if 0 < dia <= 31:
            return True
        
        else:
            return False
        
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if 0 < dia <= 30:
            return True
        
        else:
            return False
        
    if mes == 2:
        if 0 < dia <= 28:
            return True
        
        else:
            return False
        
def digito_central(n):
    n = str(n)
    
    return n[len(n)//2]

def palindromo3(n):
    n = str(n)
    
    if n[0] == n[2]:
        return True
    
    else:
        return False
    
def binario_3bits(n):
    return int(bin(n)[2:])

def sinais_opostos(a, b):
    if (a < 0 and b >= 0) or (a >= 0 and b < 0):
        return True
    
    else:
        return False
    
