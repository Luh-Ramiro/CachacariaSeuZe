import requests
import json
from deep_translator import GoogleTranslator

def obter_conselhos(qtd):
    conselhos = []
    for _ in range(qtd):
        response = requests.get("https://api.adviceslip.com/advice")
        if response.status_code == 200:
            conselho = response.json()['slip']
            conselhos.append(conselho)
    return conselhos

def salvar_conselho(conselho):
    with open('conselhos.txt', 'a') as f:
        f.write(f"{conselho['id']}: {conselho['advice']}\n")

def mostrar_conselhos():
    try:
        with open('conselhos.txt', 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("Nenhum conselho salvo ainda.")

def traduzir_conselhos(conselhos):
    for conselho in conselhos:
        traducao = GoogleTranslator(source='en', target='pt').translate(conselho['advice'])
        print(f"Conselho: {conselho['advice']}\nTradução: {traducao}\n")

def main():
    while True:
        print("\nMenu:")
        print("1. Ouvir o Seu Zé")
        print("2. Mostrar Conselhos guardados")
        print("3. Traduzir para o 'Gringo'")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            qtd = int(input("Quantos conselhos você quer receber? "))
            conselhos = obter_conselhos(qtd)
            for conselho in conselhos:
                print(f"Conselho {conselho['id']}: {conselho['advice']}")
                salvar = input("Você deseja salvar este conselho? (s/n): ")
                if salvar.lower() == 's':
                    salvar_conselho(conselho)

        elif opcao == '2':
            mostrar_conselhos()

        elif opcao == '3':
            if 'conselhos' in locals():
                traduzir_conselhos(conselhos)
            else:
                print("Nenhum conselho disponível para tradução. Primeiro, obtenha conselhos.")

        elif opcao == '4':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()