
import tweepy
from tweepy import *
from time import sleep


###########Executar esse programa em um notebook Jupyter.#############

#####Credenciais, não modificar#####
ACCESS_TOKEN = '1448727628937113603-fSajJFUidQudpOfYqBFHlGNTXP8nVa'
ACCESS_SECRET = 'ATJxgRbB1MDixHn5z267iPVndZjC6FE54GhBF8YamX9Ej'
CONSUMER_KEY = 'E8HttmPQ3MQ0uIL4SC1E8mXfK'
CONSUMER_SECRET = '7W1OfuQJeMoRPNPBqihFR15NojXmpEJuEwG932vUvlfpSPIGzI'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

#####Número tweets timeline  ######## 
print("------------------------------------------------------------------------------------------------------")
print("\nPrograma realizado por Bruno Soares Veríssimo, 2022.")
print('\nProjeto de pesquisa "INFORMAÇÕES INFUNDADAS E SEUS IMPACTOS NA PANDEMIA DA COVID-19: O CASO BRASILEIRO".')
print("\nIFMG - Campus Ouro Branco.")
print("\n----------------------------------------------------------------------------------------------------")
numero = int(input("Digite o número 1 caso queira ver sua timeline;\nO número 2 caso queira ver os detalhes de um determinado usuário;\nOu o número 3 caso queira ver os tweets e respostas de um determinado usuário:   "))
while numero == 1:
    try:
        x = int(input('Qual é a quantidade de tweets que você quer ver?  '))
        print("Últimos {} tweets da sua timeline:". format(x))
        for tweet in tweepy.Cursor(api.home_timeline).items(x):
            print('{} realizou o tweet:  {} , com o id numérico: {}.'.format(tweet.user.name, tweet.text, tweet.id))
            sleep(10)
         ####Decisão continuar ou não#######
        s = str(input("Caso queira ver um maior número de tweets digite sim, caso contrário, digite não:  "))
        while s == "sim" or  s=="Sim":
            x = int(input('Qual é a quantidade de tweets que você quer ver?'))
            print("Últimos {} tweets da sua timeline:". format(x))
            for tweet in tweepy.Cursor(api.home_timeline).items(x):
                print('{} realizou o tweet:  {} , com o id numérico: {}.'.format(tweet.user.name, tweet.text, tweet.id))
                sleep(10)
            s = str(input("Caso queira ver um maior número de tweets digite sim, caso contrário, digite não:  "))
        while s == "não" or s=="Não":
            quit()
            ######Enquanto diferentes########
        while s !="não" or s!="Não" or s!="Sim" or s!="sim":
            s = str(input("Resposta inválida. Caso queira ver um maior número de tweets digite sim, caso contrário, digite não:  "))
            while s == "sim" or  s=="Sim":
                x = int(input('Qual é a quantidade de tweets que você quer ver?'))
                print("Últimos {} tweets da sua timeline:". format(x))
                for tweet in tweepy.Cursor(api.home_timeline).items(x):
                    print('{} realizou o tweet:  {} , com o id numérico: {}.'.format(tweet.user.name, tweet.text, tweet.id))
                    sleep(10)
                s = str(input("Caso queira ver um maior número de tweets digite sim, caso contrário, digite não:  "))
            while s == "não" or s=="Não":
                quit()
    except:
        print ('Ocorreu algum erro! Tente novamente.')
        
#######Detalhes usuário#########
        
