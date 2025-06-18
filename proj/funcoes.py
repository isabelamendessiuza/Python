import random
import time

class jogofairytopia:
    def __init__(self):
        self.jogador = {
            "vida": 100,
            "vida_maxima": 100,
            "energia": 100,
            "energia_max": 100,
            "pontuacao": 0,
            "bibble": [],
            "bibble_limite": 3
        }

        self.personagens = {
            "Fada do Campo": "Protagonista corajosa que nasceu sem asas, mas com um coração gigante.",
            "Laverna": "Vilã que lançou a névoa venenosa para paralisar as fadas e destruir Fairytopia.",
            "Azura": "Guardiã das Fadas, capturada pela Laverna.",
            "Dahlia": "Aliada que conhece o ponto fraco de Laverna.",
            "Nalu": "Amigo que oferece ajuda para respirar debaixo d’água."
        }

        self.itens = {
            "Colar Mágico": "Permite guardar energia e ajuda na missão.",
            "Alga Mágica": "Permite respirar debaixo d’água.",
            "Poção Curativa": "Recupera vida e energia.",
            "Anel de Invisibilidade": "Ajuda a se esconder dos inimigos."
        }

        self.locais = {
            "Fairytopia": "Terra encantada onde as fadas vivem em harmonia até a chegada da névoa.",
            "Floresta Nebulosa": "Local perigoso onde o jogador pode se perder.",
            "Caverna de Laverna": "Fortaleza da vilã onde acontece a batalha final.",
            "Casa de Azura": "Lugar seguro onde o jogador pode recuperar forças."
        }

        self.vestidos = ["Rosa", "Azul", "Violeta"]
        self.acoes_primeira_escolha = ["Floresta Nebulosa", "Ir até Azura", "Enfrentar Laverna"]
        self.itens_coletaveis = ["Colar Mágico", "Alga Mágica", "Poção Curativa"]

    def introducao(self):
        print("Em uma terra encantada chamada FAIRYTOPIA, existiam fadas que voavam sobre as flores!")
        time.sleep(3)
        print("Até que um dia, as flores murcharam, as fadas não voavam mais, a neblina veio à tona!")
        time.sleep(3)
        print("Era a Laverna (gritos) que estava amaldiçoando Fairytopia.")
        time.sleep(3)
        print("Laverna e os seus fungos soltaram um poluente que, ao atingirem suas asas, as impossibilitavam de voar. Foi uma tragédia...")
        time.sleep(3)
        print("Mas você está aqui para nos ajudar!! Você é conhecida por Fada do Campo, a fada que nasceu sem asas, mas que tem um grande coração, e foi escolhida para DETER a Laverna e recuperar a magia e a paz de Fairytopia!!")
        time.sleep(3)

    def evento(self): 
        vestido = random.choice(["Rosa", "Azul", "Violeta"])
        print(f"Você está linda hoje com seu vestido {vestido}")

    def verificar_game_over(self):
        if self.jogador["vida"] <= 0 or self.jogador["energia"] <= 0:
            print("Você não resistiu... Laverna venceu. Fim de jogo.")
            self.salvar_status()
            exit()

    def verificar_vitoria(self):
        if self.jogador["pontuacao"] >= 100:
            print("Você rejeita a oferta de Laverna e arremessa o colar no ponto de união estraçalhando-o.")
            print("Os poderes dos guardiões são devolvidos, e Laverna desaparece.")
            print("De volta a Fairytopia, as flores e as fadas estão curadas. A rainha das fadas aparece.")
            print("Rainha: Obrigada, Fada do Campo, por salvar Fairytopia! Em recompensa ao seu ato de coragem, lhe dou esse colar mágico, que lhe dará asas e poderá voar!")
            self.salvar_status()
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

    def segunda_escolha(self):
        print("Azura foi capturada. Você precisa tomar uma decisão!")
        print("(1) Ir até Dahlia")
        print("(2) Fugir por medo")
        print("(3) Jogar fora o colar")

        while True:
            escolha = input("Digite o número da sua escolha: ")

            if escolha == "1":
                print("Você parte em busca de Dahlia com coragem.")
                self.jogador["pontuacao"] += 15
                self.jogador["energia"] -= 10
                break
            elif escolha == "2":
                print("Você fugiu com medo. A missão falhou.")
                self.jogador["vida"] = 0
                break
            elif escolha == "3":
                print("Você jogou fora o colar... uma escolha arriscada.")
                if "Colar Mágico" in self.jogador["bibble"]:
                    self.jogador["bibble"].remove("Colar Mágico")
                self.jogador["energia"] -= 5
                self.jogador["pontuacao"] -= 5
                self.jogador["vida"] = 0
                break
            else:
                print("Opção inválida. Tente novamente.")
        self.verificar_game_over()
        self.verificar_vitoria()

    def terceira_escolha(self):
        print("Você está sobrevoando com Hue, mas é atacada por pássaros de fogo.")
        print("(1) Voltar para a casa")
        print("(2) Atacar")
        print("(3) Desviar e se esconder entre as árvores")

        while True:
            escolha = input("Digite o número da sua escolha: ")

            if escolha == "1":
                print("Você falhou com Fairytopia")
                self.jogador["pontuacao"] -= 10
                self.jogador["energia"] -= 10
                self.jogador["vida"] = 0
                break
            elif escolha == "2":
                print("Você não tem recursos para atacar.")
                self.jogador["vida"] = 0
                break
            elif escolha == "3":
                print("Você distraiu os pássaros de fogo!")
                self.jogador["energia"] -= 3
                self.jogador["pontuacao"] += 10
                break
            else:
                print("Opção inválida. Tente novamente.")
        self.verificar_game_over()
        self.verificar_vitoria()

    def quarta_escolha(self):
        print("Você encontra Nalu, que oferece uma alga para respirar debaixo d’água.")
        print("(1) Comer a alga")
        print("(2) Tentar sem alga")
        print("(3) Fazer submarino")

        while True:
            escolha = input("Digite o número da sua escolha: ")
            if escolha == "1":
                print("Você está nadando com Nalu em busca de Dahlia")
                self.jogador["pontuacao"] += 10
                self.jogador["energia"] -= 10
                break
            elif escolha == "2":
                print("Você não resistiu às profundezas")
                self.jogador["vida"] = 0
                break
            elif escolha == "3":
                print("Você demorou demais. Laverna venceu.")
                self.jogador["energia"] -= 10
                self.jogador["pontuacao"] -= 10
                self.jogador["vida"] = 0
                break
            else:
                print("Opção inválida. Tente novamente.")
        self.verificar_game_over()
        self.verificar_vitoria()

    def quinta_escolha(self):
        print("Dahlia te conta que o ponto fraco de Laverna está no ponto de união.")
        print("(1) Esperar 2 dias")
        print("(2) Ir direto enfrentar Laverna (+30 Corajosa)")
        print("(3) Nadar com Nalu")

        while True:
            escolha = input("Digite o número da sua escolha: ")
            if escolha == "1":
                print("Laverna derrotou Fairytopia")
                self.jogador["pontuacao"] -= 10
                self.jogador["energia"] -= 10
                self.jogador["vida"] = 0
                break
            elif escolha == "2":
                print("Você está indo até a caverna de Laverna para derrotá-la")
                self.jogador["pontuacao"] += 10
                self.jogador["energia"] -= 5
                break
            elif escolha == "3":
                print("Você se distraiu com o Nalu")
                self.jogador["energia"] -= 10
                self.jogador["pontuacao"] -= 10
                self.jogador["vida"] = 0
                break
            else:
                print("Opção inválida. Tente novamente.")
        self.verificar_game_over()
        self.verificar_vitoria()

    def sexta_escolha(self):
        print("Laverna tenta te seduzir com o desejo de asas.")
        print("Charada: O que é o ponto de união?")
        print("A) Um espelho mágico")
        print("B) Um colar com cristal encantado")
        print("C) Uma poção adormecida")
        print("D) Um anel de invisibilidade")

        while True:
            escolha = input("Digite a letra da sua escolha: ").upper()

            if escolha in ["A", "C", "D"]:
                print("Laverna derrotou Fairytopia")
                self.jogador["pontuacao"] -= 10
                self.jogador["energia"] -= 10
                self.jogador["vida"] = 0
                break
            elif escolha == "B":
                print("Você salvou Fairytopia! A rainha te presenteia com asas mágicas!")
                self.jogador["pontuacao"] += 10
                self.jogador["energia"] -= 5
                break
            else:
                print("Opção inválida")
        self.verificar_game_over()
        self.verificar_vitoria()

    def salvar_status(self):
        try:
            with open("status_final.txt", "w", encoding="utf-8") as file:
                file.write("=== STATUS FINAL DO JOGADOR ===\n")
                file.write(f"Vida: {self.jogador['vida']}/{self.jogador['vida_maxima']}\n")
                file.write(f"Energia: {self.jogador['energia']}/{self.jogador['energia_max']}\n")
                file.write(f"Pontos: {self.jogador['pontuacao']}\n")
                file.write(f"Biblle: {self.jogador['bibble']}\n")
            print("\nSeu status final foi salvo com sucesso no arquivo 'status_final.txt'.")
        except Exception as e:
            print(f"\nOcorreu um erro ao salvar o arquivo: {e}")
