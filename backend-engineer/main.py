from Organize import Organize
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        file_name = input("Please provide file name: ")
    else:
        file_name = sys.argv[1]
    try:
        f = open(file_name, 'r')
        lines = f.readlines()
        container = Organize()
        for line in lines:
            container.insert(line.strip())
        container.txt_fileGenerator()
        f.close()
    except OSError:
        print('cannot open', file_name)