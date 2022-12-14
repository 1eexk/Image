import struct
import sys
import os 
 
align_mask = 8 * 1024 -1

# main body
if sys.argv.__len__() > 1:
    src1_file = sys.argv[1]
else:
    print('Please input 1 files and try again.\n')
    exit(1);
 
if not os.path.exists(src1_file):
    print(src1_file,'not exist!')
    exit(1)

dst_file = src1_file + 'aligned'

try:
    s1f = open(src1_file, "rb")
    df = open(dst_file, "wb")
    contents = s1f.read()
    s1f.seek(0,0)
    s1f.seek(0,2)
    length = s1f.tell()
    print("file len:",length)
    df.write(contents)
    cat_len = (length & align_mask)
    cat_len = align_mask - cat_len + 1
    print("cat_len:",cat_len)
    df.write(b'\0'*cat_len)
finally:
    if s1f:
        s1f.close()
    if df:
        df.close()
print("aligned Completed!")
