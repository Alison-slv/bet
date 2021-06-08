#!/usr/bin/python
# -*- encode: utf-8 -*-
# autor: alison silva

from random import choice
import sys

class Times:
    """
    classe onde contera todos os times da
    competicao, onde voce podera apostar.
    e tambem as rodadas ja definidas de
    acordo com a quantidade de times.
    """
    def __init__(self):
        """
        metodo inicializador da classe Times
        """
        self.times = [
            'brazil', 'china', 'franca', 'italia', 'china', 'inglaterra', 'alemanha', 'argentina', 'belgica', 'croacia'
        ]
        self.rodadas = {
            "rodada_1": [self.times[0], self.times[9]],
            "rodada_2": [self.times[1], self.times[8]],
            "rodada_3": [self.times[2], self.times[7]],
            "rodada_4": [self.times[3], self.times[6]],
            "rodada_5": [self.times[4], self.times[5]],
        }

class Bet(Times):
    """
    classe principal do jogo, onde podera
    apostar, ver os resultados do jogo, 
    verificar o vencedor do jogo
    """
    def __init__(self):
        super().__init__()
        self._rodada_atual = 1
        self.jogo_atual = []
        self.resultado_jogo = []
        self._cont_result = 0
        self.apostas_feitas = []
        self._balanco = 0

    @property
    def balanco(self):
        return self._balanco

    @balanco.setter
    def balanco(self, valor):
        if valor >= 0:
            self._balanco = valor

        else:
            print("quantia negativa, seu saldo nao pode ser menor que zero")

    @property
    def rodada_atual(self):
        return self._rodada_atual

    @rodada_atual.setter
    def rodada_atual(self, valor_rodada):
        if valor_rodada > len(self.rodadas):
            self._rodada_atual = 1
        else:
            self._rodada_atual = valor_rodada
    
    def rodada(self):
        jogo = []
        for time in self.rodadas["rodada_"+str(self.rodada_atual)]:
        	print(time)
        	jogo.append(time)
        self.jogo_atual = jogo
        self.rodada_atual += 1
        self._cont_result = 1

    def resultado(self):
        _possiveis_gols = [0,1,4,2,3,0,2,1,0,4,5,1,6,3,3,0]
        if self._cont_result == 1:
            if len(self.resultado_jogo) > 0:
                self.resultado_jogo.clear()
            gols = lambda ps : choice(ps)
            for time in self.jogo_atual:
                gol = gols(_possiveis_gols)
                self.resultado_jogo.append([time, gol])
            self._cont_result = 0
        return self.resultado_jogo

    def time_vencedor(self):
        if self.resultado_jogo:
            casa = self.resultado_jogo[0][1]
            fora = self.resultado_jogo[1][1]
            if casa > fora:
                return self.resultado_jogo[0]
            elif casa < fora:
                return self.resultado_jogo[1]
            else:
                return False
        else:
            print("ainda nao saiu o resultado do jogo")

    def apostar(self, quantia, escolha):
        if self._cont_result == 1:
            if quantia > 0 and quantia <= self.balanco:
                if escolha == "casa":
                    print(f"voce apostou no {self.jogo_atual[0]}")
                    self.apostas_feitas.append([quantia, self.jogo_atual[0]])

                elif escolha == "fora":
                    print(f"voce apostou no {self.jogo_atual[1]}")
                    self.apostas_feitas.append([quantia, self.jogo_atual[1]])
                self.balanco -= quantia
            else:
                print("quantia negativa, ou maior que o disponivel")
        else:
            print("voce nao pode apostar, ate ter uma rodada atual")

    def verifica_apostas(self):
        valores = []
        for aposta in self.apostas_feitas:
            vencedor = self.time_vencedor()
            if vencedor == False:
                aposta[0] += self._balanco
            elif vencedor:
                if aposta[1] == vencedor[0]:
                    valores.append(aposta[0]+(aposta[0]/2))
            else:
                print("nao temos o vencedor ainda!")
        self.apostas_feitas.clear()
        self.balanco += int(sum(valores))

    def depositar(self,  quantia):
        if quantia >= 0:
            if quantia <= 500:
                self.balanco += quantia
            else:
                print("quantia minima para deposito é 500")
        else:
            print("quantia negativa")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("rode o arquivo 'main.py' para jogar")
        print("python aposta.py [opcao]")
        print("\n   versao - mostra a versao do CLI game")

    elif sys.argv[1] == "versao":
        print("versao: 0.15")