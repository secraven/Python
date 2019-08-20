import zipfile
import itertools

zf = zipfile.ZipFile('c:\\bin\\myfile.zip')
#print(zf.namelist())

dict = []
chrs = 'abcde12345'
min_length, max_length = 6, 6   
for n in range(min_length, max_length+1):
    for xs in itertools.product(chrs, repeat=n):
        dict.append(''.join(xs))
# print(dict)

outF = open("c:\\bin\\myOutFile.txt", "w")
for line in dict:
  # write line to output file
  outF.write(line)
  outF.write("\n")
outF.close()
