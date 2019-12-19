import numpy as np

Matris=[[0, 1, 1, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 1, 0, 0],
[1, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 1, 1, 0, 0],
[0, 0, 0, 1, 0, 0, 1, 0],
[0, 1, 0, 1, 0, 0, 0, 1],
[0, 0, 1, 0, 1, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 1, 0]]

Matris_1=np.zeros((8,8))
M=np.zeros((7,7))

for i in range(8):
    for j in range(8):
        if i==j:
            for k in range(8):
                L[i][j]+=K[i][k];
        else:
            L[i][j]=-K[i][j]

for i in range(7):
    for j in range(7):
        M[i][j]=L[i][j]

print("Komsuluk matrisi:")
print(K)

print("7x7 matrisi:")
print(M)

print("yayilim agaclari sayisi:")
print(int(np.linalg.det(M)))