while numero == 2:
    try:
        usuario = str(input('Qual é o nome do usuário que você quer ver os detalhes?\nNo caso o @ do usuário:  '))
        screen_name = usuario
        user = api.get_user(usuario)
        x = int(input('Ok, você quer ver qual número de últimos seguidores do usuário denominado {}?\nNúmero máximo 119.  '.format(user.name)))
        print("Detalhes do usuário:")
        print('O nome completo desse usuário é: {}.'.format(user.name))
        if user.url==None:
            print ('Não há links associados ao perfil do usuário {}.'. format(user.name))
        else:
            print('O link associado ao perfil do usuário {} é: {}'.format (user.name, user.url))
        print('O ID desse usuário é: {}.'.format(user.id))
        if user.description=='':
            print ('{} não informou uma descrição.'. format(user.name))
        else:
            print('A descrição desse usuário é: {}'. format(user.description))
        if user.location =='':
            print ('{} não informou sua localização.'. format(user.name))
        else:
            print('A localização desse usuário é: {}.'.format (user.location))
        print("Últimos {} seguidores:". format(x))
        for follower in tweepy.Cursor (api.followers, screen_name).items(x):
            print('Usuário denominado: {}, com o ID: {},  seguiu o usuário: {}.  '.format(follower.name, follower.id, user.name))
            sleep(2)
        ######Continuar ou não#######
        ab = str(input("Caso queira ver os detalhes de um usuário diferente digite sim, caso contrário, digite não:  "))
        while ab=="Sim" or ab=="sim":
            usuario = str(input('Qual é o nome do usuário que você quer ver os detalhes?\nNo caso o @ do usuário:  '))
            screen_name = usuario
            user = api.get_user(usuario)
            x = int(input('Ok, você quer ver qual número de últimos seguidores do usuário denominado {}?\nNúmero máximo 119.  '.format(user.name)))
            print("Detalhes do usuário:")
            print('O nome completo desse usuário é: {}.'.format(user.name))
            if user.url==None:
                print ('Não há links associados ao perfil do usuário {}.'. format(user.name))
            else:
                print('O link associado ao perfil do usuário {} é: {}'.format (user.name, user.url))
            print('O ID desse usuário é: {}.'.format(user.id))
            if user.description=='':
                print ('{} não informou uma descrição.'. format(user.name))
            else:
                print('A descrição desse usuário é: {}'. format(user.description))
            if user.location =='':
                print ('{} não informou sua localização.'. format(user.name))
            else:
                print('A localização desse usuário é: {}.'.format (user.location))
            print("Últimos {} seguidores:". format(x))
            for follower in tweepy.Cursor (api.followers, screen_name).items(x):
                print('Usuário denominado: {}, com o ID: {},  seguiu o usuário: {}.  '.format(follower.name, follower.id, user.name))
                sleep(2)
            ab = str(input("Caso queira ver os detalhes de um usuário diferente digite sim, caso contrário, digite não:  "))
        while ab== "Não" or ab=="não":
            quit()
            ####Enquanto diferentes#######
        while ab !="não" or ab!="Não" or ab!="Sim" or ab!="sim":
            ab = str(input("Resposta inválida. Caso queira ver os detalhes de um usuário diferente digite sim, caso contrário, digite não:  "))
            while ab=="Sim" or ab=="sim":
                usuario = str(input('Qual é o nome do usuário que você quer ver os detalhes?\nNo caso o @ do usuário:  '))
                screen_name = usuario
                user = api.get_user(usuario)
                x = int(input('Ok, você quer ver qual número de últimos seguidores do usuário denominado {}?\nNúmero máximo 119.  '.format(user.name)))
                print("Detalhes do usuário:")
                print('O nome completo desse usuário é: {}.'.format(user.name))
                if user.url==None:
                    print ('Não há links associados ao perfil do usuário {}.'. format(user.name))
                else:
                    print('O link associado ao perfil do usuário {} é: {}'.format (user.name, user.url))
                print('O ID desse usuário é: {}.'.format(user.id))
                if user.description=='':
                    print ('{} não informou uma descrição.'. format(user.name))
                else:
                    print('A descrição desse usuário é: {}'. format(user.description))
                if user.location =='':
                    print ('{} não informou sua localização.'. format(user.name))
                else:
                    print('A localização desse usuário é: {}.'.format (user.location))
                print("Últimos {} seguidores:". format(x))
                for follower in tweepy.Cursor (api.followers, screen_name).items(x):
                    print('Usuário denominado: {}, com o ID: {},  seguiu o usuário: {}.  '.format(follower.name, follower.id, user.name))
                    sleep(2)
                ab = str(input("Caso queira ver os detalhes de um usuário diferente digite sim, caso contrário, digite não:  "))
            while ab== "Não" or ab=="não":
                quit()
    except:
        print ('Ocorreu algum erro! Tente novamente.')
            
