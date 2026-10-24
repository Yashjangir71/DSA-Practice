a = {"data": 10, "next": None}
b = {"data": 20, "next": None}
c = {"data": 30, "next": None}

a["next"] = b
b["next"] = c
current_node = a
count = 0
while current_node:
    count += 1
    current_node = current_node["next"]
print(count)
