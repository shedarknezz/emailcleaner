import argparse 
'''
Created on 1 Feb 2017

@author: MeowStudios 
'''

class loader:
    

    def __init__(self,args=None):
        parser = argparse.ArgumentParser()
        parser.add_argument("sourcefile", type=argparse.FileType('r'), help="source file for operation chain")
        parser.add_argument("-o", "--outputnamebase", dest='filenameportion', help="intermediate and final output files will use this as unique portion of file name")
        parser.add_argument("-x", "--extractemails", action="store_true", help="eXtract emails form file")
        self.args=parser.parse_args();
        
    def set_data(self,args):
        self.args = args;

    
    def get_data(self):
        return self.args;     