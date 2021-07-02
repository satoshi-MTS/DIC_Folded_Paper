# 紙の厚さ
THICKNESS = 0.00008

# 紙を1回折った時の厚さを計算するコード
# folded_thickness = THICKNESS * 2

# 43回の場合
number_of_folding = 43

folded_thickness = THICKNESS * (2 ** number_of_folding)

print("厚さ： {}メートル".format(folded_thickness))

# メートルをキロメートルに変換して小数点以下2桁で表示する
# print("厚さ： {:.2f}キロメートル".format(folded_thickness / 1000))

# メートルを万キロメートルに変換
print('厚さ : {:.2f}万キロメートル'.format(folded_thickness / 10 ** 7))

