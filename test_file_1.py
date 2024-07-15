class OneFile:
    pass


class SecondFile(OneFile):
    pass


class FactoryFile:
    pass


class FactoryNotFile:
    pass


b = FactoryFile()
ability = FactoryNotFile()

print('hello world')
print('i am not so busy')
print('new factory')
new_value = 'value string'