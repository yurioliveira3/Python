#Classe pai
class Veiculo: 
    #Construtor de Veiculo
    def __init__(self, name, max_vel, km):
        self.name = name;
        self.max_vel = max_vel;
        self.km = km;

#Classe filho
class Onibus(Veiculo):
    #Construtor do Onibus
    def __init__(self, name, max_vel, km):
        #Chama o construtor do pai para crir o objeto
        super().__init__(name, max_vel, km)

    #Metodo para printar o objeto
    def welcome(self):
        print("CAR:", self.name," MAX VEL:", self.max_vel, "KM:", self.km)

if __name__ == "__main__":
    #Cria o objeto
    T = Onibus("Corsa",45,500);
    
    #Printa 
    T.welcome();
