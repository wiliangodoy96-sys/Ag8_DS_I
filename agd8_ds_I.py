# Programar para uma pesquisa de opinião com seus clientes para saber o grau de satisfação no atendimento.
# Autor: Wilian Godoy Francisco

# Contadores - fazem o registro de contagem em "excelente" e "ruim"
excelente = 0
ruim = 0

# Estrutura de repetição para pesquisa dos clientes
for i in range (10): # estrutura de repetição para que após o prenchimento do nome, idade e nota de opinião, seja gerado um loop para um novo preenchimento, até fechar a quantidade de pessoas pesqisada

# Entrada de Dados
	nome = input("Digite o seu Nome: ")
	idade = int(input("Digite a sua Idade: "))
	opiniao = int(input("Digite sua Opção Sobre o Atendimento - 1: Excelente; 2: Bom; 3: Ruim: "))

# Decisões 
	if opiniao ==1:
		excelente +=1
	elif opiniao ==3:
		ruim +=1

# Impressão da resposta de contagem
print ("RESULTADO DA PESQUISA")
print ("resposta excelente: ", excelente)
print ("resposta ruim:", ruim)
