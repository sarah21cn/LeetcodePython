# Tree

102. Binary Tree Level Order Traversal

     https://leetcode.com/problems/binary-tree-level-order-traversal/

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ret, level = [], [root]
        while level:
            ret.append([node.val for node in level])
            newLevel = []
            for node in level:
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)
            level = newLevel
        return ret
```

