# iterator is an  object a countable number object 


# iter() list , tuple set , dict can either keys or values str

# name_string = "swetha"
# iterator_object = iter(name_string)
# print(iterator_object)
# print(next(iterator_object))
# print(next(iterator_object))
# print(next(iterator_object))
# print(next(iterator_object))
# print(next(iterator_object))
# print(next(iterator_object))

# tuple_string = ("suray","teja","swetha")
# iterator_object = iter(tuple_string)
# print(next(iterator_object))
# print(next(iterator_object))
# print(next(iterator_object))

# for string in tuple_string:
#     print(string)
    

class Name:
    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        names = ["surya", "teja", "swetha"]
        if self.index < len(names):
            name = names[self.index]
            self.index += 1
            return name
        else:
            raise StopIteration
name = Name()
name_iterator = iter(name)
print(next(name_iterator))
print(next(name_iterator))
print(next(name_iterator))
print(next(name_iterator))