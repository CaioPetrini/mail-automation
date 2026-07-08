import json

def ler_arquivo_json():
    with open("config.json", "r", encoding="utf-8") as arquivo: # "r" = read
        dados = json.load(arquivo) # json.load retorna um dicionário
        return dados