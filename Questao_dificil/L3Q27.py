1agenda =  {}
print("Agenda da Instituição Y")
resposta ="S"
while resposta == "S":
    nome = input ("Digite o nome do servidor ou colaborador que deseja cadastrar: ")
    endereco = input ("Digite o endereço: ")
    dd = int (input ("Digite o DD: "))
    telefone = int (input ("Digite o telefone: "))

    agenda[nome] = {
        "Nome": nome,
        "Endereco": endereco,
        "DD": dd,
        "Telefone": telefone
    }

    resposta= input ("Deseja cadastrar outra pessoa? (S/N) ")

print("Contatos cadastrados: ")

for contato in agenda:
    print("Nome: ",agenda[contato]["Nome"])
    print("Endereço: ",agenda[contato]["Endereco"])
    print ("DD: ",agenda[contato] ["DD"])
    print("Telefone: ",agenda[contato] ["Telefone"])
    print("-"*30)

arquivo = open("agenda.txt", "w", encoding="utf-8")
for contato in agenda:
    arquivo.write("Nome: " + agenda[contato]["Nome"] + "\n" )
    arquivo.write("Endereço: " + agenda[contato]["Endereco"] + "\n" )
    arquivo.write("DD: " + str(agenda[contato]["DD"]) + "\n" )
    arquivo.write("Nome: " + str(agenda[contato]["Nome"]) + "\n")
    print("-"*30)
arquivo.close()

nomep = input ("Digite o nome do servidor ou colaborador que deseja pesquisar: ")

if nomep in agenda:
    print ("DD:", agenda[nomep]["DD"])
    print ("Telefone:", agenda[nomep]["Telefone"])
else:
    print("Contato nao encontrado! ")
