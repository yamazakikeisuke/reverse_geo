# 境界データで逆ジオコーディングする

緯度と経度から市区町村名などを取得する（逆ジオコーディング）ためのソース(reverse_geo.py)です。

都道府県や市区町村、それよりも細かい地区情報が盛り込まれた境界データなどがあった場合に、調べたい緯度・経度がそれらの境界のどの場所に含まれるかを判定します。

企業のAPIやGeoPandasなどでも同様の機能を提供していますが、回数制限やネットワーク速度に依存せずに処理を行うことができます。

# 境界データの各種リンク
[ESRIジャパンの全国市区町村界データ](https://www.esrij.com/products/japan-shp/)

[統計地理情報システム](https://www.e-stat.go.jp/gis/statmap-search?type=2)

[スマートニュース メディア研究所の選挙区境界データなど](https://smartnews-smri.com/research/research-757/)
