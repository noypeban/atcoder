# atcoder

atcoderを解くためのonlne環境レポジトリ

## replitを使う

https://replit.com/@noypeban/atcoder

## 操作の流れ

### 問題をダウンロード

```sh
# local installしたnodeモジュールにpathを通す
source addpath.sh
# コンペIDを指定する
acc new abc271
# login/passの入力
# 解く問題を選択
# => コンペID/問題番号のディレクトリ階層ができる
```

### 解く

main.pyファイルを作成、解く

### テスト

```sh
oj t -c "python3 main.py" -d ./tests/
```

### 提出

```sh
# ojでログインしないといけない時
oj login https://atcoder.jp
# submit
abc submit main.py
```

`vscode.dev`ではunittestをpythonで実行する事ができなかった。  
replitではunittestのコピペでは成功。

- replitではNixというパッケージマネージャーで管理している様子
- Packageの所から`online-judge-tools`を検索、＋ボタンでinstallできた
- 最初は`replit no module named poetry`と出たけど、replの削除、再作成でうまく行った

## install

1. replit左ペインのパッケージで`online-judge-tools`をインストール
2. Shellで`node`とタイプし、サジェストからnode.jsをインストール
3. Shellで`npm install atcoder-cli`とタイプし、accをインストール

ここまで行ったけど、accにパスが通ってない

## online-judge-toolsの設定、使い方

## TODO

- [ ] atcoder-cliが使えないか？
- [x] online-judge-toolsが使えないか？
- [ ] vscode.dev環境でコードを実行する方法は？
- [x] 無理なら、replitなど他のonline実行環境で環境構築は可能か？