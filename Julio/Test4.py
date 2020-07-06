
import open3d as o3d
import numpy as np



print("Load a polygon volume and use it to crop the original point cloud")
vol = o3d.visualization.read_selection_polygon_volume("cropped.json")
chair = vol.crop_point_cloud(pcd)
o3d.visualization.draw_geometries([chair])
print(downpcd.normals[0])