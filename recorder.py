tentativas = 0
esperança = True

while esperança:
    i_am = input("eu consigo tentar mais uma vez? [Sim]ou [Nao]")
    if i_am =='Sim':
        tentativas +=1
        print(f"tentando {tentativas}")
    else:
        print(f'''
             em toda minha vida eu tentei {tentativas} '''
              )
        esperança = False