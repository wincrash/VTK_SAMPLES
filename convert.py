#!/usr/bin/python3

import meshio
import glob
import vtk
path="*.vtu"
files = glob.glob(path)
for x in files:
    print(x)
    newX=x[:-3]+"vtk"
    print(newX)

# Read the source file.
    reader = vtk.vtkXMLUnstructuredGridReader()
    reader.SetFileName(x)
    reader.GetPointDataArraySelection().EnableAllArrays ()

    reader.Update()  # Needed because of GetScalarRange
    output = reader.GetOutput()
    print(output)
    writer = vtk.vtkDataSetWriter()
    writer.SetFileName(newX)
    writer.SetInputData(output)
    writer.Write()

#    mesh = meshio.read(x)
#    mesh.write(newX,file_format="vtk")
#    mesh.write(newX)
