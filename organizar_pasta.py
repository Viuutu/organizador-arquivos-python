from datetime import datetime

# Dentro da função, ao mover o arquivo:
with open("historico.log", "a") as log:
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log.write(f"[{data_hora}] Movido: {arquivo} para {pasta}\n")
