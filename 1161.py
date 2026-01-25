from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    for i in range(len(values)):
        if nodes[i] is not None:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(nodes):
                nodes[i].left = nodes[left_idx]
            if right_idx < len(nodes):
                nodes[i].right = nodes[right_idx]
    return nodes[0]

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # Используем обычный список вместо deque (pop(0) — медленно, но работает)
        q = [root]
        print(q)
        best_level = 1
        max_sum = float('-inf')
        level = 1

        while q:
            level_size = len(q)
            cur_sum = 0
            # Обрабатываем все узлы текущего уровня
            for _ in range(level_size):
                node = q.pop(0)  # из начала списка
                cur_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # Обновляем лучший уровень
            if cur_sum > max_sum:
                max_sum = cur_sum
                best_level = level
            level += 1
        return best_level

# === ТЕСТ ===
data = [1, 7, 0, 7, -8, None, None]
root = build_tree_from_list(data)
print(root)
solution = Solution()
print(solution.maxLevelSum(root))  # Выведет: 2
a1=[1,2,3]
a2=[1,3,2]
if tuple(a1)==tuple(a2):
    print(True)