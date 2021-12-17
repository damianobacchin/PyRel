from math import sqrt

# Media
def mean(data):
    sum = 0
    for i in data:
        sum += i
    return sum / float(len(data))


# Deviazione standard
def standard_deviation(data):
    sum = 0
    media = mean(data)
    for i in data:
        sum += (i-media)**2
    return sqrt(sum / float(len(data)-1))



# Metodo dei minimi quadrati
def linear_interpolation(data):
    sumX = 0
    sumX2 = 0
    sumY = 0
    sumXY = 0
    for i in range(len(data)):
        sumX += i+1
        sumX2 += (i+1)**2
        sumY += data[i]
        sumXY += data[i]*(i+1)
    
    delta = len(data)*sumX2 - sumX**2
    alfa = (1/delta) * (sumX2*sumY - sumX*sumXY)
    beta = (1/delta) * (len(data)*sumXY - sumX*sumY)
    
    sumSy = 0
    for i in range(len(data)):
        sumSy += (data[i]-alfa-beta*i)**2
    sigmaY = sqrt( (1/(len(data)-2)) * sumSy )
    sigmaAlfa = sigmaY * sqrt((1/delta)*sumX2)
    sigmaBeta = sigmaY * sqrt(len(data)/delta)

    return (alfa, beta, sigmaAlfa, sigmaBeta)


# Metodo minimi quadrati con errori Sigma y
def linear_interpolation2(data):
    sigmaI = standard_deviation(data)
    sigmaI2 = pow(sigmaI, 2)
    sumX = 0
    sumX2 = 0
    sumY = 0
    sumXY = 0
    for i in range(len(data)):
        sumX += i/sigmaI2
        sumX2 += pow(i, 2)/sigmaI2
        sumY += data[i] / sigmaI2
        sumXY += (data[i]*i) / sigmaI2
    delta = (1/sigmaI2)*len(data) * sumX2 - sumX**2
    alfa = (1/delta) * (sumX2*sumY - sumX*sumXY)
    beta = (1/delta) * ((1/pow(sigmaI, 2))*len(data)*sumXY - sumX*sumY)
    sigmaAlfa = sqrt((1/delta) * sumX2)
    sigmaBeta = sqrt((1/delta) * (1/sigmaI2) * len(data))
    return (alfa, beta, sigmaAlfa, sigmaBeta)



# Criterio di Chauvenet (ritorna il numero di deviazioni standard)
def chauvenet(data, suspect):
    sd = standard_deviation(data)
    media = mean(data)
    numSD = abs(suspect-media) / sd
    return numSD



# READ FILE DATA
data = []
file = open('dati_triangoli.csv', 'r')
for line in file.readlines():
    data.append(float(line))

print(f'Media: {mean(data)}')
print(f'Deviazione standard: {standard_deviation(data)}')
print(f'Interpolazione I: {linear_interpolation(data)}')
print(f'Interpolazione II: {linear_interpolation2(data)}')
print(f'Chauvenet: {chauvenet(data, 10.3)}')