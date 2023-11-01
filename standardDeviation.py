def calculateMean(data):
    if len(data) == 0:
        return None
    return sum(data) / len(data)

def calculateStandardDeviation(data):
    n = len(data)
    if n < 2:
        return None

    mean = calculateMean(data)

    # Calculate the sum of squared differences
    sumSquaredDiff = sum((x - mean) ** 2 for x in data)

    # Calculate the mean of squared differences
    meanSquaredDiff = sumSquaredDiff / (n - 1)

    # Calculate the standard deviation
    standardDeviation = round((meanSquaredDiff ** 0.5), 2)

    return standardDeviation

# Input numbers from the user
data = []
n = int(input("Enter the number of data points: "))
for i in range(n):
    dataPoint = float(input(f"Enter data point {i + 1}: "))
    data.append(dataPoint)

stdDev = calculateStandardDeviation(data)
print("Standard Deviation:", stdDev)
