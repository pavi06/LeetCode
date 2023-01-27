# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.totalsum=0
        def sumroot(root,val):
            if not root:
                return 
            val=(val*10)+root.val  #to consider it as a number
            if root.left==None and root.right==None:
                self.totalsum+=val
            sumroot(root.left,val)  #each node is called with val 
            sumroot(root.right,val)
        sumroot(root,0)
        return self.totalsum
            
        