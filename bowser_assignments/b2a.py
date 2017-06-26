#!/usr/bin/env python
import sys
byte_arr = []
byte = result = ""
for line in sys.stdin:
        length = len(str(line)) - 1
        if length % 8 == 0:
                for a in line:
                        if len(byte) < 8:
                                byte += a
                        else:
                                byte_arr.append(byte)
                                byte = a
        elif length % 7 == 0:
                for a in line:
                        if len(byte) < 7:
                                byte += a
                        else:
                                byte_arr.append("0" + byte)
                                byte = a
        for each_byte in byte_arr:
                result += chr(int(each_byte,2))
        print result
        byte = result = ""
        byte_arr = []

