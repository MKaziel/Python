import sys
import os

class file_handling :

    def __init__(self):
        pass
    
    def creator(self, filename):
        if not os.path.exists(filename):
            file = open(filename, "a")
            return file
        elif os.path.exists(filename):
            file = open(filename, "r+")
            if file.read():
                raise ValueError("Le fichier existe avec du contenu")
            else :
                file.write("old")
                return file
        return -1

    
    def writer(self, opened_file, data):
        length = 0
        opened_file.seek(0)
        if isinstance(data,list):
            for my_str in data:
                if isinstance(my_str,str):
                    opened_file.write(my_str)
                    length += len(my_str)
        elif isinstance(data, str):
            opened_file.write(data)
            length = len(data)

        return length
    
    
    def closer(self, opened_file):
        opened_file.close()
        return opened_file
    

