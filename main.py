
from calendar import month
from fcntl import DN_DELETE
from traceback import print_exception


def calculateNetworkHashRate(t:int):
     return int(73.91*t + 860)

def calculateEthExchangeRate(t:int):
    return (3264 - 115.6*t + 11.81*(t*t))

class Hardware:

#the below definition of my class variables doesn't let me create an object without also defining the 4 positional arguments
#why?

#    def __init__ (self, name, powerDraw, price, hashRate):
#        self.name = name
#        self.powerDraw = powerDraw
#        self.price = price
#        self.hashRate = hashRate

#trying a different method
#this works, but I have to predefine the value of my variables in the class constructor

#in C++, I could create class attributes that I didn't have to define if I didn't want to. Can I do that in Python?
    name = "name"
    powerDraw = 0
    price = 0
    hashRate = 0


#driver code

GPU = Hardware()
#opening specs file
with open ("GPUspecs.txt") as specs:

    fileDict = {}

    for line in specs.readlines():
        data = line.split()

#        GPU.data[0] = data[1]
#Is there any way to make that line work? I'm pretty sure I could stack classes and variables like that in C++
#        print(f'{data[0]} {data[1]}')


#this is a stupid, but it lets me mess around with dictionaries as a built in type
        fileDict[data[0]] = data[1]

#now we have a dictionary that holds (key, value) pairs for our attribute definitions
#search the dict and add the value to the corresponding attribute for the GPU object
GPU.name = fileDict['name']
GPU.powerDraw = fileDict['powerDraw']
GPU.price = fileDict['price']
GPU.hashRate = fileDict['hashRate']

#use the power draw of the GPU to calculate the cost of electricity in a month, assuming cost = $.10 kwh
monthElectricCost = 30*(int(GPU.powerDraw))*24/1000*.10

compoundProfit = 0
for t in range(2, 38):
#this is python's version of C++'s "for (int i=2; i <=38; i++) {}", right?    
    networkHashRate = calculateNetworkHashRate(t)
#    print(networkHashRate)
    EthExchangeRate = calculateEthExchangeRate(t)
#    print(EthExchangeRate)
#calculate your ROI for month t with 2 of these GPUs
    monthProfit = 30*2.25*5760*(int(GPU.hashRate)*2/int(networkHashRate)/1000000)*EthExchangeRate - monthElectricCost
#    print (f'30 * 2 * 5760 * {GPU.hashRate} * 2 / {networkHashRate} / 10^6 * 4000 - {monthElectricCost}')
#30 days in a month
# 2 eth per block, plus some gas and transaction fees 
#5760 blocks per day
#your percent contribution to the network
#the value of the Eth you mined in dollars
#minus your cost of electricity (nts: Claire should talk to Tom about electricity cost)
    compoundProfit = compoundProfit + monthProfit
    with open ("monthlyROI.csv", "a") as monthlyROI:
        monthlyROI.write(f'{t}, {monthProfit} \n')
    with open ("compoundROI.csv", "a") as compoundROI:
        compoundROI.write(f'{t}, {compoundProfit} \n')