activities = [
    ["A1",0,6],["A2",3,4],["A3",1,2],["A4",5,8],["A5",5,7],["A6",8,9]
]

coins = [1,2,5,10,15,25,50,100,200,500,1000]

def coinchange(coins, amount):
    coins.sort()
    index = len(coins) - 1
    while True:
        if amount >= coins[index]:
            print(coins[index])
            amount -= coins[index]

        if amount < coins[index]:
            index -= 1

        if amount == 0:
            break

def printMaxAct(activities):
    activities.sort(key = lambda x: x[2])
    i = 0
    first = activities[i][0]
    print(first)
    for j in range(len(activities)):
        if activities[j][1] > activities[i][2]:
            print(activities[j][0])
            i = j

#printMaxAct(activities)
coinchange(coins, 2035)
