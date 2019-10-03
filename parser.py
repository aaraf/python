import re

class Parser:

    INTERFACE   = 'interface'
    DESCRIPTION = 'description'
    IP_ADDR     = 'ip address'

    @classmethod
    def fromFile(self, fileName):
        return self(fileName)

    def __init__(self, fileName):
        self._fileName = fileName

    def using(self, interfaceName):
        self.interfaceName = interfaceName
        return self

    def parse(self):
        return list(self.__format())
        
    def __format(self):
        for value in self.__buildBlocks():
            formattedBlock = self.__formatBlock(value)
            if formattedBlock:
                yield formattedBlock
            
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

        data = {}
        for attribute in block:
            
            if self.INTERFACE in dict.keys(data) and self.interfaceName != 'all' and self.interfaceName != data[self.INTERFACE]:
                return {}

            if self.INTERFACE in attribute:
                data[self.INTERFACE] = attribute.replace(self.INTERFACE, '').strip()

            elif self.DESCRIPTION in attribute:
                data[self.DESCRIPTION] = attribute.replace(self.DESCRIPTION, '').strip()
            
            elif self.IP_ADDR in attribute:
                ip, netMask = re.findall( r'[0-9]+(?:\.[0-9]+){3}', attribute.replace(self.IP_ADDR, '').strip() )
                data['ip_address'] = ip
                data['net_mask']   = netMask
                
        return data



Parser.fromFile("config.txt").using('all').parse();