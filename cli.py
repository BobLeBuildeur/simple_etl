import sys
from src.parser import process
from src.util import read

if __name__ == "__main__":
	
	if len(sys.argv) < 2:
		raise ValueError('No filename')
		
	process(read(sys.argv[1]))
