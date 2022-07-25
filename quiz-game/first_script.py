from time import sleep

print ("saturn: bem-vindo ao quiz!\n") 
sleep(1)
print ("saturn: a cada resposta correta, você GANHA um ponto.\n        a cada resposta errada, você PERDE um ponto.\n        são dez perguntas.\n") 
sleep(1)


jogando = input("saturn: você quer jogar? [s/n]\n escolha: ")

if jogando != "s":
    print("\nsaturn: finalizando o processo")
    sleep(2)
    quit()

pontos = 0


print("\nsaturn: ok, vamos jogar.\n") 
sleep(2)

###pergunta 1

resp = input("saturn: quanto é 1 + 1?\n ")
if resp == "2":
    sleep(1)
    print("\nsaturn: correto!")
    pontos += 1
    sleep(1/3)
    print("seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)
else:                                      
    sleep(1)
    print("\nsaturn: errado.")
    pontos -= 1
    sleep(1/3)
    print("saturn: seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)


###pergunta 2

resp = input("saturn: quanto é 99 + 4? \n ")
if resp == "103":
    sleep(1)
    print("\nsaturn: correto!")
    pontos += 1
    sleep(1/3)
    print("seu score total é de: " + str(pontos) + "\n\n")
else:                                      
    sleep(1)
    print("\nsaturn: errado.")
    pontos -= 1
    sleep(1/3)
    print("saturn: seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)


###pergunta 3

resp = input("saturn: quanto é 7 * 4?\n ")
if resp == "28":
    sleep(1)
    print("\nsaturn: correto!")
    pontos += 1
    sleep(1/3)
    print("seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)
else:                                      
    sleep(1)
    print("\nsaturn: errado.")
    pontos -= 1
    sleep(1/3)
    print("saturn: seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)


###pergunta 4

resp = input("saturn: quanto é 5 / 5?\n ")
if resp == "1":
    sleep(1)
    print("\nsaturn: correto!")
    pontos += 1
    sleep(1/3)
    print("seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)
else:                                      
    sleep(1)
    print("\nsaturn: errado.")
    pontos -= 1
    sleep(1/3)
    print("saturn: seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)


###pergunta 5

resp = input("saturn: quanto é 5 / 5?\n ")
if resp == "1":
    sleep(1)
    print("\nsaturn: correto!")
    pontos += 1
    sleep(1/3)
    print("seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)
else:                                      
    sleep(1)
    print("\nsaturn: errado.")
    pontos -= 1
    sleep(1/3)
    print("saturn: seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)


###pergunta 6

resp = input("saturn: quanto é 3 * 9?\n ")
if resp == "27":
    sleep(1)
    print("\nsaturn: correto!")
    pontos += 1
    sleep(1/3)
    print("seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)
else:                                      
    sleep(1)
    print("\nsaturn: errado.")
    pontos -= 1
    sleep(1/3)
    print("saturn: seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)


###pergunta 7

resp = input("saturn: quanto é 9 / 3?\n ")
if resp == "3":
    sleep(1)
    print("\nsaturn: correto!")
    pontos += 1
    sleep(1/3)
    print("seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)
else:                                      
    sleep(1)
    print("\nsaturn: errado.")
    pontos -= 1
    sleep(1/3)
    print("saturn: seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)


###pergunta 8

resp = input("saturn: quanto é 5 * 5?\n ")
if resp == "25":
    sleep(1)
    print("\nsaturn: correto!")
    pontos += 1
    sleep(1/3)
    print("seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)
else:                                      
    sleep(1)
    print("\nsaturn: errado.")
    pontos -= 1
    sleep(1/3)
    print("saturn: seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)

###pergunta 9

resp = input("saturn: quanto é 8 * 7?\n ")
if resp == "54":
    sleep(1)
    print("\nsaturn: correto!")
    pontos += 1
    sleep(1/3)
    print("seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)
else:                                      
    sleep(1)
    print("\nsaturn: errado.")
    pontos -= 1
    sleep(1/3)
    print("saturn: seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)

###pergunta 10

resp = input("saturn: quanto é 1 - 4?\n ")
if resp == "-3":
    sleep(1)
    print("\nsaturn: correto!")
    pontos += 1
    sleep(1/3)
    print("seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)
else:                                      
    sleep(1)
    print("\nsaturn: errado.")
    pontos -= 1
    sleep(1/3)
    print("saturn: seu score total é de: " + str(pontos) + "\n\n")
    sleep(1/2)

### encerrando jogo e mostrando pontuação

if(pontos>=6):
    print("saturn: parabéns! você fez " + str(pontos) + " pontos.\n        o mínimo para passar são 6 pontos.")
else:
    print("saturn: você fez " + str(pontos) + " pontos.\n        o mínimo para passar são 6 pontos.")

sleep(2)
print("\n\n=========================================\n\nsaturn: obrigado por jogar!\n        finalizando o jogo em 15 segundos.\n\n=========================================\n")
sleep(15)
