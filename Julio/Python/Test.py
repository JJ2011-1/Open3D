import open3d


"""print("Testing IO for meshes ...")
mesh = open3d.io.read_triangle_mesh("airplane.ply")
print(mesh)
open3d.io.write_triangle_mesh("copy_of_knot.ply", mesh)
"""


print("Testing IO for images ...")
img = open3d.io.read_image("Flower.jpg")
print(img)
open3d.io.write_image("copy_of_lena_color.jpg", img)

