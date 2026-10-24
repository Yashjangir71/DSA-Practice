a = {"data": 10, "next": None}
b = {"data": 20, "next": None}
c = {"data": 30, "next": None}
d = {"data": 40, "next": None}

a["next"] = b
b["next"] = c
c["next"] = d
current_node = a
while current_node:
    print(current_node["data"])
    current_node = current_node["next"]