import matplotlib.pyplot as plt 

file = open('ex1data1.txt', 'r')
lines = file.read().splitlines()

x_list = list(map(lambda l: float(l.split(',')[0]), lines))
y_list = list(map(lambda l: float(l.split(',')[1]), lines))

alfa = 0.001
teta0 = 0
teta1 = 1
iteration = 500

xmax = max(x_list)
xmin = min(x_list)
normalizex = []

for x in x_list:
    x1 = (x - xmax) / (xmax - xmin)
    normalizex.append(x1)

ymax = max(y_list)
ymin = min(y_list)
normalizey = []

for y in y_list:
    y1= (y-ymax) / (ymax-ymin)
    normalizey.append(y1)

def hteta(x,teta0,teta1):
    return teta0 + (teta1* x)

def cost(teta0,teta1):
    sum= 0
    for i in range(len(normalizex)):
        sum += (hteta(normalizex[i], teta0,teta1) - normalizey[i] ) ** 2
    return sum * (1/2*(len(normalizex)))

def teta(teta0, teta1):
    sum= 0
    for i in range(len(normalizex)):
        sum += (hteta(normalizex[i],teta0,teta1) - normalizey[i] ) 
    teta0 = teta0 - alfa * (1/(len(normalizex))) * sum  
    
    sum= 0
    for i in range(len(normalizex)):
        sum += (hteta(normalizex[i],teta0,teta1) - normalizey[i] ) * normalizex[i] 
    teta1 = teta1 - alfa * (1/(len(normalizex))) * sum  
    return teta0, teta1 

costs = []
for i in range(iteration): 
    c = cost(teta0,teta1) 
    costs.append(c) 
    teta0, teta1 = teta(teta0, teta1) 

print("teta0: " + str(teta0) + " teta1: " + str(teta1)) 

results = []
for x in normalizex:
    results.append(hteta(x, teta0, teta1))

plt.plot(normalizex, results, color="black")
plt.scatter(normalizex, normalizey)
plt.gca().set_title("Normalized Dataset",fontsize = 14)
plt.show()
plt.plot(range(iteration),costs)
plt.show()