import random
import time


jogador = {
    "vida_maxima": 20,
    "energia_max": 100,
    "bibble_limite": 2,
    "vida": 20,
    "energia": 100,
    "pontuacao": 10,
    "bibble": []
}

def introducao():
    print("Em uma terra encantada chamada FAIRYTOPIA, existiam fadas que voavam sobre as flores!")
    print("Até que um dia, as flores murcharam, as fadas não voavam mais, a neblina veio à tona!")
    print("Era a Laverna (gritos) que estava amaldiçoando Fairytopia.")
    print("Laverna e os seus fungos soltaram um poluente que, ao atingirem suas asas, as impossibilitavam de voar. Foi uma tragédia...")
    print("Mas você está aqui para nos ajudar!! Você é conhecida por Fada do Campo, a fada que nasceu sem asas, mas que tem um grande coração, e foi escolhida para DETER a Laverna e recuperar a magia e a paz de Fairytopia!!")

def verificar_game_over():
    if jogador["vida"] <= 0 or jogador["energia"] <= 0:
        print("Você não resistiu... Laverna venceu. Fim de jogo.")
        exit()

def verificar_vitoria():
    if jogador["pontuacao"] >= 100:
        print("Você rejeita a oferta de Laverna e arremessa o colar no ponto de união estraçalhando-o.")
        print("Os poderes dos guardiões são devolvidos, e Laverna desaparece.")
        print("De volta a Fairytopia, as flores e as fadas estão curadas. A rainha das fadas aparece.")
        print("Rainha: Obrigada, Fada do Campo, por salvar Fairytopia! Em recompensa ao seu ato de coragem, lhe dou esse colar mágico, que lhe dará asas e poderá voar!")
        exit()

def mostrar_status():
    print("STATUS ATUAL:")
    print(f"Vida: {jogador['vida']}/{jogador['vida_maxima']}")
    print(f"Energia: {jogador['energia']}/{jogador['energia_max']}")
    print(f"Pontuação: {jogador['pontuacao']}\n")

def primeira_escolha():
    print("Você está saindo de Fairytopia. Para onde deseja ir?\n")
    print("(1) Floresta Nebulosa")
    print("(2) Ir até Azura, a Guardiã das Fadas")
    print("(3) Enfrentar Laverna agora")

    while True:
        escolha = input("Digite o número da ação escolhida: ")

        if escolha == "1":
            print("Você se perdeu na Floresta Nebulosa.")
            jogador["pontuacao"] -= 10
            jogador["energia"] -= 15
            break

        elif escolha == "2":
            print("Ótima escolha! Você está a caminho de Azura.")
            jogador["pontuacao"] += 10
            jogador["energia"] -= 5
            jogador["vida"] = jogador["vida_maxima"]
            if len(jogador["bibble"]) < jogador["bibble_limite"]:
                jogador["bibble"].append("Colar Mágico")
            else:
                print("Bibble cheia! Não foi possível guardar o colar.")
            break

        elif escolha == "3":
            print("Você tentou enfrentar Laverna sem preparo... Foi derrotada.")
            jogador["vida"] = 0  
            break

        else:
            print("Opção inválida. Tente novamente.")
    verificar_game_over()
    verificar_vitoria()

def segunda_escolha():
    print("Olá, minha querida! Ah... toda a Fairytopia está em apuros por causa da Laverna. Pela manhã, irei partir em busca de Dahlia (uma ex-seguidora de Laverna).")
    print("Gostaria de pedir para que... fique com o meu colar mágico. Ele irá te proteger.")
    print("Azura foi... CAPTURADA POR UM FUNGO DE LAVERNA!!!!!")
    print("O que você vai fazer?")
    print("(1) Ir até Dahlia")
    print("(2) Fugir por medo")
    print("(3) Jogar fora o colar")

    while True:
        escolha = input("Digite o número da sua escolha: ")

        if escolha == "1":
            print("Você parte em busca de Dahlia com coragem.")
            jogador["pontuacao"] += 15
            jogador["energia"] -= 10
            break

        elif escolha == "2":
            print("Você fugiu com medo. A missão falhou.")
            jogador["vida"] = 0
            break

        elif escolha == "3":
            print("Você jogou fora o colar... uma escolha arriscada.")
            if "Colar Mágico" in jogador["bibble"]:
                jogador["bibble"].remove("Colar Mágico")
            jogador["energia"] -= 5
            jogador["pontuacao"] -= 5
            jogador["vida"] = 0
            break

        else:
            print("Opção inválida. Tente novamente.")
    verificar_game_over()
    verificar_vitoria()

