import numpy as np
import random
L = 4
N = L*L*L

M = np.zeros((L,L,L))# 3d array representing unit cell
active_atoms = []
#for i in range(L):
#    for j in range(L):
#        for k in range(L):
#            if (i+j+k)%2==0:
#                M[i,j,k] = 1.0
#                active_atoms.append((i,j,k))

for (i, j, k) in itertools.product(range(L),range(L),range(L)):
    if (i+j+k)%2==0:
        M[i,j,k] =1.0
        active_atoms.append((i,j,k))   
        
nbr = {i : [(i[0],(i[1]+1)%L,(i[2]+1)%L),
            (i[0],(i[1]-1)%L,(i[2]+1)%L),
            (i[0],(i[1]+1)%L,(i[2]-1)%L),
            (i[0],(i[1]-1)%L,(i[2]-1)%L),
            
            ((i[0]+1)%L,i[1],(i[2]+1)%L),
            ((i[0]-1)%L,i[1],(i[2]+1)%L),
            ((i[0]+1)%L,i[1],(i[2]-1)%L),
            ((i[0]-1)%L,i[1],(i[2]-1)%L),
            
            ((i[0]+1)%L,(i[1]+1)%L,i[2]),
            ((i[0]-1)%L,(i[1]+1)%L,i[2]),
            ((i[0]+1)%L,(i[1]-1)%L,i[2]),
            ((i[0]-1)%L,(i[1]-1)%L,i[2])] for i in active_atoms}
def swap(M):
    pot = []
    while len(pot)==0:
        r0 = random.choice(active_atoms)
        s0 = M[r0[0],r0[1],r0[2]]
        r = r0
        neighbours = nbr[r0]
        for i in neighbours:
            s1 = M[i[0],i[1],i[2]]
            if s0+s1==3.0:
                pot.append(i)
    r1 = random.choice(pot)
    s = M[r1[0],r1[1],r1[2]]
    M[r0[0],r0[1],r0[2]] = s
    M[r1[0],r1[1],r1[2]] = s0
    return M
print(swap(M))
