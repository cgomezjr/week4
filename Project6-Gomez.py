print("This program will calculate for pi based on the number of iterations")
numIterations = int(input("Input the number of iterations: "))

denominator = 1
total = 1

for count in range(numIterations):
        denominator = denominator + 2
        total = total - (1/denominator)
        denominator = denominator + 2
        total = total + (1/denominator)
        
pi = total * 4	
print("pi =",pi)
