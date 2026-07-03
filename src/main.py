def exibir_mensagem(mensagem):
        print(mensagem)
        
def obter_mensagem_boas_vindas():
        return """
====================================
MAIL AUTOMATION
====================================

Bem-vindo ao Mail Automation!

Inicializando aplicação...
        
Aplicação iniciada com sucesso!
"""

def iniciar_aplicacao():
    
    mensagem = obter_mensagem_boas_vindas()
    exibir_mensagem(mensagem)
      
iniciar_aplicacao()