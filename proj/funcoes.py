import random
import time

class JogoFairytopia:
    def __init__(self):
        self.jogador = {
            jogador = {
            "vida_maxima": 20,
            "energia_max": 100,
            "bibble_limite": 2,
            "vida": 20,
            "energia": 100,
            "pontuacao": 10,
            "bibble": []
            }

        }

    def introducao(self):
        print("Em uma terra encantada chamada FAIRYTOPIA, existiam fadas que voavam sobre as flores!")
        print("Até que um dia, as flores murcharam, as fadas não voavam mais, a neblina veio à tona!")
        print("Era a Laverna (gritos) que estava amaldiçoando Fairytopia.")
        print("Laverna e os seus fungos soltaram um poluente que, ao atingir suas asas, as impossibilitavam de voar. Foi uma tragédia...")
        print("Mas você está aqui para nos ajudar!! Você é conhecida por Fada do Campo, a fada que nasceu sem asas, mas que tem um grande coração, e foi escolhida para DETER a Laverna e recuperar a magia e a paz de Fairytopia!!")

    def verificar_game_over(self):
        if self.jogador["vida"] <= 0 or self.jogador["energia"] <= 0:
            print("Você não resistiu... Laverna venceu. Fim de jogo.")
            exit()

    def verificar_vitoria(self):
        if self.jogador["pontuacao"] >= 100:
            print("Você rejeita a oferta de Laverna e arremessa o colar no ponto de união estraçalhando-o.")
            print("Os poderes dos guardiões são devolvidos, e Laverna desaparece.")
            print("De volta a Fairytopia, as flores e as fadas estão curadas. A rainha das fadas aparece.")
            print("Rainha: Obrigada, Fada do Campo, por salvar Fairytopia! Em recompensa ao seu ato de coragem, lhe dou esse colar mágico, que lhe dará asas e poderá voar!")
            exit()

    def mostrar_status(self):
        print("STATUS ATUAL:")
        print(f"Vida: {self.jogador['vida']}/{self.jogador['vida_maxima']}")
        print(f"Energia: {self.jogador['energia']}/{self.jogador['energia_max']}")
        print(f"Pontuação: {self.jogador['pontuacao']}\n")

    def primeira_escolha(self):
        print("Você está saindo de Fairytopia. Para onde deseja ir?\n")
        print("(1) Floresta Nebulosa")
        print("(2) Ir até Azura, a Guardiã das Fadas")
        print("(3) Enfrentar Laverna agora")

        while True:
            escolha = input("Digite o número da ação escolhida: ")

            if escolha == "1":
                print("Você se perdeu na Floresta Nebulosa.")
                self.jogador["pontuacao"] -= 10
                self.jogador["energia"] -= 15
                break

            elif escolha == "2":
                print("Ótima escolha! Você está a caminho de Azura.")
                self.jogador["pontuacao"] += 10
                self.jogador["energia"] -= 5
                self.jogador["vida"] = self.jogador["vida_maxima"]
                if len(self.jogador["bibble"]) < self.jogador["bibble_limite"]:
                    self.jogador["bibble"].append("Colar Mágico")
                else:
                    print("Bibble cheia! Não foi possível guardar o colar.")
                break

            elif escolha == "3":
                print("Você tentou enfrentar Laverna sem preparo... Foi derrotada.")
                self.jogador["vida"] = 0  
                break

            else:
                print("Opção inválida. Tente novamente.")
        self.verificar_game_over()
        self.verificar_vitoria()
