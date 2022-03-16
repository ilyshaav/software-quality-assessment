
class Compressor:
    def __init__(self):
        pass

    def checkLen(string):
        if len(string) <31:
            return True
        else:
            return False

    def textCompression(string):
        string+="\n"
        count = 0
        strBuf =""
        for i in range(len(string)-1):
            count +=1
            if string[i] != string[i+1] :
                strBuf += str(count) + string[i]
                count = 0
        return strBuf


