import random
empty = 0
cols =51
rows = 51
array = []
v_walls =[]

def fillEmptyValue():
    for i in range(cols):
        array.append(0)

def assignUniqueSet():
    k = 0
    for i in range(cols):
        if (array[i] == empty):
            array[i] = k
            k += 1


def mergeSet(index, element):
    mutableSet = array[index + 1]
    for i in range(cols):
        if array[i] == mutableSet:
            array[i] = element

def addingVerticalWalls(row):
    for i in range(cols-1):
        choise=random.choice([True, False])
        if (choise == True) or (array[i]==array[i+1]):
            v_walls[row][i] = True
        else:
            mergeSet(i,array[i])
    v_walls[row][cols - 1] = True

def calculateUniqueSet(element):
    countUniqSet = 0
    for i in range(cols):
        if (array[i]==element):
            countUniqSet+=1
    return countUniqSet

def addingHorizontalWalls(row):
    for i in range(cols):
        choise = random.choice([True, False])
        if calculateUniqueSet(array[i]!= 1) and choise == True:
            h_wals[row][i] = True

def checkedHorizontalWalls(row):
    for i in range(cols):
        if calculateHorizontalWalls(sideLine_[i], row) == 0:
            h_wals[row][i] = False

def calculateHorizontalWalls(element, row):
    countHorizontalWalls = 0
    for i in range(cols):
        if array[i] == element and h_walls[rows][i]==False:
            countHorizontalWalls+=1
    return countHorizontalWalls

def addingEndLine():
    assignUniqueSet()
    addingVerticalWalls(rows_ - 1)
    checkedEndLine()

def checkedEndLine():
    for i in range(cols-1):
        if (array[i] != array[i+1]):
            v_walls_[rows - 1][i] = False
            mergeSet(i,array[i])
        h_walls[rows-1][i] = True
    h_walls[rows-1][i-1] = True

def generateMaze():
    fillEmptyValue()
    for j in range(rows-1):
        assignUniqueSet()
        addingVerticalWalls(j)
        addingHorizontalWalls(j)
        checkedHorizontalWalls(j)
        preparatingNewLine(j)
    addingEndLine()

generateMaze()