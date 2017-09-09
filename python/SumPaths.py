#!/usr/bin/env python

import unittest
import math

class TestSumPaths(unittest.TestCase):

  def testSanity(self):
    n1 = Node(value=1)
    self.assertEqual(n1.sumPaths(), 1)

  def testEasy1(self):
    n1 = Node(value=1, left=Node(value=1))
    self.assertEqual(n1.sumPaths(), 11)

  def testEasy2(self):
    n1 = Node(value=1, left=Node(value=1), right=Node(value=1))
    self.assertEqual(n1.sumPaths(), 22)

  def testAristaExample(self): 
    n1 = self.makeTreeA()
    self.assertEqual(n1.sumPaths(), 1637)

  def test202Example(self): 
    n1 = self.makeTreeB()
    self.assertEqual(n1.sumPaths(), 202)

  def testExampleC(self): 
    n1 = self.makeTreeC()
    self.assertEqual(n1.sumPaths(), 429)
  
  def makeTreeA(self): 
    return Node(1, Node(4, Node(3), Node(7, Node(9))), Node(5))

  def makeTreeB(self): 
    return Node(2, Node(0, Node(2)))

  def makeTreeC(self): 
    #24 + 202 + 203 = 429
    return Node(2, Node(0, Node(2), Node(3)), Node(4))





  # Write some more test cases

class Node:
  def __init__(self, value=0, left=None, right=None):
    self.left = left
    self.right = right
    self.value = value

  def sumPaths(self):
    lst = self.helper()
    total = 0 
    for i in lst: 
      total = total + i[0]
    return total 



  def helper(self):
    if not self.left:
      left = []
    else: 
      left = self.left.helper()

    if not self.right: 
      right = []
    else: 
      right = self.right.helper()

    returnList = left + right

    if not returnList: 
      return [(self.value, 1)]

    for i in range(len(returnList)): 
      power = returnList[i][1]
      returnList[i] = (self.value*(10**power) + returnList[i][0], power + 1)
    return returnList








if __name__ == "__main__":
  unittest.main()

