from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def add_item(self, data):
        return self.container.append(data)

    def remove_item(self):
        return self.container.pop()

    def see_last_element(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def get_length(self):
        return len(self.container)


# Below function will check if paranthesis combination matches or not
def is_match(ch1, ch2):
    match_dict = {")": "(", "}": "{", "]": "["}
    return match_dict[ch1] == ch2


# Below function will check the balanced paranthesis
def check_paranthesis_balance(str):
    st = Stack()

    for ch in str:

        # Add in stack in sequence of bracket received
        if ch == "(" or ch == "{" or ch == "[":
            st.add_item(ch)

        # Check the closing tag is balanced or not
        if ch == ")" or ch == "}" or ch == "]":

            # This means stack is empty
            if st.get_length() == 0:
                return False

            # Match the current bracket with popped bracket from stack
            if not is_match(ch, st.remove_item()):
                return False

    return st.get_length() == 0


print(check_paranthesis_balance("({a+b})"))
print(check_paranthesis_balance("))((a+b}{"))
print(check_paranthesis_balance("((a+b))"))
print(check_paranthesis_balance("))"))
print(check_paranthesis_balance("[a+b]*(x+2y)*{gg+kk}"))
