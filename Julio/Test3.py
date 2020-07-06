
import open3d as o3d
import numpy as np

"""
print("Load a ply point cloud, print it, and render it")
pcd = o3d.io.read_point_cloud("f16.ply")
print(pcd)
print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd])

print("Downsample the point cloud with a voxel of 0.05")
downpcd = pcd.voxel_down_sample(voxel_size=0.11)
o3d.visualization.draw_geometries([downpcd])

print("Recompute the normal of the downsampled point cloud")
downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
o3d.visualization.draw_geometries([downpcd])

print("Print a normal vector of the 0th point")
print(downpcd.normals[0])

print("Print the normal vectors of the first 10 points")
print(np.asarray(downpcd.normals)[:10, :])


print("Load a polygon volume and use it to crop the original point cloud")
vol = o3d.visualization.read_selection_polygon_volume("cropped.json")
pcd = o3d.io.read_point_cloud("fragment.ply")
chair = vol.crop_point_cloud(pcd)
o3d.visualization.draw_geometries([chair])



print("Paint chair")
chair.paint_uniform_color([1, 0.706, 0])
o3d.visualization.draw_geometries([chair])
"""

pcl = o3d.io.read_triangle_mesh("airplane.ply").sample_points_poisson_disk(number_of_points=2000)
hull, _ = pcl.compute_convex_hull()
hull_ls = o3d.geometry.LineSet.create_from_triangle_mesh(hull)
hull_ls.paint_uniform_color((1, 0, 0))
o3d.visualization.draw_geometries([pcl, hull_ls])

pcd = o3d.io.read_point_cloud("airplane.ply")

with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
    labels = np.array(pcd.cluster_dbscan(eps=0.02, min_points=10, print_progress=True))

max_label = labels.max()
print(f"point cloud has {max_label + 1} clusters")
colors = o3d.visualization.PointColorOption.Color ("airplane.ply")(labels / (max_label if max_label > 0 else 1))
colors[labels < 0] = 0
pcd.colors = o3d.utility.Vector3dVector(colors[:0, :3])
o3d.visualization.draw_geometries([pcd])