#######Tweets timeline usuário#######       
while numero == 3:
    try:
        usuario1 = str(input('Qual é o nome do usuário que você quer ver os tweets?\nNo caso o @ do usuário:  '))
        screen_name = usuario1
        user = api.get_user(usuario1)
        y = int(input('Qual é a quantidade de tweets que você quer ver?  '))
        print("Últimos {} tweets do usuário denominado {}:".format(y, user.name))
        for tweet in tweepy.Cursor(api.user_timeline, screen_name).items(y):
            print('{} realizou o tweet:  {} , com o id numérico: {}.'.format(tweet.user.name, tweet.text, tweet.id))
            sleep(10)
            ######Decisão continuar ou não#######
        ab = str(input("Caso queira ver um maior número de tweets ou tweets de um usuário diferente digite sim, caso contrário, digite não:  "))
        while ab == "sim" or ab == "Sim":
            usuario1 = str(input('Qual é o nome do usuário que você quer ver os tweets?\nNo caso o @ do usuário:  '))
            screen_name = usuario1
            user = api.get_user(usuario1)
            y = int(input('Qual é a quantidade de tweets que você quer ver?  '))
            print("Últimos {} tweets do usuário denominado {}:".format(y, user.name))
            for tweet in tweepy.Cursor(api.user_timeline, screen_name).items(y):
                print('{} realizou o tweet:  {} , com o id numérico: {}.'.format(tweet.user.name, tweet.text, tweet.id))
                sleep(10)
            ab = str(input("Caso queira ver um maior número de tweets ou tweets de um usuário diferente digite sim, caso contrário, digite não:  "))
        while ab == "não" or ab=="Não":
            quit()
            #####Enquanto diferentes#####
        while ab !="não" or ab!="Não" or ab!="Sim" or ab!="sim":
            ab = str(input("Resposta inválida. Caso queira ver um maior número de tweets ou tweets de um usuário diferente digite sim, caso contrário, digite não:  "))
            while ab == "sim" or ab == "Sim":
                usuario1 = str(input('Qual é o nome do usuário que você quer ver os tweets?\nNo caso o @ do usuário:  '))
                screen_name = usuario1
                user = api.get_user(usuario1)
                y = int(input('Qual é a quantidade de tweets que você quer ver?  '))
                print("Últimos {} tweets do usuário denominado {}:".format(y, user.name))
                for tweet in tweepy.Cursor(api.user_timeline, screen_name).items(y):
                    print('{} realizou o tweet:  {} , com o id numérico: {}.'.format(tweet.user.name, tweet.text, tweet.id))
                    sleep(10)
                ab = str(input("Caso queira ver um maior número de tweets ou tweets de um usuário diferente digite sim, caso contrário, digite não:  "))
            while ab == "não" or ab=="Não":
                quit()
    except:
        print ('Ocorreu algum erro! Tente novamente.')
        
            
    #Enquanto números diferentes#
