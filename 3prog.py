dic = {"Joao": "a", "Maria" : "b"} #armenza o conteudo ex: a variavel A armazena em Joao 
s = "%(Joao)s e %(Maria)s" # a porcentagem vai pegar o conteudo de Joao e Maria (A e B) s é como se fosse F de função
print(s%dic) 