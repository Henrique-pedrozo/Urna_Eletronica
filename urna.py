import pickle

def carregar_candidatos(): 
    dic_candidatos = {}
    try: 
        with open("candidatos.txt", "r") as arq:
            for linha in arq:
                    linha_limpa = linha.strip()
                    if not linha_limpa:
                        continue
                    dados = linha.split(",")
                    nome = dados[0]
                    numero = dados[1]
                    partido = dados[2]
                    estado = dados[3]
                    cargo = dados[4]
                    
                    if cargo not in dic_candidatos:
                        dic_candidatos[cargo] = {}
                        
                    dic_candidatos[cargo][numero] = {
                    "nome": nome,
                    "partido": partido,
                    "estado": estado
                }
        print("Candidatos carregados com sucesso!")
        return dic_candidatos
    except: 
        print("Erro ao carregar o arquivo!")               
        return {}
    
def carregar_eleitores():
    dic_eleitores = {}
    try:
        # encoding='utf-8' é importante para ler acentos
        with open("eleitores.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                linha_limpa = linha.strip()
                if not linha_limpa:
                    continue
                
                dados = linha.split(",")
                
                # Previne erro se tiver alguma linha em branco ou incompleta no arquivo
                if len(dados) >= 5:
                    nome = dados[0].strip()
                    rg = dados[1].strip()
                    titulo = dados[2].strip()
                    municipio = dados[3].strip()
                    uf = dados[4].strip()
                    
                    # Aqui criamos a entrada no dicionário
                    dic_eleitores[titulo] = {
                        "nome": nome,
                        "rg": rg,
                        "municipio": municipio,
                        "uf": uf
                    }
        
        print("Eleitores carregados com sucesso!")
        return dic_eleitores
        
    except Exception as e:
        print(f"Erro ao carregar eleitores: {e}")
        return {}
        
print("1 - Ler arquivo de candidatos")
print("2 - Ler arquivo de eleitores")
print("3 - Iniciar votação")
print("4 - Apurar votos")
print("5 - Mostrar resultados")
print("6 - Fechar programa")
escolha = int(input("Escolha umas das opções: "))


if escolha == 1:
    candidatos = carregar_candidatos()
    print(candidatos)

elif escolha == 2:
    eleitores = carregar_eleitores()
    print(eleitores)    
            