while numero != 1 or numero != 2 or numero != 3:
    numero = int(input("Resposta inválida, por favor digite o número 1 caso queira ver sua timeline;\nO número 2 caso queira ver os detalhes de um determinado usuário;\nOu o número 3 caso queira ver os tweets e respostas de um determinado usuário:   "))  
    
    #####Número tweets timeline 2 ########
    while numero == 1:
        try:
            x = int(input('Qual é a quantidade de tweets que você quer ver?  '))
            print("Últimos {} tweets da sua timeline:". format(x))
            for tweet in tweepy.Cursor(api.home_timeline).items(x):
                print('{} realizou o tweet:  {} , com o id numérico: {}.'.format(tweet.user.name, tweet.text, tweet.id))
                sleep(10)
             ####Decisão continuar ou não#######
            s = str(input("Caso queira ver um maior número de tweets digite sim, caso contrário, digite não:  "))
            while s == "sim" or s=="Sim":
                x = int(input('Qual é a quantidade de tweets que você quer ver?'))
                print("Últimos {} tweets da sua timeline:". format(x))
                for tweet in tweepy.Cursor(api.home_timeline).items(x):
                    print('{} realizou o tweet:  {} , com o id numérico: {}.'.format(tweet.user.name, tweet.text, tweet.id))
                    sleep(10)
                s = str(input("Caso queira ver um maior número de tweets digite sim, caso contrário, digite não:  "))
            while s == "não" or s=="Não":
                quit()
                ####Enquanto diferentes#####
            while s !="não" or s!="Não" or s!="Sim" or s!="sim":
                s = str(input("Resposta inválida. Caso queira ver um maior número de tweets digite sim, caso contrário, digite não:  "))
                while s == "sim" or  s=="Sim":
                    x = int(input('Qual é a quantidade de tweets que você quer ver?'))
                    print("Últimos {} tweets da sua timeline:". format(x))
                    for tweet in tweepy.Cursor(api.home_timeline).items(x):
                        print('{} realizou o tweet:  {} , com o id numérico: {}.'.format(tweet.user.name, tweet.text, tweet.id))
                        sleep(10)
                    s = str(input("Caso queira ver um maior número de tweets digite sim, caso contrário, digite não:  "))
                while s == "não" or s=="Não":
                    quit()
        except:
            print ('Ocorreu algum erro! Tente novamente.')
                
            #######Detalhes usuário 2#######
    while numero == 2:
        try:
            usuario = str(input('Qual é o nome do usuário que você quer ver os detalhes?\nNo caso o @ do usuário:  '))
            screen_name = usuario
            user = api.get_user(usuario)
            x = int(input('Ok, você quer ver qual número de últimos seguidores do usuário denominado {}?\nNúmero máximo 119.  '.format(user.name)))
            print("Detalhes do usuário:")
            print('O nome completo desse usuário é: {}.'.format(user.name))
            if user.url==None:
                print ('Não há links associados ao perfil do usuário {}.'. format(user.name))
            else:
                print('O link associado ao perfil do usuário {} é: {}'.format (user.name, user.url))
            print('O ID desse usuário é: {}.'.format(user.id))
            if user.description=='':
                print ('{} não informou uma descrição.'. format(user.name))
            else:
                print('A descrição desse usuário é: {}'. format(user.description))
            if user.location =='':
                print ('{} não informou sua localização.'. format(user.name))
            else:
                print('A localização desse usuário é: {}.'.format (user.location))
            print("Últimos {} seguidores:". format(x))
            for follower in tweepy.Cursor (api.followers, screen_name).items(x):
                print('Usuário denominado: {}, com o ID: {},  seguiu o usuário: {}.  '.format(follower.name, follower.id, user.name))
                sleep(2)
                ######Decisão continuar ou não########
            ab = str(input("Caso queira ver os detalhes de um usuário diferente digite sim, caso contrário, digite não:  "))
            while ab=="Sim" or ab=="sim":
                usuario = str(input('Qual é o nome do usuário que você quer ver os detalhes?\nNo caso o @ do usuário:  '))
                screen_name = usuario
                user = api.get_user(usuario)
                x = int(input('Ok, você quer ver qual número de últimos seguidores do usuário denominado {}?\nNúmero máximo 119.  '.format(user.name)))
                print("Detalhes do usuário:")
                print('O nome completo desse usuário é: {}.'.format(user.name))
                if user.url==None:
                    print ('Não há links associados ao perfil do usuário {}.'. format(user.name))
                else:
                    print('O link associado ao perfil do usuário {} é: {}'.format (user.name, user.url))
                print('O ID desse usuário é: {}.'.format(user.id))
                if user.description=='':
                    print ('{} não informou uma descrição.'. format(user.name))
                else:
                    print('A descrição desse usuário é: {}'. format(user.description))
                if user.location =='':
                    print ('{} não informou sua localização.'. format(user.name))
                else:
                    print('A localização desse usuário é: {}.'.format (user.location))
                print("Últimos {} seguidores:". format(x))
                for follower in tweepy.Cursor (api.followers, screen_name).items(x):
                    print('Usuário denominado: {}, com o ID: {},  seguiu o usuário: {}.  '.format(follower.name, follower.id, user.name))
                    sleep(2)
                ab = str(input("Caso queira ver os detalhes de um usuário diferente digite sim, caso contrário, digite não:  "))
            while ab== "Não" or ab=="não":
                quit()
                ######Enquanto diferentes#####
            while ab !="não" or ab!="Não" or ab!="Sim" or ab!="sim":
                ab = str(input("Resposta inválida. Caso queira ver os detalhes de um usuário diferente digite sim, caso contrário, digite não:  "))
                while ab=="Sim" or ab=="sim":
                    usuario = str(input('Qual é o nome do usuário que você quer ver os detalhes?\nNo caso o @ do usuário:  '))
                    screen_name = usuario
                    user = api.get_user(usuario)
                    x = int(input('Ok, você quer ver qual número de últimos seguidores do usuário denominado {}?\nNúmero máximo 119.  '.format(user.name)))
                    print("Detalhes do usuário:")
                    print('O nome completo desse usuário é: {}.'.format(user.name))
                    if user.url==None:
                        print ('Não há links associados ao perfil do usuário {}.'. format(user.name))
                    else:
                        print('O link associado ao perfil do usuário {} é: {}'.format (user.name, user.url))
                    print('O ID desse usuário é: {}.'.format(user.id))
                    if user.description=='':
                        print ('{} não informou uma descrição.'. format(user.name))
                    else:
                        print('A descrição desse usuário é: {}'. format(user.description))
                    if user.location =='':
                        print ('{} não informou sua localização.'. format(user.name))
                    else:
                        print('A localização desse usuário é: {}.'.format (user.location))
                    print("Últimos {} seguidores:". format(x))
                    for follower in tweepy.Cursor (api.followers, screen_name).items(x):
                        print('Usuário denominado: {}, com o ID: {},  seguiu o usuário: {}.  '.format(follower.name, follower.id, user.name))
                        sleep(2)
                    ab = str(input("Caso queira ver os detalhes de um usuário diferente digite sim, caso contrário, digite não:  "))
                while ab== "Não" or ab=="não":
                    quit()
        except:
            print ('Ocorreu algum erro! Tente novamente.')
            
    #######Tweets timeline usuário 2#######
    while numero == 3:
        try:
            usuario1 = str(input('Qual é o nome do usuário que você quer ver os tweets?\nNo caso o @ do usuário:  '))
            screen_name = usuario1
            user = api.get_user(usuario1)
            y = int(input('Qual é a quantidade de tweets que você quer ver?  '))
            print("Últimos {} tweets do usuário denominado {}:".format(y, user.name))
            for tweet in tweepy.Cursor(api.user_timeline, screen_name).items(y):
                print('{} realizou o tweet:  {} , com o id numérico: {}.'.format(tweet.user.name, tweet.text, tweet.id))
                sleep(10)
            ab = str(input("Caso queira ver um maior número de tweets ou tweets de um usuário diferente digite sim, caso contrário, digite não:  "))
            while ab == "sim" or ab == "Sim":
                usuario1 = str(input('Qual é o nome do usuário que você quer ver os tweets?\nNo caso o @ do usuário:  '))
                screen_name = usuario1
                user = api.get_user(usuario1)
                y = int(input('Qual é a quantidade de tweets que você quer ver?  '))
                print("Últimos {} tweets do usuário denominado {}:".format(y, user.name))
                for tweet in tweepy.Cursor(api.user_timeline, screen_name).items(y):
                    print('{} realizou o tweet:  {} , com o id numérico: {}.'.format(tweet.user.name, tweet.text, tweet.id))
                    sleep(10)
                    #####Decisão continuar ou não#######
                ab = str(input("Caso queira ver um maior número de tweets ou tweets de um usuário diferente digite sim, caso contrário, digite não:  "))
            while ab == "não" or ab=="Não":
                quit()
                ######Enquanto diferentes########
            while ab !="não" or ab!="Não" or ab!="Sim" or ab!="sim":
                ab = str(input("Resposta inválida. Caso queira ver um maior número de tweets ou tweets de um usuário diferente digite sim, caso contrário, digite não:  "))
                while ab == "sim" or ab == "Sim":
                    usuario1 = str(input('Qual é o nome do usuário que você quer ver os tweets?\nNo caso o @ do usuário:  '))
                    screen_name = usuario1
                    user = api.get_user(usuario1)
                    y = int(input('Qual é a quantidade de tweets que você quer ver?  '))
                    print("Últimos {} tweets do usuário denominado {}:".format(y, user.name))
                    for tweet in tweepy.Cursor(api.user_timeline, screen_name).items(y):
                        print('{} realizou o tweet:  {} , com o id numérico: {}.'.format(tweet.user.name, tweet.text, tweet.id))
                        sleep(10)
                    ab = str(input("Caso queira ver um maior número de tweets ou tweets de um usuário diferente digite sim, caso contrário, digite não:  "))
                while ab == "não" or ab=="Não":
                    quit()
        except:
            print ('Ocorreu algum erro! Tente novamente.')

