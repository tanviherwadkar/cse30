# assignment: programming assignment 4 (Expression Tree)
# author: Tanvi Herwadkar
# date: November 20, 2022
# file: tree.py implements a binary tree with a child class expression tree that
#       creates an expression tree from a postfix expression and evaulates it
# important methods: make_tree(infix): take an infix, returns an ExpTree
#                    evaluate(tree): takes an ExpTree and returns value

from stack import Stack

class BinaryTree:
    def __init__(self, rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s


class ExpTree(BinaryTree):

    def make_tree(postfix):
        operator = set([ "+", "-" , "*" , "/" , "^"])
        stack = Stack()
        for i in postfix:
            if (i not in operator):
                stack.push(ExpTree(i))
            else:
                temp = ExpTree(i)
                temp.rightChild = stack.pop()
                temp.leftChild = stack.pop()
                stack.push(temp)
        return stack.pop()

    def preorder(tree):
        s = ''
        if tree != None:
            s = tree.getRootVal()
            s += ExpTree.preorder(tree.getLeftChild())
            s += ExpTree.preorder(tree.getRightChild())
        return s

    def inorder(tree):
        s = ''
        if tree != None:
            if tree.getLeftChild() == None and tree.getRightChild() == None:
                s += tree.getRootVal()
            else:
                s += "("
                s +=ExpTree.inorder(tree.getLeftChild())
                s += tree.getRootVal()
                s +=ExpTree.inorder(tree.getRightChild())
                s += ")"
        return s

    def postorder(tree):
        s = ''
        if tree != None:
            s += ExpTree.postorder(tree.getLeftChild())
            s += ExpTree.postorder(tree.getRightChild())
            s += tree.getRootVal()
        return s

    def evaluate(tree):
        operator = ["+","-","*","/","^"]
        if tree == None:
            return

        elif type(tree) == str:
            return tree

        else:
            if tree.getRootVal() not in operator:
                return tree.getRootVal()
            else:
                left = ExpTree.evaluate(tree.getLeftChild())
                right = ExpTree.evaluate(tree.getRightChild())
                root = ExpTree.evaluate(tree.getRootVal())

            new_l = float(left)
            new_r = float(right)

            if (root == "+"):
                return new_l+new_r
            elif (root == "-"):
                return new_l - new_r
            elif (root == "*"):
                return new_l*new_r
            elif (root == "/"):
                return new_l/new_r
            elif (root == "^"):
                return new_l**new_r

    def __str__(self):
        return ExpTree.inorder(self)


# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':
    # test a BinaryTree

    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild() == None
    assert r.getRightChild() == None
    assert str(r) == 'a()()'

    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'

    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'

    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'
    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'

    # test an ExpTree
    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'

    print(ExpTree.evaluate(tree))
    assert ExpTree.evaluate(tree) == 11.0
    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    print(ExpTree.evaluate(tree))
    assert ExpTree.evaluate(tree) == 21.0