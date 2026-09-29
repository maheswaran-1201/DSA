class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def create():
    root=TreeNode('1')
    nodeA=TreeNode('2')
    nodeB=TreeNode('3')
    nodeC=TreeNode('4')
    nodeD=TreeNode('5')
    nodeE=TreeNode('6')
    nodeF=TreeNode('7')
    nodeG=TreeNode('8')
    nodeH=TreeNode('9')
    nodeI=TreeNode('10')


    root.left=nodeA
    root.right=nodeB

    nodeA.left=nodeC
    nodeA.right=nodeD

    nodeD.left=nodeG

    nodeB.left=nodeE
    nodeB.right=nodeF

    nodeF.left=nodeH
    nodeF.right=nodeI

    print("binary tree created succesfully")
    

    
def PreOrderTraversal(node):
    if node is None:
        return
    print(node.data,end=" ")
    PreOrderTraversal(node.left)
    PreOrderTraversal(node.right)

def InOrderTraversal(node):
    if node is None:
        return
    InOrderTraversal(node.left)
    print(node.data,end=" ")
    InOrderTraversal(node.right)

def PostOrderTraversal(node):
    if node is None:
        return
    PostOrderTraversal(node.left)
    PostOrderTraversal(node.right)
    print(node.data,end=" ")


while True:
    print("1.create")
    print("2.preorder traversal")
    print("3.inorder traversal")
    print("4.postorder traversal")
    print("5.exit")

    ch=int(input("enter the choice"))

    if ch==1:
        create()
    elif ch==2:
        PreOrderTraversal(root)
    elif ch==3:
        InOrderTraversal(root)
    elif ch==4:
        PostOrderTraversal(root)
    elif ch==5:
        break
    else:
        print("invalid choice")

    
    
