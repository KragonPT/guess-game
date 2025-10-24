nome = input("Qual o teu nome?")
idade = int(input("Quantos anos tens?"))
print ("Olá", nome, "!")
print ("Tu tens", idade, "anos.")
if idade < 13:
  print("És uma criança.")
elif idade < 18:
  print("És um adolescente.")
elif idade < 65:
  print("És um adulto.")
else:
  print("És um idoso.")
