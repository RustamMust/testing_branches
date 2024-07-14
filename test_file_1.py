class OneFile:
    pass


class SecondFile(OneFile):
    pass


class Factory:
    one = OneFile()

    two = SecondFile()

    print('my commit')


a = Factory()
b = SecondFile()
c = OneFile()



