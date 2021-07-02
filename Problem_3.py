# 紙の厚さ
THICKNESS = 0.00008

# 紙を1回折った時の厚さを計算するコード
# folded_thickness = THICKNESS * 2

# 43回の場合
number_of_folding = 43
folded_thickness = THICKNESS

for number in range(number_of_folding):
	folded_thickness = folded_thickness * 2

# メートルを万キロメートルに変換
print('厚さ : {:.2f}万キロメートル'.format(folded_thickness / 10 ** 7))
