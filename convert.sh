#!/bin/bash

for x in $(ls *.vtu)
do

y=${x:0:$((${#x}-3))}vtk
echo $x $y
meshio convert --ascii $x $y
rm $x
done
