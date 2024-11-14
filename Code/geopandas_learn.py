import geopandas as gpd
import matplotlib.pyplot as plt
# 读取shp文件
info_gpd = gpd.read_file('Shapefile_example/CA_cities_wgs1984.shp')


info_geometry = info_gpd.geometry

# 最重要的一个属性“geometry”
print(info_geometry)

# 直接读取经纬度信息，不需要过多的操作
lat = []
lon = []
for point in info_gpd.geometry:
    lon.append(point.x)
    lat.append(point.y)





