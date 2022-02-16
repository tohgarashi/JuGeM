# プログラミング用日本語等幅フォント JuGeM

## 特徴

- JuliaMonoと源柔ゴシック等幅Lを合成・調整した、プログラミング用の日本語等幅フォントです。
  - JuliaMono : Julia言語を念頭に制作されている等幅フォントです。(https://github.com/cormullion/juliamono)
  - 源柔ゴシック等幅L : 源ノ角ゴシックをTrueType 形式に変換し、角を丸める加工を行い丸ゴシック風にした派生フォントです。(http://jikasei.me/font/genjyuu/)

- JuliaMonoの文脈依存置換の内、パイプ演算などの横向き三角のみを有効化するfeature 'ss21' を追加しています。

- Light ~ Blackの5つのウェイトとそれぞれのイタリック体を用意しています。
  - Lightを作成する際、バランスを整えるためJuliaMonoを機械的に細くしました。

- ライセンス
  - フォントファイルは SIL Open Font License 1.1 です。
  - 合成スクリプト等のソースコードは MIT です。