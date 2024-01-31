class Steak:
    def __init__(self):
        self.data = []

    def __repr__(self):
        return f"{self.data}"

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.data) == 0

    def check_brackets(self, arr: str):
        count_open = 0
        count_close = 0

        for item in arr:
            if item == "(":
                count_open += 1
                self.push(item)
            if item == ")":
                count_close += 1
                if self.is_empty():
                    continue
                self.pop()
        if self.is_empty() and count_open == count_close:
            return True
        return False



if __name__=="__main__":
    stack = Steak()
    print(stack.check_brackets("((()))"))
    print(stack.check_brackets("(()()())"))
    print(stack.check_brackets("((())"))
    print(stack.check_brackets("())("))
