class Test:
    def print_text(self):
        print("Это родительский класc Text")

class Test2(Test):
    def print_text(self):
        print("Это дочерний класс Test2")

test2 = Test2()
test2.print_text()