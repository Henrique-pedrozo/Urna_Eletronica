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