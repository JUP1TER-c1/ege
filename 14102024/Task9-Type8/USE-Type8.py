from itertools import product
alphabet = '012345678'
ap=[]
for i in product(alphabet, repeat=5):
    if  i[0] != '0' and int(i[0]) > int(i[1]) > int(i[2]) > int(i[3]) > int(i[4]):
        ap.append(i)
print(len(ap))