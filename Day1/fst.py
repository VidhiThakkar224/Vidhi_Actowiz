s = input("Enter String : ")
stack = []
mapping = {"(" : ")", "{" : "}", "[" : "]"}
valid = True

for char in s:
    if char in mapping.keys():
        stack.append(char)
    elif char in mapping.values():
        if not stack:  # no opening bracket in stack
            valid = False
            break
        top = stack.pop()
        if mapping[top] != char:  # mismatched brackets
            valid = False
            break

# if stack is not empty, extra opening brackets remain
if stack:
    valid = False

if valid:
    print("Valid")
else:
    print("Invalid")