def terceira_escolha():
    print("estrangeiros: “ VC MATOU A AZURA, COMO PODE” ")
    print("Hue (a borboleta gigante) : VAMOS FADA, VAMOS ")
    print("Você: MAS QUEM É VC")
    print("Hue: NÃO IMPORTA QUEM EU SOU, OU QUEM DEVERIA SER, OQ IMPORTA É PRECISAMOS IR ")
    print("(Você e hue voam)")
    print("*Na caverna de Laverna*")
    print("Fungos chegam com azuraFungos chegam com azura")
    print("Laverna Ri")
    print("Laverna: “Ora, ora, ora.... quem está aqui HAHAH, Azura a Guardiã das Fadas, mas.. espera, O SEU PESCOÇO, eu só vou perguntar uma vez (respiração profunda) ONDE ESTÁ O COLAR, ONDE ELE ESTÁ” ")
    print("Azura: “ Eu pensei que você só iria perguntar uma vez” ")
    print("Laverna fica furiosa ")
    print("Fungo:” Senhora.. vimos uma fada sem asas, voando com uma borboleta gigante...” ")
    print("Laverna:”uma.. fada sem asas... FADA DO CAMPO” ")
    print("*Você está sobrevoando sobre as nuvens, mas.. derepente” ")
    print(" Voce e Hue estão sendo atacados por pássaros de fogo  ")
    print("O que vc faz?")
    print("(1)	Voltar para a casa    ")
    print("(2) Ataca   ")
    print("(3)	Desvia e se esconde entre as arvore  ")

    while True:
        escolha = input("Digite o número da sua escolha: ")

        if escolha == "1":
            print("Você falhou com Fairytopia")
            jogador["pontuacao"] -= 10
            jogador["energia"] -= 10
            jogador["vida"] = 0
            break

        elif escolha == "2":
            print("Você não tem recursos para atacar.")
            jogador["vida"] = 0
            break

        elif escolha == "3":
            print("Você distraiu os pássaros de fogo!")
            jogador["energia"] -= 3
            jogador["pontuacao"] += 10
            break

        else:
            print("Opção inválida. Tente novamente.")
    verificar_game_over()
    verificar_vitoria()

def quarta_escolha():
    print("Vocês chegam próximos de um rio, e o principe sereio Nalu, se aproxima")
    print("Nalu: Quem são vocês? ")
    print("Você: Eu sou a fada do campo, eu estou procurando a Dahlia ")
    print("Nalu: ela está no fundo do oceano, mas existe uma alga que vc pode ingerir e respirar debaixo da agua.   ")
    print("Oq vc faz?")
    print("(1)	Come a alga ")
    print("(2)	Tenta respirar sem a alga  ")
    print("(3)	Pensa em fazer um submarino ")

    while True:
        escolha = input("Digite o número da sua escolha: ")

        if escolha == "1":
            print("Você está nadando com Nalu embusca de Dahlia")
            jogador["pontuacao"] += 10
            jogador["energia"] -= 10
            break

        elif escolha == "2":
            print("Você não resistiu ás profundezawse")
            jogador["vida"] = 0
            break

        elif escolha == "3":
            print("Você demorou muito tempo. Laverna venceu")
            jogador["energia"] -= 10
            jogador["pontuacao"] -= 10
            jogador["vida"] = 0
            break

        else:
            print("Opção inválida. Tente novamente.")
    verificar_game_over()
    verificar_vitoria()

