# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.total=0
        def treee(root,flag):
            if flag and root.left==None and root.right==None:
                self.total+=root.val
                return 
            if root.left!=None:
                treee(root.left,True)
            if root.right!=None:
                treee(root.right,False)
        if root==None:
            return 0
        treee(root,False)
        return self.total
        