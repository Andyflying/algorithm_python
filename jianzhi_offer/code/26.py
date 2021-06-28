# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bl(self, A, B):
        if A and B:
            if A.val == B.val:
                return self.bl(A.left, B.left) and self.bl(A.right, B.right)
            else:
                return False
        elif B:
            return False
        else:
            return True
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return False
        if A:
            return self.bl(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
        else:
            return False

        