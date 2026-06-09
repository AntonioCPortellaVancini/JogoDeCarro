import os
import time
import json
from datetime import datetime

def verificar_conquistas(pontos, nome):
    metas = {
        5: "Piloto Iniciante",
        20: "Fuga Perfeita",
        30: "Rei da Estrada",
        40: "Lenda Intocavel"
    }
    
    titulo = metas.get(pontos, "")
    
    if titulo != "":
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        tempo_exato = time.time()
        
        nova_conquista = {
            "jogador": nome,
            "conquista": titulo,
            "data": data_atual,
            "timestamp": tempo_exato
        }
        
        lista_conquistas = []
        
        if os.path.exists("conquistas.json"):
            arquivo_leitura = open("conquistas.json", "r")
            try:
                lista_conquistas = json.load(arquivo_leitura)
            except:
                lista_conquistas = []
            arquivo_leitura.close()
            
        lista_conquistas.append(nova_conquista)
        
        arquivo_escrita = open("conquistas.json", "w")
        json.dump(lista_conquistas, arquivo_escrita, indent=4)
        arquivo_escrita.close()
        
        return titulo
        
    return ""