print("This program will calculate the distance traveled of a ball based on the initial height and how many times bounced.\n")
newInitialHeight = int(input("What is the starting height: "))
numBounce = int(input("What is the number of bounces?: "))

newTotalDistance = 0
initialNumBounce = numBounce

for count in range(numBounce):
        initialHeight = newInitialHeight
        totalDistance = newTotalDistance
        total = initialHeight * 0.6
        distanceAfterBounce = initialHeight + total
        newTotalDistance = totalDistance + distanceAfterBounce
        newInitialHeight = total
print("\nThe total distance traveled after", initialNumBounce, "bounces is", str(newTotalDistance))
