# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:50:43 2019

@author: Administrator
"""

class Node:
    def __init__(self,weight):
        self.weight = weight
        self.isin = False
        self.left = None
        self.right = None
        self.parent = None

class HuffmanTree:
    def __init__(self,weightList):
        self.weightList = weightList
        self.HL = []
        HuffmanTree.create(self)
        HuffmanTree.printitem(self)
    
    def create(self):
        m=len(self.weightList)
        n= 2*m-1
        for i in range(n):
            self.HL.append(Node(float('inf')))
            self.HL[-1].left = 0
            self.HL[-1].right = 0
            self.HL[-1].parent = 0
        for i in range(m):
            self.HL[i].weight = self.weightList[i]
        for i in range(m,n):
            min1 = n-1
            min2 = n-1
            for j in range(i):
                if self.HL[j].weight < self.HL[min1].weight and self.HL[j].isin  == False:
                    min2 = min1
                    min1 = j
                elif self.HL[j].weight < self.HL[min2].weight and self.HL[j].isin  == False:
                    min2 = j
            self.HL[min1].parent = i
            self.HL[min1].isin =True
            self.HL[min2].parent = i
            self.HL[min2].isin =True
            self.HL[i].left = min1
            self.HL[i].right = min2
            self.HL[i].weight = self.HL[min1].weight + self.HL[min2].weight
    def printitem(self):
        HuffmanTree.create(self)
        for i in range(2*len(self.weightList)-1):
            print('HL[',i,'].weight=',self.HL[i].weight)
            print('HL[',i,'].parent=',self.HL[i].parent)
            print('HL[',i,'].left=',self.HL[i].left)
            print('HL[',i,'].right=',self.HL[i].right)
            print()
            
                
h_weight = [9,4,1,3,7,8,2,6]
t = HuffmanTree(h_weight)
#t.printitem()

