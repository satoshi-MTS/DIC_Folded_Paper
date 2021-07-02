# 紙の厚さ
THICKNESS = 0.00008

# 紙を1回折った時の厚さを計算するコード
# folded_thickness = THICKNESS * 2

# 43回の場合
number_of_folding = 43

folded_thickness = THICKNESS * (2 ** number_of_folding)

print("厚さ： {}メートル".format(folded_thickness))
