# fazer a classe
class jogadorpingpong:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
    def sacar(self):
      print("sacar: ping")

    def rebater (self):
      print("rebater: pong")

    #criando o objeto da classe. "instancia"
Bruno = jogadorpingpong("Bruno",16,)
Pedro = jogadorpingpong("Pedro",16,)

#chamando o objeto na tela

print("meu jogador se chama {} e possui {} anos".format(Bruno.nome,Bruno.idade))
Bruno.sacar()

print("meu jogador se chama {} e possui {} anos".format(Pedro.nome,Pedro.idade))
Pedro.rebater()
