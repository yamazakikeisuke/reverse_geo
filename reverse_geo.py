import geopandas as gp
from shapely.geometry import Polygon, Point

#緯度経度から市区町村を割り出す関数
def reverse_geo(shdf, point):
    for index, row in shdf.iterrows():
       polygon = row['geometry']
       #"point"がどの境界に含まれるかを判定する
       if polygon.contains(point):
         #見つかったら該当する市区町村の情報を必要な列だけ返す
         #Erisのデータの場合は、県、郡、市区町村、人口、世帯数
          return(row['KEN'], row['GUN'], row['SIKUCHOSON'], row['P_NUM'], row['H_NUM'])
    #見つけられなかった場合はNoneを返す
    return("None", "None", "None", "None", "None")

#判定に使う境界データを読み込む（"japan_ver84"ディレクトリー配下のErisの全国市区町村界データの場合）
shdf = gp.read_file('./japan_ver84/japan_ver84.shp', encoding='shift-jis')

#座標系の確認。調べたい地点の座標系と同一であることを必ず確認する
print(shdf.crs)

#調べたい地点の情報（例）
position = Point(139.45802792168061, 35.318270525221962)

#逆ジオコーディングを実行
reverse_geo_info = reverse_geo(shdf, position)
print(reverse_geo_info)

