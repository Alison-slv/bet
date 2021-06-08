#!/usr/bin/python3.8
# -*- encode: utf-8 -*-
# autor: alison slva

from aposta import Bet

apostador = Bet()

def menu():
    print("\n1 - rodada  2 - resultado")
    print("3 - apostar   4 - depositar")
    print("0 - sair")

def main():
    while True:
        menu()
        print(f"seu saldo {apostador.balanco}")
        escolha = int(input("escolha$ "))
        if escolha == 0:
            print("ate breve..")
            break

        elif escolha == 1:
            print(f"\nrodada {apostador._rodada_atual}")
            apostador.rodada()

        elif escolha == 2:
            resultado = apostador.resultado()
            print()
            for time in resultado:
                print(f"time {time[0]} gol {time[1]}")
            apostador.verifica_apostas()

        elif escolha == 3:
            valor = int(input("valor a apostar$ "))
            palpite = input("seu palpite[casa-fora]$ ")
            apostador.apostar(valor, palpite)

        elif escolha == 4:
            quantia = int(input("quantia a depositar$ "))
            apostador.depositar(quantia)

if __name__ == "__main__":
    main()