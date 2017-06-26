import sys

f = open(sys.argv[1])
con = f.read()
list1 = list(con)

for each_byte in list1:
    sys.stdout.write(format(ord(each_byte),'08b'))
