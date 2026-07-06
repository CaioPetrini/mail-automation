import json

def exibir_mensagem(mensagem):
        print(mensagem)
        
def obter_mensagem_boas_vindas():
    
    config = ler_arquivo_json()
    
    return f"""
====================================
{config["titulo"]}
====================================

{config["mensagem_boas_vindas"]}

Inicializando aplicação...
        
Aplicação iniciada com sucesso!
"""

def ler_arquivo_json():
    with open("config.json", "r", encoding="utf-8") as arquivo: # "r" = read
        dados = json.load(arquivo) # json.load retorna um dicionário
        return dados

def iniciar_aplicacao():
    
    mensagem = obter_mensagem_boas_vindas()
    exibir_mensagem(mensagem)
      
iniciar_aplicacao()