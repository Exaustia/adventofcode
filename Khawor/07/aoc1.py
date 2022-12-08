
class directory():
    
    # parent = None

    def __init__(self,name, parent):
        super().__init__()
        self.size = 0
        self.parent = parent
        self.name = name
        self.children = []

    def addFile(self,size):
        self.size += size
        if(self.parent != None):
            self.parent.addFile(size)
    
    def addDirectory(self, child):
        self.children.append(child)
        return child
    
    def getParent(self):
        return self.parent

    def __str__(self, tabul):
        string = "\n"
        # if(self.size < 100000):
        string = self.name+' '+str(self.size)+"\n"
        tabul += '.'
        if(len(self.children) > 0):
            for child in self.children:
                string+=tabul + child.__str__(tabul)
        return string
    
    def sumUnder(self,sum, max):
        if(self.size<max):
            sum += self.size
            # print(str(sum))
        if(len(self.children) > 0):
            for child in self.children:
                sum = child.sumUnder(sum, max)
        return sum
    
    def closerOf(self, of, value):
        if((self.size - of) > 0) and ((self.size - of) < value):
            value = self.size
            print(value)
        if(len(self.children) > 0):
            for child in self.children:
                value = child.closerOf(of, value)
        return value


if __name__ == '__main__':
    fileSystem = directory("", None)
    currentDir = fileSystem
    f = open("input.txt","r")
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line[0] == '$':
            
            if line[1:5] == " cd ":
                
                if line[5:] != '..':
                    # print("'"+line[5:]+"'")
                    currentDir = currentDir.addDirectory(directory(line[5:], currentDir))
                else:
                    currentDir = currentDir.getParent()
        else:
            if line[:3] != 'dir':
                currentDir.addFile(int(line[:line.find(' ')]))
    
    print(fileSystem.__str__(''))

    # print(str(fileSystem.sumUnder(0, 100000)))
    neededSpace = 30000000
    oF = fileSystem.size- (70000000 - neededSpace) 
    # print(fileSystem.size)
    # print(oF)
    print(str(fileSystem.closerOf(oF,oF*2)))