from TTL import *

inp('a','b')

NAND('a','b','p1')
NAND('a','p1','p2')
NAND('b','p1','p3')
NAND('p2','p3','c')

out('a','b', 'c')

build()