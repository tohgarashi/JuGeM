# プログラミング用日本語等幅フォント JuGeM

## ダウンロード

[Releases](https://github.com/tohgarashi/JuGeM/releases)から`JuGeM-ttf.tar.gz`をダウンロードし解凍すると、各種ttfファイルが入っています。

これを環境に応じて配置してください。

## 特徴

- JuliaMonoと源柔ゴシック等幅Lを合成・調整した、プログラミング用の日本語等幅フォントです。
  - JuliaMono : Julia言語を念頭に制作されている等幅フォントです。(https://github.com/cormullion/juliamono)
  - 源柔ゴシック等幅L : 源ノ角ゴシックをTrueType 形式に変換し、角を丸める加工を行い丸ゴシック風にした派生フォントです。(http://jikasei.me/font/genjyuu/)

- 半角全角1:2の幅比率です。\
  また、JuliaMonoのグリフは縦横5:3の比率であり、これをキープしたまま半角全角1:2とするために全角の縦横比率を5:6としているため、全角文字は間隔が広くなっています。

- JuliaMonoには本来全角であるべきFULLWIDTHの文字(全角の句読点や英数字など)が半角幅で収録されていますが、JuGeMではこの部分に源柔ゴシックから全角のグリフを採用しています。

- JuliaMonoの文脈依存置換の内、パイプ演算などの横向き三角のみを有効化するfeature 'ss21' を追加しています。\
例えば、VSCodeではsettings.jsonに `"editor.fontLigatures": "'calt' off, 'ss21'"`と記述することで横向き三角の文脈依存置換のみを有効化することが出来ます。

- Light ~ Blackの5つのウェイトとそれぞれのイタリック体を用意しています。

  |  Weight    |  fontWeight  |
  | ----       | ----         |
  |  Light     |  300         |
  |  Regular   |  400         |
  |  Bold      |  700         |
  |  ExtraBold |  800         |
  |  Black     |  900         |

  - Lightを作成する際、バランスを整えるためJuliaMonoを機械的に細くしました。

- ライセンス
  - フォントファイルは SIL Open Font License 1.1 です。
  - 合成スクリプト等のソースコードは MIT です。