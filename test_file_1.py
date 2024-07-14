class OneFile:
    pass


class SecondFile(OneFile):
    pass


class Factory:
    one = OneFile()

    two = SecondFile()


a = Factory()
b = SecondFile()
c = OneFile()



