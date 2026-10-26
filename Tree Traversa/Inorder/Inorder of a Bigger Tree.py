def inorder(node):
    if node is None:
        return
    inorder(node["left"])
    print(node["data"])
    inorder(node["right"])

root = {"data": 4,
        "left": {"data": 2,
                 "left": {"data": 1, "left": None, "right": None},
                 "right": {"data": 3, "left": None, "right": None}},
        "right": {"data": 6,
                  "left": {"data": 5, "left": None, "right": None},
                  "right": {"data": 7, "left": None, "right": None}}}
inorder(root)  # prints 1, 2, 3, 4, 5, 6, 7
