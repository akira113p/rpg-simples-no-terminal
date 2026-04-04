import random
print("Olá, bem vindo ao nosso sistema de RPG do FIAPMON")
print(" aqui é assim que funciona, Magos tem proeficiencia em magia, guerreiros em força e arqueiros em agilidade")
print(" Neste game você ira enfrentar inimigo e se melhorar para enfrentar seres mais fortes.")
print(" Você nescessita de 1000 de xp para upar para o proximo nivel, o 2° ataque é liberado ao nivel 4, o 3° é ao nivel 11. Vamos começar?")
nivel = 1
LV = 1
xp = 0
ataque2BLOCK = True
ataque3BLOCK = True
perdeu = False
especial = 0
upgrade = False
serio = ""
nome = input("Então, qual sera seu nome?")
lvAntigo = 1
 
if nome == "":
    nome = "Sem nome"
   
def mago():
    vida = 80
    magia = 15
    agilidade = 6
    forca= 1
    return vida, magia,agilidade,forca
def Guerreiro():
    vida = 150
    forca = 10
    agilidade = 3
    magia = 0
 
    return vida, magia,agilidade,forca
def Arqueiro():
    #a base do atque do arqueiro e agilidade
    forca = 5
    agilidade = 10
    magia =1
    vida = 100
 
    return vida, magia,agilidade,forca,
def admin():
    vida=9999999999999999999999999999999999
    forca = 10000
    agilidade = 10000
    magia =100000
    vida = 100000000
 
    return vida, magia,agilidade,forca
 
while True:
    print("qual sua classe")
    print("")
    print("mago -1")
    print("guerreiro -2")
    print("arqueiro -3")
    escolha = (input("qual sera a sua escolha?  "))
    print("")
    if escolha == "1":
       
        vida, magia, agilidade, forca = mago()
        classe_escolhida = "mago"
        ataque1Name ="Fireball"
        ataque2Name ="ThunderBolt"
        ataque3Name ="IceDagger"
        break
    elif escolha == "2":
        vida, magia, agilidade, forca  = Guerreiro()
        classe_escolhida = "guerreiro"
        ataque1Name ="Ruptura"
        ataque2Name ="Impacto"
        ataque3Name ="Devastação"
        break
    elif escolha == "3":
        vida, magia, agilidade, forca = Arqueiro()
        classe_escolhida = "arqueiro"
        ataque1Name ="Perfuração"
        ataque2Name ="Tempestade"
        ataque3Name ="Disparo_Pesado"
        break
    elif escolha == "admin":
        vida, magia, agilidade, forca = admin()
        classe_escolhida = "admin"
        ataque1Name ="ChaosHand"
        ataque2Name ="ToonForce"
        ataque3Name ="Cmd"
        break
    else:
        print("escolha uma classe valida")
