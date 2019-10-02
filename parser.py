class Parser:

    @classmethod
    def fromFile(self, fileName):
        return self(fileName)

    def __init__(self, fileName):
        self._fileName = fileName

    def parse(self):
        self.__format()
        
    def __format(self):
        for value in self.__buildBlocks():
            for val in self.__formatBlock(value):
                print(val)
            
    def __buildBlocks(self):
        block = []
        
        with open(self._fileName) as f:
            for line in f:
                if (line.find('!') != -1):
                        yield block
                        block = []
                else:
                    block.append(line.strip())

    def __formatBlock(self, block):
        for attribute in block:
            res = dict()
            if attribute.find('interface') != (-1):
                res.append({interface : 'asdas'})
            
            yield res

Parser.fromFile("config.txt").parse();
