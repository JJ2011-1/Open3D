import open3d 
import numpy as np  

	

print("Testing mesh in open3d ...")
mesh =open3d.io.read_triangle_mesh("f16.ply")
print(mesh)
print('Vertices:')
print(np.asarray(mesh.vertices))
print('Triangles:')
print(np.asarray(mesh.triangles))
open3d.visualization.draw_geometries([mesh])




print("Painting the mesh")
mesh.paint_uniform_color([1, 0.706, 0])
open3d.visualization.draw_geometries([mesh])

print("We make a partial mesh of only the first half triangles.")

mesh.triangles = open3d.utility.Vector3iVector(
        np.asarray(mesh.triangles)[:len(mesh.triangles) // 2, :])
mesh.triangle_normals = open3d.utility.Vector3dVector(
    np.asarray(mesh.triangle_normals)[:len(mesh.triangle_normals) // 2, :])
print(mesh.triangles)
open3d.visualization.draw_geometries([mesh])



