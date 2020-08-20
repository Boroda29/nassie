import settngs

class Model:
    def save(self):
        settngs.DATA_BASE[self.__class__.__name__.lower()].append(self)


if __name__ == '__main__':
    print(__name__)
