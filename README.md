# atcoder

atcoderを解くためのonlne環境レポジトリ

https://kenkoooo.com/atcoder/#/table/

## replitを使う

https://replit.com/@noypeban/atcoder

## 操作の流れ

### pathを通し、loginし、alias登録

```sh
# replitログイン後毎回source必要
source prepare.sh
```

### 問題をダウンロード

```sh
# コンペIDを指定する
acc new abc271
# => コンペID/問題番号のディレクトリ階層ができる
```

### 解く

main.pyファイルを作成、解く

### テスト

```sh
test
```

### 提出

```sh
submit
```
## install

1. replit左ペインのパッケージで`online-judge-tools`をインストール
2. Shellで`node`とタイプし、サジェストからnode.jsをインストール
3. Shellで`npm install atcoder-cli`とタイプし、accをインストール
4. `${PWD}/node_modules/.bin`にpathを通す

- 2で`replit no module named poetry`エラーが出たが、replの削除、再作成で先に進めた
- 3でほんとはグローバルインストールしたかったけど書き込み権がないと言われローカルにした

## acc設定

```sh
# 問題を選択せず全部ダウンロードする
acc config default-task-choice all 
# 検証用ディレクトリ名をojと同じにする
acc config default-test-dirname-format test
```