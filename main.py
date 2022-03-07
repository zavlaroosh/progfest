import matplotlib.pyplot as plt

path = r'C:\Users\Utilisateur\Desktop\ulaval\Été 2021\python\Travaux pratiques\tp2_Xavier_Larouche\pythonProject1\AtelierVisualisation\progFest_OOPUnitTests\data/2022-02-30_experiment1.txt'
class EncabulatorData():
    def __init__(self):
        self.fich = open(path,'r')
        self.name = path[-25:]
        self.datay = []
        self.datax = []
        self.metadata = []
    def readfile(self):
        data = open(path,'r')
        if '.csv' in path:
            self.metadata.append(data.readline())
            self.metadata.append(data.readline())
            for lines in data.readlines():
                data = lines.split(self,',')
            for i in data:
                if i % 2 == 0:
                    self.datax.append(i)
                else:
                    self.datay.append(i)

        elif '.txt' in path:
            data = open(path, 'r')
            if path[-3:] == 'txt':
                self.metadata.append(data.readline())
                self.metadata.append(data.readline())
                for lines in data.readlines():
                    data = lines.split(self)
                for i in data:
                    if i % 2 == 0:
                        self.datax.append(i)
                    else:
                        self.datay.append(i)



y = EncabulatorData().readfile().datay
x = EncabulatorData().readfile().datax

plt.plot(x,y)
plt.show()


