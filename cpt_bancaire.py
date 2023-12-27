import math 
import random
# premier programme (plus simple) avec dictionnaire remplie .




# fonctions relative à l'agent de la bank.
clients ={                       #  numcl : mpc    numcl =  number of the client    mpc =password of account
    1 : "code1" ,

    2 : "code2" ,

    3 : "code3" 
}
clientcompt ={                                #numcl : numc       numc = number of the account
    1 : 10 ,

    2 : 20,

    3 : 30
}
compt = {                                     #numc : soldec     soldec = solde of the account
    10 : 0 ,

    20 : 0 ,

    30 : 0
}

def Ajouter_client():
          numcl = int(input("entrer le numero de client: "))
          def lamda_num_compte():
               x = (random.randint(0,100))
               numc = numcl*100 + x
               return numc
          numc = lamda_num_compte()
          mpc =input("entrer le code de securité: ")
          soldec = input("entrer le solde: ")
          clients.update({ numcl : mpc})
          clientcompt.update({ numcl : numc })
          compt.update({ numcl : soldec })


def supprimerclient():
           sc = int(input("entrer le num de compte que vous desirer supprimer: "))
           del compt[sc]
           for  key, value in clientcompt.items():
                   if sc == value :
                      x = key
           del clientcompt[x]
           del clients[x]


def modifier_client_mp():
        numcl =int(input("entrer le numero de client"))
        mpc =input("entrer le code de securité")
        clients[numcl] = mpc
        
         
def deposer():
        numc = int(input("type compt nbr: "))
        arg= int(input("type de nbr of moneyyyy: "))
        for key , value in compt.items():
                if numc == key :
                        x = value + arg
        compt[numc] = x

def retirer():
        numc = int(input("type compt nbr: "))
        arg= int(input("type de nbr of moneyyyy: "))
        for key , value in compt.items():
                if numc == key :
                        x = value - arg
        compt[numc] = x
        
        
  
    
Ajouter_client()
print(clientcompt)
supprimerclient()
print("dictionnaire de compt:  ")
print(compt)
print("dic de clients compt:")
print(clientcompt)
print("dic de client:")
print(clients)

print("pour deposer")
deposer()
print(compt)

print("pour retirer")
retirer()
print(compt)


