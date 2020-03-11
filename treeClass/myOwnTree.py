# coding=utf-8
class BinaryTree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.indexInHeap=None
    def getIndexHeap(self):
        return self.indexInHeap
    def setIndexHeap(self,value):
        self.indexInHeap=value
    def insertLeft(self,newNode):
        if self.left==None:
            self.left=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.left=self.left
            self.left=t
    def insertRight(self,newNode):
        if self.right==None:
            self.right=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.right=self.right
            self.right=t
    def getValue(self):
        return self.value
    def setValue(self,value):
        self.value=value
    def getRightChild(self):
        return self.right
    def getLeftChild(self):
        return self.left