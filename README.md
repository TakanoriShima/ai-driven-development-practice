# AI Training Support

GitHub Issue を起点に、AI を活用しながら実装・レビュー・テスト・Pull Request・Merge・Deploy まで進める、**AI 駆動開発プロセスを実践したポートフォリオ**です。

題材として、研修情報を入力すると生成 AI が企業向けの研修概要文を作成する Web アプリケーション「AI Training Support」を開発しました。

## 公開デモ

Streamlit Community Cloud にデプロイしています。

https://takanorishima-ai-driven-development-practice-app-hnjvvk.streamlit.app/

## デモ画面

[![AI Training Support デモ画面](https://i.gyazo.com/ed34da1bd032b4ad58bfcccfa70aea0c.png)](https://gyazo.com/ed34da1bd032b4ad58bfcccfa70aea0c)

## アプリケーション概要

AI Training Support は、企業研修の企画・準備を支援するシンプルな Web アプリケーションです。

研修タイトル、対象者、研修テーマ、研修時間、備考を入力すると、入力内容の確認に加えて、以下の 2 方式で研修概要文を生成できます。

- Python によるルールベースの研修概要生成
- Gemini API による生成 AI を利用した研修概要生成

生成 AI では、入力された研修情報をもとに、企業研修の案内文として自然な日本語を生成します。

## 主な機能

### 研修情報入力

以下の情報を入力できます。

- 研修タイトル
- 対象者
- 研修テーマ
- 研修時間
- 備考

研修タイトルと研修テーマは必須項目です。

### 入力内容の確認

「入力内容を確認」ボタンから、入力した研修情報を画面上で確認できます。

### ルールベースによる研修概要生成

「研修概要を生成」ボタンを押すと、Python の文字列処理によって研修概要文を生成します。

### 生成 AI による研修概要生成

「AI で研修概要を生成」ボタンを押すと、入力された研修情報を Gemini API へ渡し、企業研修の案内文として自然な研修概要を生成します。

例：

> 本研修は、営業および管理部門の一般社員を対象に、ChatGPT を活用した業務効率化や効果的なプロンプト設計を学ぶプログラムです。3 時間の研修内で基礎知識の解説から実践演習までを行い、日常業務ですぐに役立つスキルの習得を目指します。

## 使用技術

- Python
- Streamlit
- Gemini API
- google-genai
- Git / GitHub
- GitHub Issues
- Pull Requests
- GitHub Copilot
- ChatGPT
- Streamlit Community Cloud

## AI 駆動開発プロセス

本プロジェクトでは、単に生成 AI API をアプリケーションから利用するだけではなく、**開発工程そのものに AI を組み込むこと**を目的としました。

基本的な開発フローは以下です。

```text
GitHub Issue
    ↓
Feature Branch
    ↓
AIによる実装方針・コードの提案
    ↓
Human Review
    ↓
実装・修正
    ↓
動作テスト
    ↓
Commit / Push
    ↓
Pull Request
    ↓
Review
    ↓
Merge
    ↓
Deploy
```

AI が生成した内容をそのまま採用するのではなく、GitHub Issue を要件の基準として、人間が提案内容・コード・差分・動作結果を確認してから採用するプロセスを実践しました。

## AI と人間の役割分担

### AI

- Issue をもとにした実装方針の検討
- コード生成
- 修正案の提案
- テスト観点の整理
- README などのドキュメント作成支援

### 人間

- 要件の決定
- AI が Issue の要件を正しく理解しているかの確認
- コードレビュー
- Git 差分の確認
- 動作テスト
- セキュリティ確認
- Pull Request レビュー
- Merge の最終判断

開発中には、AI が Issue とは異なる実装内容を提案するケースもありました。

その際は AI の回答をそのまま採用せず、Issue の要件と照合して提案を却下・修正し、再度実装方針を検討しました。

この経験から、AI 駆動開発では「AI に実装を任せる」だけではなく、**人間が要件・品質・セキュリティを管理することが重要**だと考えています。

## Issue ベースの段階的開発

本プロジェクトは、機能を一度に実装するのではなく、GitHub Issue 単位で段階的に開発しました。

### Issue #1

研修支援 Web アプリケーションの初期構成を作成。

- Streamlit による基本画面
- アプリケーションタイトル・概要
- README
- requirements.txt

### Issue #3

研修情報入力フォームを追加。

- 研修タイトル
- 対象者
- 研修テーマ
- 研修時間
- 備考
- 必須項目チェック
- 入力内容確認

### Issue #5

研修情報からルールベースで研修概要文を生成する機能を追加。

- Python による文章生成
- 任意項目への対応
- 既存機能の回帰テスト

### Issue #7

Gemini API による生成 AI 機能を追加。

- 「AI で研修概要を生成」機能
- Gemini API 連携
- google-genai SDK
- API エラー処理
- Streamlit Secrets による API キー管理
- 既存機能の回帰テスト

各 Issue ごとに Feature Branch を作成し、実装・テスト・Pull Request・レビュー・Merge を行いました。

## セキュリティ

Gemini API キーはソースコードに直接記述していません。

ローカル環境では、以下のファイルを使用します。

```text
.streamlit/secrets.toml
```

設定例：

```toml
GEMINI_API_KEY = "YOUR_API_KEY"
```

`secrets.toml` は `.gitignore` に登録し、Git の管理対象から除外しています。

```gitignore
.streamlit/secrets.toml
```

公開環境では、Streamlit Community Cloud の Secrets 機能を利用しています。

**API キーなどの秘密情報を GitHub リポジトリへコミットしない設計**としています。

## セットアップ方法

### 1. リポジトリをクローン

```bash
git clone git@github.com:TakanoriShima/ai-driven-development-practice.git
```

### 2. プロジェクトディレクトリへ移動

```bash
cd ai-driven-development-practice
```

### 3. 必要なライブラリをインストール

```bash
pip install -r requirements.txt
```

### 4. Gemini API キーを設定

プロジェクト直下に以下のファイルを作成します。

```text
.streamlit/secrets.toml
```

内容：

```toml
GEMINI_API_KEY = "YOUR_API_KEY"
```

実際の API キーは GitHub へコミットしないでください。

### 5. アプリケーションを起動

```bash
streamlit run app.py
```

ブラウザからアプリケーションを操作できます。

## 使い方

1. 研修情報を入力します。
2. 「入力内容を確認」で入力内容を確認できます。
3. 「研修概要を生成」でルールベースの研修概要を生成できます。
4. 「AI で研修概要を生成」で Gemini API による研修概要を生成できます。

## このプロジェクトで実践したこと

- GitHub Issue を起点としたタスク管理
- Feature Branch による機能開発
- AI を利用した実装方針・コード生成
- AI 出力に対する Human Review
- Git による差分確認
- 手動テスト・回帰テスト
- Pull Request によるレビュー
- Issue と Pull Request の関連付け
- Merge 後のブランチ整理
- API キーなど秘密情報の安全な管理
- Streamlit Community Cloud への Deploy

## 今後の拡張例

- 生成した研修概要の保存・履歴管理
- 研修カリキュラム案の AI 生成
- プロンプトテンプレートの切り替え
- 自動テストの導入
- CI/CD によるテスト・デプロイ自動化

## 開発目的

本プロジェクトは、完成した Web アプリケーションだけでなく、

**「AI を活用しながら、人間が要件・品質・セキュリティを管理してソフトウェアを開発するプロセス」**

を実践し、その開発過程を GitHub 上に残すことを目的としています。
