from time import sleep

print ("saturn: bem-vindo ao quiz!\n") 
sleep(1)
print ("saturn: a cada resposta correta, você GANHA um ponto.\n        a cada resposta errada, você PERDE um ponto.\n        são dez perguntas.\n") 
sleep(1)


jogando = input("saturn: você quer jogar?\n ")

if jogando != "sim":
    quit()

pontos = 0

print("\nsaturn: ok, vamos jogar.\n") 
sleep(2)


resp = input("saturn: quanto é 1 + 1?\n ")
if resp == "2":
    sleep(1)
    print("\nsaturn: correto!")
    pontos += 1
    sleep(1/3)
    print("seu score total é de: " + str(pontos))
else:                                      
    sleep(1)
    print("\nsaturn: errado.")
    pontos -= 1
    sleep(1/3)
    print("saturn: seu score total é de: " + str(pontos))
