from abc import ABCMeta , abstractmethod
from collections import *

  

class produit(metaclass = ABCMeta) :
    def __init__(self , nom , code) :
        self.__nom = nom
        self.__code = code

    @property
    def nom (self) :
        return self.__nom

    @property
    def code(self) :
        return self.__code

    @abstractmethod
    def getPrixAchat(self) :
        pass

class produitElementaire(produit) :
    def __init__(self, nom, code , prixAchat):
        super().__init__(nom, code) 
        self.__prixAchat = prixAchat

    
    @property
    def prixAchat(self) :
        return self.__prixAchat                                      
    def __str__(self) :
        return (f" [{self.nom}] ( code : {self.code}, prix:{self.__prixAchat} dh )")

    def getPrixAchat(self):
        return self.__prixAchat
  





class composition(produitElementaire) :
    def __init__(self ,produitelem  , quantite ) :
        super().__init__(produitelem.nom,produitelem.code,produitelem.prixAchat)
        self.__quantite = quantite
    
     
    
    @property
    def quantite(self) :
        return self.__quantite
    
    @quantite.setter
    def quantite(self , value) :
        self.__quantite = value
    def __str__(self) :
        return f"Quntitie = { self.quantite }  de produit : { super().__str__() } "
    def compositionPrix(self):
        return self.getPrixAchat() * self.__quantite




class produit_compose  :
    tauxTVA = 0.18 
    def __init__(self,nom,  fraisFabrication , listeConstituants ):
        self.__fraisFabrication = fraisFabrication
        self.__listeConstituants =  listeConstituants
        self.__nom = nom
    @property  
    def fraisFabrication(self) :
        return self.__fraisFabrication
    
    @fraisFabrication.setter
    def fraisFabrication(self , value) :
        self.__fraisFabrication = value

    
    @property
    def listeConstituants(self) :
        return self.__listeConstituants
    
    @listeConstituants.setter
    def listeConstituants(self , value) :
        self.__listeConstituants = value

    @property
    def TauxTVA(self):
        return self.tauxTVA

    def __str__(self):
        info = ""
        for i in self.__listeConstituants :
            info = info+ i.__str__()+ "\n"
        
        return info + "Total Price:" + str(self.getPrixHT()) + " DH"

    def getPrixHT(self):
        produitsTotalPrix = 0
        for i in self.__listeConstituants:
            produitsTotalPrix += i.getPrixAchat() * i.quantite
        return self.__fraisFabrication + produitsTotalPrix 

pe1 = produitElementaire("egg","4567",1)
pe2 = produitElementaire("Oil","3456",15)

com1 = composition(pe1,3)
com2 = composition(pe2,5)
 
cakeCompositionList =[com1,com2] 



cakeproduitCompose = produit_compose("cake",10,cakeCompositionList)

# print("[ cake info ] :")
# print(cakeproduitCompose)
print("")

pe3 = produitElementaire("flour","1234",6)
pe4 = produitElementaire("water","2345",3)

com3 = composition(pe3,10)
com4 = composition(pe4,15)

breadcompositionlist = [com3,com4]

breadProduitcompose = produit_compose("bread",19,breadcompositionlist)

# print("")
# print("[ bread info ] :")
# print(breadProduitcompose)
# print("")
print("")
listProduit = [pe1,pe2,cakeproduitCompose]

description = namedtuple('description',['x','y'])
dict= {}
listDescription = defaultdict()
for i in listProduit:
    if type(i) == produitElementaire :
        p = description(str(i),": est un produit elementaire")
    else :
        p = description(str(i),": est un produit compose")

    dict[p[0]] = p[1]
    print(p[0] , p[1])
print("")
# print(dict)
listDescription[p[0]] = p[1]
print("")
# print(listDescription)


for i in listProduit:
    if type(i)==produitElementaire:
        print(i.code)
    else:
        for j in i.listeConstituants:
            print(j.code)