class OneFile:
    pass


class SecondFile(OneFile):
    pass


class Factory:
    one = OneFile()

    two = SecondFile()

    print('my commit')
    print('hello')
    print('hello')
    print('how are you')


a = Factory()
b = SecondFile()
c = OneFile()



