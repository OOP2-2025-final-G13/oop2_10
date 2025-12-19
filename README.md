# 注文アプリ改

注文管理を効率化するためのWebアプリケーションです。ユーザー、製品、注文、統計、レビューの管理・編集が可能です。

---

## 目次
- [概要](#概要)
- [アピールポイント](#アピールポイント)
- [主な機能](#主な機能)
- [スクリーンショット](#スクリーンショット)
- [セットアップ](#セットアップ)
- [使い方](#使い方)
- [技術スタック](#技術スタック)
- [ディレクトリ構成](#ディレクトリ構成)

---

## 概要
本アプリケーションは、注文・ユーザー・製品・統計・レビューの管理を一元化し、業務効率化を支援します。直感的なUIで各項目の追加・編集が可能です。

## アピールポイント
- 直感的なUIで誰でも簡単に操作可能
- 一覧・検索・編集がすべてWeb上で完結
- 注文・売上の統計表示で業務改善に役立つ
- レビュー管理機能で顧客満足度向上
- シンプルな構成でカスタマイズ・拡張が容易
- 軽量なORM（Peewee）採用で高速動作

## 主な機能
- ユーザー管理（追加・編集）
- 製品管理（追加・編集）
- 注文管理（追加・編集）
- 統計表示（売上確認）
- レビュー管理（追加・編集）

## スクリーンショット
### ユーザー一覧
<img width="1280" height="516" alt="Image" src="https://github.com/user-attachments/assets/0b27a19e-ec08-4840-af5c-28eaf837631c" />

### 売上統計
<img width="1279" height="859" alt="Image" src="https://github.com/user-attachments/assets/251995e3-5df1-4ad1-ba25-1bdad7611477" />

### 管理画面（グラフ・分布）
<img width="645" height="1101" alt="Image" src="https://github.com/user-attachments/assets/4a91f880-32c8-4a67-b6a7-933bad4e6ccb" />

## セットアップ
### 必要条件
- Python 3.13 以上
- pip

### 必要パッケージ

```bash
pip install Flask==3.0.3 peewee==3.17.7
```

## 使い方
1. リポジトリをクローン
	```bash
	git clone https://github.com/OOP2-2025-final-G13/ordering-app-improvements.git
	cd ordering-app-improvements
	```
2. 必要パッケージをインストール
	```bash
	pip install Flask==3.0.3 peewee==3.17.7
	```
3. アプリケーションを起動
	```bash
	python app.py
	```
4. ブラウザでアクセス
	- [http://localhost:8080](http://localhost:8080)

## 技術スタック
- Python (Flask)
- Peewee (ORM)
- HTML/CSS (Jinja2テンプレート)

## ディレクトリ構成
```
ordering-app-improvements/
├── app.py
├── models/
├── routes/
├── static/
├── templates/
└── README.md
```