def quinta_escolha():
    print("Você e Nalu chegaram a casa de Dahlia, ela fica relutante em ajudar pois os guardiões não confiavam nela. Mas vc a convence de fazer a escolha certa ")
    print("Dahlia: Quando eu saí da caverna da Laverna, ela tinha criado um dispositivo para sugar os poderes dos colares dos guardiões das fadas e transferi-los para si mesma. Uma dica fada do campo o ponto de união é a fraqueza dela. ")
    print("(1) Esperar 2 dias ")
    print("(2)	Agir, e  ir direto a Laverna para encontar o ponto de união e derrota-la (+30 Corajosa)")
    print("(3)	Nadar com Nalu ")

    while True:
        escolha = input("Digite o número da sua escolha: ")

        if escolha == "1":
            print("Laverna derrotou Fairytopia")
            jogador["pontuacao"] -= 10
            jogador["energia"] -= 10
            jogador["vida"] = 0
            break

        elif escolha == "2":
            print("Você etá indo até a caverna de laverna para derrota-lá")
            jogador["pontuacao"] += 10
            jogador["energia"] -= 5
            break

        elif escolha == "3":
            print("Você se distraiu com o Nalu")
            jogador["energia"] -= 10
            jogador["pontuacao"] -= 10
            jogador["vida"] = 0
            break

        else:
            print("Opção inválida. Tente novamente.")
    verificar_game_over()
    verificar_vitoria()

def sexta_escolha():
    print("Vc chega na caverna da Laverna, com o colar da Azura, enquanto a Hue distrai os fungos, vc entra em ação e encontra os guardiões. Mas algo terrível te surpreendeu.. Laverna aparece")
    print("Laverna: Ora, ora, ora... que visita agradável fada do campo. ")
    print("Vc: La..la..laverna")
    print("Laverna: Sabe.. se vc me der o colar, eu posso te conceder o maior dos seus desejos, asas, vc terá asas, como sempre sonhou ")
    print("*Laverna te hipnotizou para que andasse em sua direção*")
    print("Laverna esta prestes a absorver todos os poderes dos guardiões")
    print("Desvenda a charada para saber qual o ponto de união q pode acabar com Laverna")
    print("Sou belo e brilhante, mas não estou aqui só pra enfeitar." )
    print("Unindo caminhos, posso o segredo revelar.")
    print("No trono da vilã, estou a brilhar,")
    print("e se me encontrar, o mal pode acabar.")
    print("  e se me encontrar, o mal pode acabar.")
    print("A) Um espelho mágico ")
    print("B) Um colar com cristal encantado ")
    print("C) Uma poção adormecida  ")
    print("D) Um anel de invisibilidade ")

    while True:
        escolha = input("Digite a letra da sua escolha: ").upper()

        if escolha == "A":
            print("Laverna derrotou Fairytopia")
            jogador["pontuacao"] -= 10
            jogador["energia"] -= 10
            jogador["vida"] = 0
            break

        elif escolha == "B":
            print("Você rejeita a oferta de Laverna e arremessa o colar no ponto de união estraçalhando-o. Os poderes dos guardiões são devolvidos, e Laverna desaparece ")    
            print("De volta a Fairytopia, as flores e as fadas estão curadas. A rainha das fadas aparece")    
            print("Rainha: Obrigada! Fada do Campo por salvar Fairytopia, em recompensa ao seu ato de coragem, lhe dou esse colar mágico, que lhe dará asas, e poderá voar! ")
            print("FIM!")  
            jogador["pontuacao"] += 10
            jogador["energia"] -= 5
            break

        elif escolha == "C":
            print("Laverna derrotou Fairytopia")
            jogador["energia"] -= 10
            jogador["pontuacao"] -= 10
            jogador["vida"] = 0
            break

        elif escolha == "D":
            print("Laverna derrotou Fairytopia")
            jogador["energia"] -= 10
            jogador["pontuacao"] -= 10
            jogador["vida"] = 0
            break

        else: 
            print("Opção inválida")
    verificar_game_over()
    verificar_vitoria()



introducao()
mostrar_status()
primeira_escolha()
mostrar_status()
segunda_escolha()
mostrar_status()
terceira_escolha()
mostrar_status()
quarta_escolha()
mostrar_status()
quinta_escolha()
mostrar_status()
sexta_escolha()
mostrar_status()

