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


# Metodo minimi quadrati doppi dati
def linear_interpolation3(dataX, dataY):
    sumX = 0
    sumX2 = 0
    sumY = 0
    sumXY = 0
    for i in range(len(dataX)):
        sumX += dataX[i]
        sumX2 += pow(dataX[i], 2)
        sumY += dataY[i]
        sumXY += dataX[i]*dataY[i]
    
    delta = len(dataX)*sumX2 - pow(sumX, 2)
    alfa = (1/delta) * (sumX2*sumY - sumX*sumXY)
    beta = (1/delta) * (len(dataX)*sumXY - sumX*sumY)

    sumSigmaY = 0
    for i in range(len(dataX)):
        sumSigmaY += pow(dataY[i]-alfa-beta*dataX[i], 2)
    sigmaY = sqrt( (1/len(dataX)) * sumSigmaY )
    sigmaAlfa = sigmaY * sqrt( (1/delta)*sumX2 )
    sigmaBeta = sigmaY * sqrt( len(dataX) / delta )

    return alfa, beta, sigmaAlfa, sigmaBeta


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






# Calcolo Xmin e Xmax
def outliers(data):
    Xmin = min(data)
    Xmax = max(data)
    return (Xmin, Xmax)


# Criterio di Chauvenet (ritorna il numero di deviazioni standard)
def chauvenet(data, suspect):
    sd = standard_deviation(data)
    media = mean(data)
    numSD = abs(suspect-media) / sd
    return numSD


# Istogramma di frequenza
def istogramma(data, range):
    count = 0
    for elem in data:
        if range[0]<elem<range[1]:
            count += 1
    return count

def tsigma(media, sd, value):
    return abs(media-value)/sd


def testChi2(grad, ok, ek):
    sum = 0
    for i in range(len(ok)):
        sum += ( (ok[i]-ek[i])**2 ) / ek[i]
    return (1/grad)*sum


# Coefficiente di correlazione lineare
def correlazione(dataX, dataY):
    mediaX = mean(dataX)
    mediaY = mean(dataY)
    sumNum = 0
    sumDenX = 0
    sumDenY = 0
    for i in range(len(dataX)):
        sumNum += (dataX[i]-mediaX) * (dataY[i]-mediaY)
        sumDenX += pow(dataX[i]-mediaX, 2)
        sumDenY += pow(dataY[i]-mediaY, 2)
    return sumNum / sqrt(sumDenX*sumDenY)



# READ FILE DATA
'''
data = []
file = open('pendolonooutliers.csv', 'r')
for line in file.readlines():
    data.append(float(line))
'''

dataX =[1.525, 32.465, 64.425, 97.585, 131.835, 167.415, 205.035, 244.78, 285.975, 331.795, 379.235, 430.795, 487.555, 551.715, 627.165, 720.51, 859.845]
dataY = [2.06, 2.0074, 1.93329, 1.86445, 1.81071, 1.70905, 1.62356, 1.54758, 1.44441, 1.36888, 1.29018, 1.165711, 1.063145, 0.91994, 0.77284, 0.608836, 0.37201]


print(f'Indice di correlazione lineare: {correlazione(dataX, dataY)}')
print(linear_interpolation3(dataX, dataY))
'''
print(f'Media: {mean(data)}')
print(f'Deviazione standard: {standard_deviation(data)}')
print(f'Interpolazione I: {linear_interpolation(data)}')
print(f'Interpolazione II: {linear_interpolation2(data)}')
print(f'Valore MIN: {outliers(data)[0]}')
print(f'Valore MAX: {outliers(data)[1]}')
print(f'Chauvenet valore MIN: {chauvenet(data, outliers(data)[0])}')
print(f'Chauvenet valore MAX: {chauvenet(data, outliers(data)[1])}')
'''

'''
print(f'Media: {mean(data)} | Deviazione standard: {standard_deviation(data)}')
print(f'Minimo: {min(data)} | Massimo: {max(data)}')
print(f'Numero dati totale: {len(data)}')

intervals = [
    (1.9589, 1.9761),
    (1.9761, 1.9932),
    (1.9932, 2.0104),
    (2.0104, 2.0275),
    (2.0275, 2.0447),
    (2.0447, 2.0618),
    (2.0618, 2.079),
    (2.079, 2.0961),
    (2.0961, 2.1133),
    (2.1133, 2.1304)
]

for interval in intervals:
    print(f'Intervallo: {interval} -> Numero dati osservati: {istogramma(data, interval)}')
'''
