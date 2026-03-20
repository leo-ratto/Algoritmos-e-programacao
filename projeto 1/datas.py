
from datetime import datetime, timedelta

def datas(meses: int) -> tuple:
    data_atual = datetime.now()
    data_resgate = data_atual + timedelta(days = meses * 30)
    return data_atual.strftime("%d/%m/%Y"), data_resgate.strftime("%d/%m/%Y")

