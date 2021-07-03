# matplotlibのインポート
import matplotlib.pyplot as plt

# 紙の厚さ
THICKNESS = 0.00008

# 折られた紙の厚さ
folded_thickness = THICKNESS

# 紙を1回折った時の厚さを計算するコード
# folded_thickness = THICKNESS * 2

# 43回を指定
number_of_folding = 43

# 空のリストを作成+初期値の追加
folded_thickness_list = [folded_thickness]

# 折られた紙の厚さを求める計算式(for文での実行)
for number in range(number_of_folding):
	folded_thickness = folded_thickness * 2
	folded_thickness_list.append(folded_thickness)

# 格納数の確認
print(len(folded_thickness_list))

# グラフを表示する。タイトルと軸ラベル名付き。
plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness [m]")
plt.plot(folded_thickness_list)
plt.show()
