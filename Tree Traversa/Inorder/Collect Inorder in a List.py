result = []

def inorder(node):
    if node is None:
        return
    inorder(node["left"])
    result.append(node["data"])
    inorder(node["right"])

root = {"data": 2,
        "left": {"data": 1, "left": None, "right": None},
        "right": {"data": 3, "left": None, "right": None}}
inorder(root)
print(result)  # [1, 2, 3]
