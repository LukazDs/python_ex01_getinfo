import datetime 

def get_info():
    
    nome = input("Digite seu nome: ")
    sobrenome = input("\nDigite seu sobrenome: ")
    idade = int(input("\nDigite sua idade: "))
    altura_metros = float(input("\nDigite sua altura em metros (ex: 1.75): "))    

    return nome, sobrenome, idade, altura_metros

def get_idade_nascimento(idade):

    ano_atual = datetime.datetime.now().year
    ano_nascimento = ano_atual - idade  

    return  ano_nascimento


def verifica_maioridade(idade): 

    if idade >= 18:
        return True
    elif idade < 18:
        return False
    else:
        raise ValueError("Entrada inválida para maioridade. Use 's' para sim ou 'n' para não.")
    

def exibir_informacoes(nome, sobrenome, idade, ano_nascimento, maior_idade_bool, altura_metros):

    print("\n--- Informações do Usuário ---")
    print(f"\nNome Completo: {nome} {sobrenome}")
    print(f"Idade: {idade} anos")
    print(f"Ano de Nascimento: {ano_nascimento}")
    print(f"Maior de Idade: {'Sim' if maior_idade_bool else 'Não'}")
    print(f"Altura: {altura_metros:.2f} metros", end="\n")

def main():
    nome, sobrenome, idade, altura_metros = get_info()
    ano_nascimento = get_idade_nascimento(idade)
    maior_idade_bool = verifica_maioridade(idade)
    exibir_informacoes(nome, sobrenome, idade, ano_nascimento, maior_idade_bool, altura_metros) 

if __name__ == "__main__":
    main()  
