# モジュールのインポート
import time

# 紙の厚さ
THICKNESS = 0.00008

# 折られた紙の厚さ
folded_thickness = THICKNESS

# 紙を1回折った時の厚さを計算するコード
# folded_thickness = THICKNESS * 2

# 43回を指定
number_of_folding = 43

# 開始時刻の設定
start1 = time.time()

# 折られた紙の厚さを求める計算式
folded_thickness = THICKNESS * (2 ** number_of_folding)

# 経過時間の測定
elapsed_time1 = time.time() - start1

# 折られた紙の厚さのリセット
folded_thickness = THICKNESS

# 開始時刻の設定
start2 = time.time()

# 折られた紙の厚さを求める計算式(for文での実行)
for number in range(number_of_folding):
	folded_thickness = folded_thickness * 2

# 経過時間の測定
elapsed_time2 = time.time() - start2

# メートルをキロメートルに変換して小数点以下2桁で表示
# print("厚さ： {:.2f}キロメートル".format(folded_thickness / 1000))

# メートルを万キロメートルに変換
print('厚さ : {:.2f}万キロメートル'.format(folded_thickness / 10 ** 7))

# 経過時間の表示
print('べき乗の場合の計算速度 : {}[s]'.format(elapsed_time1))
print('for文の場合の計算速度 : {}[s]'.format(elapsed_time2))
