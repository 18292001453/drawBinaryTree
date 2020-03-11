# coding=utf-8
import matplotlib.pyplot as plt
from  treeClass import myOwnTree
def getNumberOfLeafs(tree):
    leafNumber = 0
    if tree:
        if  not tree.getRightChild() and not tree.getLeftChild():
            leafNumber+=1
        else:
            leafNumber+=getNumberOfLeafs(tree.getLeftChild())
            leafNumber += getNumberOfLeafs(tree.getRightChild())
    return leafNumber
def getDeepOfTree(tree):
    maxDeep=0
    if tree:
        maxLeft=getDeepOfTree(tree.getLeftChild())
        maxRight=getDeepOfTree(tree.getRightChild())
        if maxLeft>maxRight:
            maxDeep=maxLeft
            return 1+maxLeft
        else:
            maxDeep=maxRight
            return 1+maxRight
    return maxDeep

def printTreePre(tree):
    if tree:
        print(tree.getValue())
        printTreePre(tree.getLeftChild())
        printTreePre(tree.getRightChild())
def getDuiIndex(tree):
    if tree:
        if tree.getLeftChild():
            tree.getLeftChild().setIndexHeap(2*tree.getIndexHeap())
        if tree.getRightChild():
            tree.getRightChild().setIndexHeap(2 * tree.getIndexHeap()+1)
        getDuiIndex(tree.getLeftChild())
        getDuiIndex(tree.getRightChild())
def getDuiHelp(list,tree):
    if tree:
        list[tree.getIndexHeap()]=tree.getValue()
        getDuiHelp(list,tree.getLeftChild())
        getDuiHelp(list,tree.getRightChild())
    return list
def getDuiList(tree):
    getDuiIndex(tree)
    h=getDeepOfTree(tree)
    res=[None for i in range(2**h-1)]
    res.insert(0,0)

    return getDuiHelp(res,tree)
def drawBinaryTree(r,nodeType=dict(boxstyle="round", fc=(1.0, 0.7, 0.7), ec="none")):

    fig = plt.figure(1, facecolor="white")
    fig.clf()
    ax1 = plt.subplot(111, frameon=False)
    h = getDeepOfTree(r)
    if h==1:
        ax1.annotate(r.getValue(), va="center", ha="center", xy=(0.5,0.5), bbox=nodeType)
        return None
    w = getNumberOfLeafs(r)
    detH = 1 / (h - 1)
    yAxis = []
    startY = 0
    while startY <= 1:
        yAxis.append(startY)
        startY += detH
    allLeafs = 2 ** (h - 1)
    detX = 1 / (allLeafs - 1)
    leafPos = []
    startX = 0
    while startX <= 1:
        leafPos.append(startX)
        startX += detX
    allXList = []
    while len(leafPos) >= 1:
        allXList.append(leafPos)
        tempList = []
        i = 0
        while i < len(leafPos) - 1:
            tempList.append((leafPos[i] + leafPos[i + 1]) / 2)
            i += 2
        leafPos = tempList
    allXList = allXList[::-1]
    finPos = []
    for xList, y in zip(allXList, yAxis[::-1]):
        for item in xList:
            finPos.append([item, y])
    finPos.insert(0, 0)

    r.setIndexHeap(1)
    duiListForR = getDuiList(r)

    for i in range(1, len(duiListForR)):
        if duiListForR[i]:

            if 2*i<len(duiListForR) and duiListForR[2*i]:
                ax1.annotate("", xy=(finPos[i][0], finPos[i][1]),xytext=(finPos[2*i][0],finPos[2*i][1]),va="center", ha="center",bbox=nodeType,arrowprops=dict(arrowstyle="<-"))##画出这个点
            if 2*i+1<len(duiListForR) and duiListForR[2*i+1]:
                ax1.annotate("", xy=(finPos[i][0], finPos[i][1]),xytext=(finPos[2*i+1][0],finPos[2*i+1][1]),va="center", ha="center",bbox=nodeType,arrowprops=dict(arrowstyle="<-"))##画出这个点
    for i in range(1, len(duiListForR)):
        if duiListForR[i]:
            ax1.annotate(duiListForR[i],va="center", ha="center",xy= (finPos[i][0], finPos[i][1]),bbox=nodeType)##画出这个点
    plt.show()

if __name__ == '__main__':
    r = myOwnTree.BinaryTree("a")
    r.insertLeft("b")
    r.insertRight("c")
    r.getRightChild().insertLeft("d")
    r.getRightChild().getLeftChild().insertRight("g")
    r.getLeftChild().insertRight("f")
    r.getLeftChild().insertLeft("h")
    r.getLeftChild().getLeftChild().insertLeft("i")
    r.getLeftChild().getLeftChild().insertRight("k")
    r.getLeftChild().getLeftChild().getLeftChild().insertRight("l")
    r.getLeftChild().getLeftChild().getLeftChild().insertLeft("m")

    leafNod=dict(boxstyle="round", fc=(1.0, 0.7, 0.7), ec="none")
    drawBinaryTree(r,leafNod)













