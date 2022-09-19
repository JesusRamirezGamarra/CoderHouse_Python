# https://www.javatpoint.com/what-is-duck-typing-in-python


class VisualStudio:
    def execute(self):
        print("Compiling")
        print("Running")
        print("Spell Check")
        print("Convention Check")


class Desktop:
    def code(self, ide):
        ide.execute()


ide = VisualStudio()
desk = Desktop()
desk.code(ide)
