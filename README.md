# プログラミング2024 課題4

## 課題の内容

リポジトリに同梱のテキストファイル[melos.txt](./melos.txt)は、「走れメロス(太宰治)」の全文です(ただしコピー&ペーストの都合上、漢字のルビも本文に埋め込まれてしまっていますが、ご了承ください)。テキストファイルのエンコーディングは全てデフォルトのUTF-8で構いません。

### 課題4-1

[melos.txt](./melos.txt)の内容を読み込み登場人物のセリフのみをファイルmelos_dialogue.txtに出力するPythonスクリプト[extract_dialogue.py](./extract_dialogue.py)を作成しなさい。出力例として、[melos_dialogue_example.txt](./melos_dialogue_example.txt)を同梱しますので、参考にしてください。

**ヒント** まずは`split`メソッドを使って全文を`「`で分割し、部分文字列のリストを作成しましょう。分割して得られた**最初の部分文字列**には会話部分は含まれないので注意してください。次に、再び`split`メソッドで各部分文字列を`」`で分割し、発話部分を取り出しましょう。最後に、とりだした発話部分の前後に`「`と`」`をつけて**改行つき**でテキストファイルに出力すれば完了です。

### 課題4-2

[melos.txt](./melos.txt)の内容を読み込み、**ひらがなを全てカタカナに、カタカナを全てひらがなに変換**したうえでファイルmelos_katakana.txtに出力するPythonスクリプトkatakana.pyを作成しなさい。出力例として、melos_katakana_example.txtを同梱しますので、参考にしてください。

**ヒント:** 全てのひらがなのユニコードコードポイントの列は、`range(ord('あ'),ord('ん')+1)`で得られます。カタカナも同様です。
