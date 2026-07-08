from services.config_service import ler_arquivo_json

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

def iniciar_aplicacao():
    
    mensagem = obter_mensagem_boas_vindas()
    exibir_mensagem(mensagem)
      
iniciar_aplicacao()