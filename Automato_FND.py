#coding: utf-8

'''
    Author: Daniel D'Angelo de Oliveira
    Code: D61864-4
    Class: CC5P48
    Date: 05/11/2020

'''

import sys


# Classe Autômato
class Automato:


    # Método construtor
    def __init__(self, arquivo, qtdeEstados, estadoInicial, estadoFinal, alfabeto, dicionario):
        self.arquivo = arquivo
        self.qtdeEstados = qtdeEstados
        self.estadoInicial = estadoInicial
        self.estadoFinal = estadoFinal
        self.alfabeto = alfabeto
        self.dicionario = dicionario


    # Método que lê o arquivo e converte as cadeias presentes no mesmo em uma lista
    def leCaracteres(self):
        caracteres = []

        try:
            with open(self.arquivo) as file:
                for x in file:
                    letra = x.strip()
                    caracteres.append(letra)
                file.close()
        except IOError:
            sys.exit("\nArquivo '{}' inválido ou inexistente !".format(self.arquivo))

        return caracteres


    # Método que avalia se a cadeia é aceita ou não
    def avalia(self):
        caracteres = self.leCaracteres()
        print("\n\nResultados:")

        for x in range(len(caracteres)):
            estadoAtual = self.estadoInicial

            for y in range(len(caracteres[x])):
                estadoAtual = self.define(estadoAtual, caracteres[x][y])


            if (estadoAtual in self.estadoFinal):
                print("\nEstado Final: {} = Aceita".format(estadoAtual))
            else:
                print("\nEstado Final: {} = Rejeita".format(estadoAtual))


    # Método que define para qual estado o autômato deve ir, de acordo com o dicionário criado
    def define(self, estado, char):

        key = str(estado)+char

        if (key in self.dicionario.keys()):
            return self.dicionario.get(key)

        else:
            return(estado)



# Função main()
def main():


    # Bloco try-except, trata erros com relação a leitura de variáveis de tipo int
    try:

        print("\nBem vindo à Máquina de Estados AFD! Serão solicitados os parâmetros para a sua máquina como arquivo, "
              "número de estados, estado inicial, estado(s) final(s), alfabeto e transições.\n")


        # Definição do arquivo, número de estados, estado inicial
        arquivo = input("Digite o caminho (PATH) do arquivo a ser testado (utilize barras invertidas duplas): ")
        estados = int(input("\nDigite o número de estados deste Autômato Finito Determinístico: "))
        estadoInicial = int(input("\nDigite o estado inicial (q0) do autômato: "))

        if (estadoInicial >= estados):
            sys.exit("O estado inicial deve conter número menor do que a quantidade total de estados. Tente novamente.")


        # Definição do(s) estado(s) final(s), salvos em uma lista
        aux, estadoFinal = 0, []
        while (aux == 0):
            est = int(input("\nDigite um estado final para o autômato: "))

            if (est < estados):
                estadoFinal.append(est)
            else:
                sys.exit("O número de estado final é maior do que a quantidade de estados possíveis. Tente novamente.")

            aux = int(input("Deseja inserir mais um estado final no autômato ?\nSe sim digite 0 e, se não, digite 1: "))


        # Definição do alfabeto
        alf, alfabeto = 0, []
        while(alf == 0):

            letraAlfabeto = input("\nDigite um caracter correspondente ao alfabeto do autômato: ")
            alfabeto.append(letraAlfabeto)

            alf = int(input("Deseja inserir mais um caractere no alfabeto ?\nSe sim digite 0 e, se não, digite 1: "))


        # Definição do dicionário para armazenar as transições.
        # Exemplo: se o autômato está no estado 0, e ler a cadeia 'a', então o autômato irá para o estado 1.
        # Isto é, dicionario [0a] = 1.
        dicionario = {}
        for x in range(estados):

            print("\nO algoritmo está no estado {}.".format(x))

            for y in range(len(alfabeto)):
                acao = int(input("Se o autômato ler o símbolo '{}', deve passar para o estado: ".format(alfabeto[y])))

                if (acao < estados):

                    # Cria um dicionário com base no estado e símbolo correspondente, resultando em uma troca (ou não) de
                    # estados
                    dicionario[str(x)+alfabeto[y]] = acao

                else:
                    sys.exit("O número de estado de transição é maior do que a quantidade de estados possíveis. "
                             "Tente novamente.")


        # Criação do objeto e chamada do método que aciona a classe em si
        automato = Automato(arquivo, estados, estadoInicial, estadoFinal, alfabeto, dicionario)
        automato.avalia()


    # Se o algoritmo ler algum valor de tipo str onde era requerido um valor int, a exceção ValueError é levantada.
    except ValueError:
        print("\nValores inválidos! Tente novamente.")



if (__name__ == "__main__"):
    main()
