###使用方法
~~~python
#首先导入binaryView
import drawPicture.viewBinaryTree as binaryView
#随后通过包中的类myQwnTree构建二叉树
from treeClass import myOwnTree
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
~~~
~~~python
#最终图是通过这句话显示出来的
leafNod=dict(boxstyle="round", fc=(1.0, 0.7, 0.7), ec="none")
binaryView.drawBinaryTree(r,leafNod)
~~~