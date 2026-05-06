from inspect import stack

def is_valid(s):
    stack = []
    mapping = {'(': ')', '{': '}', '[': ']'}

    for char in s:
        if char in mapping.keys():
            stack.append(char)

        elif char in mapping.values():
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack) == 0

s = input("enter string : ")

if is_valid(s):
    print("valid")
else:
    print("Invalid")