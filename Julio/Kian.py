


import open3d as o3d
import numpy as np
import PIL.Image
import IPython.display
import os
import urllib.request
import tarfile
import gzip
import zipfile
import shutil


print("Testing mesh in open3d ...")
mesh = o3d.get_knot_mesh()
print(mesh)
print('Vertices:')
print(np.asarray(mesh.vertices))
print('Triangles:')
print(np.asarray(mesh.triangles))
