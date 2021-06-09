# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        head = TreeNode(preorder[0])
        idx = 0
        while inorder[idx] != preorder[0]:
            idx += 1
        head.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        head.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return head