while True:
    if classe_escolhida == "mago":
         ataque1 = magia + (0.2 * agilidade)
         ataque2 =  (magia * 1.5 + 0.5 * agilidade)
         ataque3 = forca * 0.2 + (magia * 2.5 + 0.2 * agilidade)
         ataque4=magia * 10000000
    elif classe_escolhida == "guerreiro":
         ataque1 = forca * 1 + (0.3 * agilidade)
         ataque2 = forca * 2 + (0.4 * agilidade)
         ataque3 = forca * 2.5 + (0.6 * agilidade)
    elif classe_escolhida == "arqueiro":
         ataque1 = (forca * 0.4) + agilidade
         ataque2 = forca * 0.5 + (agilidade * 2  )
         ataque3 = forca * 0.3 + (agilidade * 2.7 )
    elif classe_escolhida == "admin":
         ataque1 = (forca * 0.2) + agilidade + (0.2 * magia)
         ataque2 = forca * 0.3 + (agilidade * 2 + 0.3 * magia)
         ataque3 = forca * 0.3 + (agilidade * 3 + 0.5 * magia)
 
    poder = forca*2 +agilidade +magia
    if upgrade:
       LV,vida,forca,magia,agilidade,upgrade,lvAntigo = up(LV,vida,forca,magia,agilidade,upgrade,lvAntigo)
 
    if perdeu:
        break
   
   
    if LV >=4 and ataque2BLOCK:
        ataque2BLOCK = False
        input("")
        print(f"vc desbloqueou um novo ataque, parabens --ataque2--")
    if LV >=11 and ataque3BLOCK:
        ataque3BLOCK = False
        input("")
        print(f"vc desbloqueou um novo ataque, parabens --ataque3--")
 
 
    if ataque2BLOCK:
        textoATK2 = "BLOQUEADO"
    else:
        textoATK2 = f"{ataque2}"
    if ataque3BLOCK:
        textoATK3 = "BLOQUEADO"
    else:
        textoATK3 = f"{ataque3}"
 
   
    def status(xp, LV,vida,poder,forca,magia,agilidade,):
        print("")
        print("")    
        print("seus status")
        print("------------------")
        print(f"LV = {LV}  ")
        print(f"xp = {int(xp)}  ")
        print(f"vida = {int(vida)}  ")
        print(f"magia = {magia} ")
        print(f"agilidade = {agilidade} ")
        print(f"forca = {forca} ")
        print(f"poder = {poder} ")
        print(f"{ataque1Name} = {ataque1} ")
        print(f"{ataque2Name} = {textoATK2} ")
        print(f"{ataque3Name} = {textoATK3} ")
        print("------------------")
 
       
    def classificacao(LV):
        print("")
        print("")    
        print("CLASIFICAÇAO")
        print("------------------")
        if LV <10:
            print("BRONZE")
        elif LV >=10 and LV <20 :
            print("PRATA")
        elif LV >=20 and LV <40 :
            print("OURO")
        elif LV >=40:
            print("Lendário")
        print("")
        print("")
   
 
 
    def inimigo1():
        xpMau=1200* nivel * 0.6
        vidaMau = 50 + nivel *0.8
        ataqueMau=7*nivel + nivel*1
       
        return vidaMau,ataqueMau,xpMau
    def inimigo2():
        xpMau=1100 * nivel * 0.7
        vidaMau = 40  + nivel*1.1
        ataqueMau=11+ nivel*2
        return vidaMau,ataqueMau,xpMau
    def inimigo3():
        xpMau=1000 *nivel * 0.6
        vidaMau = 100 +nivel + nivel*2
        ataqueMau=+nivel + nivel*0.8
        return vidaMau,ataqueMau,xpMau
 
    def up(LV,vida,forca,magia,agilidade,upgrade,lvAntigo):
        print(f"voce ganhou {LV-lvAntigo} leveis")
        while lvAntigo < LV:
            lvAntigo = lvAntigo+1
            print("====================================")
            print("escolha uma habiliade para aprimorar!")
            print(f"========seu nivel atual é {lvAntigo}=====")
            print("====================================")
            print("")
            input("")
            print("--------------------")
            print("vida -1")
            print("magia -2")
            print("agilidade -3")
            print("forca -4")
            print("--------------------")
            print("")    
            powerup = (input("escolha um   "))
            print("")
            if powerup == "1":
                vida = vida + vida *0.5
            elif powerup == "2":
                magia = magia + magia
            elif powerup == "3":
                agilidade = agilidade + agilidade
            elif powerup == "4":
                forca = forca + forca
            else:
                print("Escolha um numereo valido")
           
        upgrade = False
        return LV,vida,forca,magia,agilidade,upgrade,lvAntigo
   
    def batalha(especial, perdeu, vida, ataque1, ataque2, ataque3, LV, xp, ataque3BLOCK, ataque2BLOCK, textoATK2, textoATK3, nivel,upgrade,lvAntigo):
        lvAntigo = LV
        possicao = random.randint(1, 3)
 
        if possicao == 1:
                vidaMau,ataqueMau,xpMau=inimigo1()
                inimigo="Goblin"
 
        elif possicao ==2:
                vidaMau,ataqueMau,xpMau=inimigo2()
                inimigo="Bandido"
        else:
            vidaMau,ataqueMau,xpMau=inimigo3()
            inimigo="Golem de Pedra"
 
 
       
        print("")
        print("")    
        print(f"seu inimigo sera --{inimigo}-- voce esta na fase--{nivel}--")
        input("")
        print("------------------")
        print("==================")
        print("------------------")
        print("seus status")
        print(f"vida--{int(vida)}--    LV--{LV}--    XP--{int(xp)}")
        print("------------------")
        print("inimigo status")
        print(f"vida--{int(vidaMau)}--    LV--{int(xpMau/1000)}--    XP--{int(xpMau)}")
        print("==================")
        input("")
        if ataque2BLOCK == False:
            textoATK2 = f"{textoATK2} damage"
        if ataque3BLOCK ==False:
            textoATK3 = f"{textoATK3} damage"
   
 
        turno =1
        LVantigo=LV
        while vida >=0 and vidaMau >=0:
           
            if especial <10:
               especial = especial+1
            print(f"turno {turno}")
            print("ataques")
            print(f"1--{ataque1Name}--{ataque1}Damage--    2--{ataque2Name}--{textoATK2}--    3--{ataque3Name}--{textoATK3}--    4--abilidade especial--{especial}/10({poder+ poder}damage--    poupar --5--")
            print("------------------")
           
            while True:
 
               
                critico = random.randint(1, 10)
                escolheAtaque = (input("escolha seu ataque  "))
                if escolheAtaque == "1":
                    ataqueAtual = ataque1
                    break
                elif escolheAtaque == "2":
                    if ataque2BLOCK:
                        print("esse ataque esta bloquedo")
                    else:  
                        ataqueAtual = ataque2
                        break
                elif escolheAtaque == "3":
                    if ataque3BLOCK:
                        print("esse ataque esta bloquedo")
                    else:  
                        ataqueAtual = ataque3
                        break
                elif escolheAtaque == "4":
                    if especial == 10:
                        ataqueAtual = poder+ poder +poder * 0.6
                        print("ESPECIAL   0/10")
                        especial= 0
                        break
                    else:
                       print(f"seu ESPECIAL ainda nao carregou  {especial}/10")
                   
                   
                elif escolheAtaque == "5":
                    ataqueAtual = 0
                    print("------------------")
                    print("vc poupou o inimigo")
                    print("ele ainda quer te matar...")
                    print("------------------")
                    input("")
                    break
                else:
                    print("escolha um valor validdo")
            print("------------------")    
            if critico == 1:
                ataqueAtual = ataqueAtual*2
                print("SEU ATAQUE FOI CRITICO")
           
            print(f"seu dano foi de {ataqueAtual}damage")
            input("")
            vidaMau = vidaMau- ataqueAtual
            print(f"vida atual do {inimigo}--({int(vidaMau)})--")
            print("------------------")
 
 
            if vidaMau > 0:
 
                turno = turno +1
                print(f"turno {turno}")
                input("")
                if critico == 2:
                    print(f"o ataque do {inimigo} foi CRITICO")
                    vida = vida- ataqueMau*1.5
                    print(f"vc recebeu {ataqueMau*2}damage")
                else:
                    vida = vida- ataqueMau  
                    print(f"vc recebeu {ataqueMau}damage")                              
               
                input("")
                print(f"sua vida atual e --({int(vida)})--")
                input("")
                print("------------------")
                print("")
       
        print("------------------")
        print("==================")
        print("------------------")
        if vida <= 0:
            perdeu = True
            print("Você foi morto")
        else:
            input("")
            print("vc ganhou o duelo!!")
            nivel = nivel +1
            print("------------------")
            vida = vida*1.2
            print (f"voce recuperou 20% da sua vida // vida atual ={int(vida)}")
            xp = xp +xpMau
            LV=1 + int(xp/1000)
            if LV != LVantigo:
                upgrade = True
            input("")
            print(f"voce ganhou {xpMau} de xp    seu nivel e {LV}({xp}xp) ")
 
            print("")
            print("")
        return xp, LV,ataque2BLOCK,ataque3BLOCK,vida,nivel,perdeu,especial,upgrade,lvAntigo
 
    def menu(especial, perdeu, vida, ataque1, ataque2, ataque3, LV, xp, ataque3BLOCK, ataque2BLOCK, nivel, forca, magia, agilidade,upgrade,serio,lvAntigo):
       
        while True:
           
 
            print("")
            print("status -1")
            print("classificacao -2")
            print("batalha -3")
            print("sair do jogo -4")
           
            print("==================")
            click = (input("escolha  "))
            if click =="1":
                print("")
                status(xp, LV,vida,poder,forca,magia,agilidade)
                print("==================")
                input()
               
               
               
            elif click =="2":
                print("")
                classificacao(LV)
                print("==================")
                input()
               
               
            elif click =="3":
                xp, LV, ataque2BLOCK, ataque3BLOCK, vida,nivel,perdeu,especial,upgrade,lvAntigo = batalha(especial, perdeu, vida, ataque1, ataque2, ataque3, LV, xp, ataque3BLOCK, ataque2BLOCK, textoATK2, textoATK3, nivel,upgrade,lvAntigo)
               
                break
 
            elif click =="4":
                print("")
                print("tem certeza que deseja encerar o jogo?")
                print("")
                print("--------------------")
                print("sim-1")
                print("nao-2")
                print("--------------------")
                serio = input("quer sair?  ")
                if(serio =="1"):
                    break
               
               
            else:
                print("")
                print("==================")
                print("invalido")
                print("==================")
     
 
        return xp, LV, ataque2BLOCK, ataque3BLOCK, vida, nivel, perdeu, especial,upgrade,serio,lvAntigo
           
    xp, LV, ataque2BLOCK, ataque3BLOCK, vida, nivel, perdeu, especial,upgrade,serio,lvAntigo = menu(especial, perdeu, vida, ataque1, ataque2, ataque3, LV, xp, ataque3BLOCK, ataque2BLOCK, nivel, forca, magia, agilidade,upgrade,serio,lvAntigo)
    if(serio =="1"):
 
        break
   
if LV <10:
  ranking=  "BRONZE"
elif LV >=10 and LV <20 :
   ranking= "PRATA"
elif LV >=20 and LV <40 :
   ranking= "OURO"
elif LV >=40:
   ranking= "Lendário"
 
print("")
print("")
print("==================")
if perdeu:
    print("VC MORREU")
else:
    print("VC TERMINOU O JOGO")
print("==================")
print("")
print("")
print("==================")
print(f"seu nome foi {nome}")
print(f"sua classe foi {classe_escolhida}")
print(f"seu ranking foi {ranking}")
print(f"vc derrotou {nivel} inimigos")
 
print("==================")