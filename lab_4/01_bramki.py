# demonstracja dzialania podstawowych bramek logicznych

from TTL import *

inp('a','b')

AND('a','b','and')
NAND('1','b','nand')
OR('a','b','or')
NOR('a','b','nor')
XOR('a','b','xor')
XNOR('a','b','xnor')

out('a','b','and','nand','or','nor','xor','xnor')

build()

