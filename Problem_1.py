# 紙の厚さ
THICKNESS = 0.00008

# 折られた紙の厚さ
folded_thickness = THICKNESS

# 紙を1回折った時の厚さを計算するコード
# folded_thickness = THICKNESS * 2

# 43回を指定
number_of_folding = 43

# 折られた紙の厚さを求める計算式
folded_thickness = THICKNESS * (2 ** number_of_folding)

# 結果の表示
print("厚さ： {}メートル".format(folded_thickness))
