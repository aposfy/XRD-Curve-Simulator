#!/usr/bin/env python

import math
import numpy
import cmath
import pprint

a=4.19

#============================================== Atom Class ==============================================
class atom:
    def __init__(self, atom_F,atom_x,atom_y,atom_z):
        self.F=atom_F
        self.x=atom_x
        self.y=atom_y
        self.z=atom_z
        
    # A rotation function, using rotation matrix, to change the position of this atom according to the rotation angle.
    def rotate(self,alpha):
        temp_matrix=[[self.x],[self.y]]
        temp_angle=numpy.radians(alpha)
        temp_rotation_matrix=[[float(math.cos(temp_angle)),float(-math.sin(temp_angle))],[float(math.sin(temp_angle)),float(math.cos(temp_angle))]]
        temp_result=numpy.matmul(temp_rotation_matrix,temp_matrix)
        self.x=temp_result[0][0]
        self.y=temp_result[1][0]

#============================================== BaZrO3 Lattice Class ==============================================
class BaZrO3_lattice:
    def __init__(self, lattice_i, lattice_j, lattice_k):
        
        # Find the position of the lattice in the Frame of Reference of the whole film, according to the index of this lattice, i,j,k.
        self.lattice_0x=lattice_i*a
        self.lattice_0y=lattice_j*a
        self.lattice_0z=lattice_k*a
        
        # Find the positions of the atoms in the Frame of Reference of the whole film, according to the coordinates of these atoms relative to the origin of the lattice.
        self.Zr_atom=atom(40,self.lattice_0x,self.lattice_0y,self.lattice_0z)
        self.Ba_atom=atom(56,self.lattice_0x+a/2,self.lattice_0y+a/2,self.lattice_0z+a/2)
        self.O1_atom=atom(8,self.lattice_0x+a/2,self.lattice_0y,self.lattice_0z)
        self.O2_atom=atom(8,self.lattice_0x,self.lattice_0y+a/2,self.lattice_0z)
        self.O3_atom=atom(8,self.lattice_0x,self.lattice_0y,self.lattice_0z+a/2)
        
        self.all_atoms=[self.Ba_atom,self.Zr_atom,self.O1_atom,self.O2_atom,self.O3_atom]
        
    # To rotate this lattice is to rotate all the atoms in this lattice
    def rotate(self,alpha):
        for p in range(0,5):
            self.all_atoms[p].rotate(alpha)
            
#============================================== MgO Lattice Class ==============================================
class MgO_lattice:
    def __init__(self, lattice_i, lattice_j, lattice_k):
        
        # Find the position of the lattice in the Frame of Reference of the whole film, according to the index of this lattice, i,j,k.        
        self.lattice_0x=lattice_i*a
        self.lattice_0y=lattice_j*a
        self.lattice_0z=lattice_k*a+30*a
        
        # Find the positions of the atoms in the Frame of Reference of the whole film, according to the coordinates of these atoms relative to the origin of the lattice.
        self.Mg1_atom=atom(12,self.lattice_0x,self.lattice_0y,self.lattice_0z)
        self.Mg2_atom=atom(12,self.lattice_0x+a/2,self.lattice_0y+a/2,self.lattice_0z)
        self.Mg3_atom=atom(12,self.lattice_0x,self.lattice_0y+a/2,self.lattice_0z+a/2)
        self.Mg4_atom=atom(12,self.lattice_0x+a/2,self.lattice_0y,self.lattice_0z+a/2)
        
        self.O1_atom=atom(8,self.lattice_0x+a/2,self.lattice_0y,self.lattice_0z)
        self.O2_atom=atom(8,self.lattice_0x,self.lattice_0y+a/2,self.lattice_0z)
        self.O3_atom=atom(8,self.lattice_0x,self.lattice_0y,self.lattice_0z+a/2)
        self.O4_atom=atom(8,self.lattice_0x+a/2,self.lattice_0y+a/2,self.lattice_0z+a/2)
        
        self.all_atoms=[self.Mg1_atom,self.Mg2_atom,self.Mg3_atom,self.Mg4_atom,self.O1_atom,self.O2_atom,self.O3_atom,self.O4_atom]
        
    # To rotate this lattice is to rotate all the atoms in this lattice
    def rotate(self,alpha):
        for p in range(0,8):
            self.all_atoms[p].rotate(alpha)

# An array containing all the BaZrO3 lattice            
all_BaZrO3_lattice=[[[BaZrO3_lattice(i,j,k) for k in range(0,30)]for j in range(0,30)]for i in range(0,30)]
print (all_BaZrO3_lattice[20][20][5].lattice_0z)
# An array containing all the MgO lattice   
all_MgO_lattice=[[[MgO_lattice(i,j,k) for k in range(0,30)]for j in range(0,30)]for i in range(0,30)]
print (all_MgO_lattice[20][20][5].lattice_0z)
'''
# Hydrogen interstitials
for i in range(0,30):
    for j in range(0,30):
        for k in range(0,30):
            if (i+j+k)%2==0:
                all_BaZrO3_lattice[i][j][k].O1_atom.y=all_BaZrO3_lattice[i][j][k].O1_atom.y+0.35
                all_BaZrO3_lattice[i][j][k].O2_atom.x=all_BaZrO3_lattice[i][j][k].O2_atom.x+0.35
            else:
                all_BaZrO3_lattice[i][j][k].O1_atom.y=all_BaZrO3_lattice[i][j][k].O1_atom.y-0.35
                all_BaZrO3_lattice[i][j][k].O2_atom.x=all_BaZrO3_lattice[i][j][k].O2_atom.x-0.35
                '''
'''
# Rotation
for i in range(0,30):
    for j in range(0,30):
        for k in range(0,30):
            all_BaZrO3_lattice[i][j][k].rotate(45)
            all_MgO_lattice[i][j][k].rotate(45)
'''

# Output positions of atoms in BaZrO3
fout=open('Lattices_BaZrO3_MgO_0.txt','w')
fout.write('351000')
fout.write('\n')
for i in range(0,30):
    for j in range(0,30):
        for k in range(0,30):
            for l in range(0,5):
                fout.write(str(all_BaZrO3_lattice[i][j][k].all_atoms[l].F))
                fout.write('\n')
                fout.write(str(all_BaZrO3_lattice[i][j][k].all_atoms[l].x))
                fout.write('\n')
                fout.write(str(all_BaZrO3_lattice[i][j][k].all_atoms[l].y))
                fout.write('\n')
                fout.write(str(all_BaZrO3_lattice[i][j][k].all_atoms[l].z))
                fout.write('\n')
                print(i,j,k)
                
for i in range(0,30):
    for j in range(0,30):
        for k in range(0,30):
            for l in range(0,8):
                fout.write(str(all_MgO_lattice[i][j][k].all_atoms[l].F))
                fout.write('\n')
                fout.write(str(all_MgO_lattice[i][j][k].all_atoms[l].x))
                fout.write('\n')
                fout.write(str(all_MgO_lattice[i][j][k].all_atoms[l].y))
                fout.write('\n')
                fout.write(str(all_MgO_lattice[i][j][k].all_atoms[l].z))
                fout.write('\n')
                print(i,j,k)                
fout.close()
print ('============================== End ==============================')
