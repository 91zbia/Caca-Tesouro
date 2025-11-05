import random;
import time;


class Celula():
    x = 0
    y = 0
    def __init__(self,char : str):
        self.char = char
        pass

class Jogada():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        pass

class Tesouro():
    def __init__(self,char,x,y):
        self.char = char
        self.x = x
        self.y = y
        pass


matriz = []

linhas = 5
colunas = 5
Marcador_Tabuleiro = "  -  "
Marcador_Jogada = "  X  "

Tesouro_Jogador = Tesouro("  O  ",0,0)
Tentativa_Jogador = Jogada(-1,-1)

Tentativas = 7
Tentativa_Atual = 0


def CriarTabuleiro():
    Tesouro_Jogador.x = random.randint(0,linhas-1)
    Tesouro_Jogador.y = random.randint(0,colunas-1)
    
    for y in range(linhas):
        linha = []
        for x in range(colunas):
            cel = Celula(Marcador_Tabuleiro)
            cel.x = x
            cel.y = y
            linha.append(cel)
        matriz.append(linha)


def RenderTabuleiro():
    print("========================")
    for x, linha in enumerate(matriz):
        for y, Celula in enumerate(linha):
            if Tentativa_Jogador.y == Tesouro_Jogador.x and Tentativa_Jogador.x == Tesouro_Jogador.y:
                    print(f"{Tesouro_Jogador.char}",end="")
            else:
                print(f"{Celula.char}",end="")
        print(f"\n")
    print("========================")



def DarDica(ultima_linha: int, ultima_coluna : int):
    print("DICA!")
    
    if(ultima_linha > Tesouro_Jogador.y):
        print("o tesouro está um pouco mais acima!")
    
    if(ultima_linha < Tesouro_Jogador.y):
        print("o tesouro está um pouco mais abaixo!")
    
    if(ultima_coluna < Tesouro_Jogador.x):
        print("o tesouro está um pouco mais para a direita!\n")
    
    if(ultima_coluna > Tesouro_Jogador.x):
        print("o tesouro está um pouco mais para a esquerda!\n")
    
    
def Main():
    print("===============================\n")
    print("bem vindo(a) ao jogo de tesouro!\n")
    print("o seu objetivo é achar onde está o tesouro!")
    print("===============================\n")

    print("para poder jogar digite as posições que você acha que está o tesouro!\n");
    print("você possui tentativas!\n")
    print("inicio em 3s\n")
    time.sleep(3)

    CriarTabuleiro()
    RenderTabuleiro()

    Tentativa_Atual = 0

    while True:
        print(f"tentativa n°{Tentativa_Atual + 1}")
        try:
            Tentativa_Jogador.y = int(input("digite a linha [1-5]: ")) - 1
            if(Tentativa_Jogador.y > 4 or Tentativa_Jogador.y < 0):
                print("os valores deve estar dentro de [1-5]!")
                continue
            
            Tentativa_Jogador.x = int(input("digite a coluna [1-5]: ")) - 1
            
            if(Tentativa_Jogador.x > 4 or Tentativa_Jogador.x < 0):
                print("os valores devem estar dentro de [1-5]!")
                continue
            
            if(Tentativa_Atual < Tentativas-1):
                matriz[Tentativa_Jogador.y][Tentativa_Jogador.x].char = Marcador_Jogada
                Tentativa_Atual += 1
                if(Tentativa_Jogador.x == Tesouro_Jogador.x and Tentativa_Jogador.y == Tesouro_Jogador.y):
                    matriz[Tentativa_Jogador.y][Tentativa_Jogador.x].char = Tesouro_Jogador.char
                    RenderTabuleiro()
                    print("PARABENS! VOCÊ GANHOU\n")
                    print("fim de jogo!\n")
                
                    break
                else:
                    print(f"você não acertou!, restam {Tentativas - Tentativa_Atual} tentativas...\n")
                    DarDica(Tentativa_Jogador.y,Tentativa_Jogador.x)
            else:
                print("suas tentativas acabaram!\n")
                print("fim de jogo!\n")
              
                break
            RenderTabuleiro()
        except:
            print("as linhas e colunas só aceitam numeros inteiros!")
            continue
        pass

if __name__ == "__main__":
    Main()
