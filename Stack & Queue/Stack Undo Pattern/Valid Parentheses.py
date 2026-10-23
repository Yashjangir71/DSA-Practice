s = "()[]{}"
stack = []
valid = True
pairs = {")": "(", "]": "[", "}": "{"}   # each closer → its opener
for ch in s:
    if ch in "([{":
        stack.append(ch)
    else:
        if not stack or stack.pop() != pairs[ch]:
            valid = False
            break
if stack:
    valid = False
print(valid)  # True