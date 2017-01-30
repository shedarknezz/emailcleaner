import argparse 

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("sourcefile",type=argparse.FileType('r'), help="source file for operation chain")
    parser.add_argument("-o","--outputnamebase", dest='filenameportion',help="intermediate and final output files will use this as unique portion of file name")
    parser.add_argument("-x","--extractemails",action="store_true", help="eXtract emails form file")

    
    args=parser.parse_args()
    
    print(args.sourcefile)
    print(args.filenameportion)
    print(args.extractemails)
    