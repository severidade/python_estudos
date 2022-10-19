caracteres_file = open(file="data/meus_personagens.txt", mode="w")

caracteres_file.write('Mônica\n')
caracteres_file.write('Cebolinha\n')
caracteres_file.write('Bob Esponja\n')

print("Batman", file=caracteres_file)
# O print passando o nome do arquivo como parâmetro
# insere o personagem no arquivo

more_characteres = ["Magali\n", "Almirante\n"]

caracteres_file.writelines(more_characteres)

caracteres_file.close()
