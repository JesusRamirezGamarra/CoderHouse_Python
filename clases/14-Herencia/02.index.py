class TheHobbit:
    def __len__(self):
        return 95022


the_hobbit = TheHobbit()
the_hobbit  # <__main__.TheHobbit object at 0x108deeef0>
len(the_hobbit)  # 95022
my_str = "Hello World"
my_list = [34, 54, 65, 78]
my_dict = {"one": 123, "two": 456, "three": 789}
len(my_str)  # 11
len(my_list)  # 4
len(my_dict)  # 3
len(the_hobbit)  # 95022

my_int = 7
my_float = 42.3

#len(my_int)     # Traceback (most recent call last):  File "<input>", line 1, in <module>
#len(my_int)     # TypeError: object of type 'int' has no len()
#len(my_float)   # Traceback (most recent call last):  File "<input>", line 1, in <module>
#len(my_float)   # TypeError: object of type 'float' has no len()
