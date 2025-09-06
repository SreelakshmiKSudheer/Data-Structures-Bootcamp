def truckTour(petrolpumps):
    # Write your code here
    totalFuel = 0
    currentFuel = 0
    start = 0
    
    for i in range(len(petrolpumps)):
        fuel = petrolpumps[i][0] - petrolpumps[i][1]
        totalFuel += fuel
        currentFuel += fuel

        if currentFuel < 0:
            start = i+1
            currentFuel = 0
            
    if totalFuel >= 0:
        return start