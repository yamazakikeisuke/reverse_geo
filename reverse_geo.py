import geopandas as gp
from geopandas.geoseries import *
from shapely.geometry import Polygon, Point
import ast

#緯度経度から市区町村を割り出す関数
def reverse_geo(shdf, point):
    for index, row in shdf.iterrows():
       polygon = row['geometry']
       if polygon.contains(point):
         #見つかったら該当する市区町村の情報を返す
          return(row['KEN'], row['GUN'], row['SIKUCHOSON'], row['P_NUM'], row['H_NUM'])
    #見つけられなかった場合はNoneを返す
    return("None", "None", "None", "None", "None")

#判定に使うシェープファイル
shdf = gp.read_file('./japan_ver84/japan_ver84.shp', encoding='shift-jis')

position = 

#逆ジオコーディングを実行
ret = reverse_geo(shdf, row["geometry"])