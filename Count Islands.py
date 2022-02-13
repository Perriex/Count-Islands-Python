import sys
sys.setrecursionlimit(10**6)

def ExploreIsland(i,j):
    global contry
    global n ,m
    if i<0 or j<0 or i>=int(n) or j>=int(m):
        return
    if contry[i][j] == 0:
        return
    else:
        contry[i][j] = 0
        ExploreIsland(i+1,j)
        ExploreIsland(i-1,j)
        ExploreIsland(i,j+1)
        ExploreIsland(i,j-1)



n,m = input().split()
contry=[]
for i in range(0,int(n)):  
    contry.append([int(j) for j in input().split()]) 

islandNum =0
for i in range(int(n)):
    for j in range(int(m)):
        if contry[i][j] == 1:
            islandNum +=1
            ExploreIsland(i,j)

print(islandNum)

