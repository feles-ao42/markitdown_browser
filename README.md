# MarkItDown Web Converter

オフィスドキュメントやPDFなどの各種ファイルをMarkdown形式に変換するWebアプリケーションです。Microsoft社の[MarkItDown](https://github.com/microsoft/markitdown)ライブラリを利用して、ブラウザ上で簡単にファイル変換が行えます。

## 機能

- ブラウザからのファイルアップロード
- 各種ファイル形式からMarkdownへの自動変換
- 変換したファイルの即時ダウンロード

## 対応ファイル形式

- Microsoft Office (.docx, .xlsx, .pptx)
- PDF (.pdf)
- 画像ファイル (.jpg, .jpeg, .png)
- テキストファイル (.txt, .csv, .json, .xml)
- HTML (.html)

## 必要要件

- Docker
- Docker Compose

## インストールと実行方法

1. リポジトリのクローン:
```bash
git clone git@github.com:feles-ao42/markitdown_browser.git
cd markitdown_browser
```

2. Dockerコンテナの起動:
```bash
docker-compose up --build
```

3. ブラウザで以下のURLにアクセス:
```
http://localhost:5000
```

## 使用方法

1. ブラウザでアプリケーションにアクセス
2. 「ファイルを選択」ボタンをクリックしてファイルを選択
3. 「Convert to Markdown」ボタンをクリック
4. 変換されたMarkdownファイルが自動的にダウンロードされます

## プロジェクト構成

```
markitdown_browser/
├── app.py              # メインアプリケーション
├── templates/          # HTMLテンプレート
│   └── upload.html     # アップロードページ
├── Dockerfile          # Dockerビルド設定
├── docker-compose.yml  # Docker Compose設定
└── requirements.txt    # Pythonパッケージ依存関係
```

## セキュリティ対策

- ファイルサイズ制限: 16MB
- 許可された拡張子のみ受付
- セキュアなファイル名の処理
- アップロードディレクトリの自動作成

## 開発環境での実行

Dockerを使用せずにローカルで実行する場合:

1. Python環境のセットアップ:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. アプリケーションの起動:
```bash
python app.py
```

## 制限事項

- アップロードファイルサイズは16MBまで
- 一度に処理できるファイルは1つまで
- 変換結果は一時的にサーバーに保存され、ダウンロード後に削除されます

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 謝辞

このプロジェクトはMicrosoft社の[MarkItDown](https://github.com/microsoft/markitdown)ライブラリを使用しています。
