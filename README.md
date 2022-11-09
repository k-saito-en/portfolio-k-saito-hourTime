# プロジェクト概要　必読！

<details>
<summary>目標
</summary>

  - インターン先での勤怠管理、給与計算の方法が、[slack](https://slack.com/intl/ja-jp/trials?remote_promo=f4d95f0b&utm_medium=ppc&utm_source=google&utm_campaign=cd_ppc_google_jp_ja_brand_slack_single_word_selfserve&utm_term=ss_slack_single_word_._スラック_._e_._c&utm_content=617976811340&gclid=CjwKCAjwhNWZBhB_EiwAPzlhNhZ0fWW_2S90B-URfKadz1t3UPWcIWSR2BBZDrJa7dDWcvMjc30CbxoCt4AQAvD_BwE&gclsrc=aw.ds)の専用チャンネルへのコメント（例：9:00出社しました）と、スプレッドシートで従業員毎に作成した就業履歴とを照らし合わせるというものだった。  
 こちらを、専用管理画面での入力のみで　給与計算・経費精算・給与明細発行、さらにはタスク管理　までを済ませられるWEBアプリを開発し、普段お世話になっている担当者さんの負担を軽減したいと考えた。

  - 自身初の個人プロジェクトということで、これからのエンジニア人生においていつでも戻ってこれる、参照できる「前例・型」という位置づけで、独学で調べながら開発を進める。
  
</details>
<details>
<summary>成功の評価指標
</summary>

- 需要の高いアプリ、作品になっているか
  - 実際に使用してもらい、フィードバックをもらう
  - demo動画、プレゼン資料を作成し、インターン先でエンジニアとしての仕事をもらう
- コードが整っているか
  - SOLID原則に従い、拡張性、可読性、保守性の高いコードを描く
- ユーザーを意識した構造か
  - 担当者さんにヒアリングを行い、現場での要件定義さながらの設計を行う
- 作品に明確な意図が込められているか
  - 目標欄参照

[参考サイト](https://www.sejuku.net/blog/86008)

</details>


<details>
<summary>使用技術（設計段階）
</summary>
  
- フロントエンド
  - 言語
    - JavaScript(HTML、CSSも視野に)
  - フレームワーク
    - Vue.js、Vuestic UI
    
- バックエンド
  - 言語
    - Python（Javaも検討中）
  - フレームワーク
    - django、Bolt(slackへの通知機能実装時に必要そう)
    
- インフラ
  - AWSEC2(Linax)、nginx、GCP
  
 - 開発環境
   - VScodeforMac

</details>

# 一次開発全体スケジュール

[こちら(Zenhubガントチャート)](https://github.com/k-saito-en/portfolio-k-saito-hourTime/issues#workspaces/hourtime-63685ca80391a20013b73b19/roadmap)（Chromeブラウザでないと表示されません🙇）

![スクリーンショット 2022-11-09 7 11 20](https://user-images.githubusercontent.com/111550856/200686816-f410adc7-2e11-45f8-a9ce-37faf7201afa.png)




# システム構成図（仕様の大幅変更につき変更予定）

![システム構成図2 1 drawio](https://user-images.githubusercontent.com/111550856/194798083-c1d69020-3c3e-441b-b831-c18243bfe69f.png)


# 画面設計図
[管理画面設計図](https://docs.google.com/presentation/d/11LiQ3onJrz9EIk4CIXRtZMHeSmYXCoYJ3ZZ_mBUo1Fc/edit#slide=id.p)

[ユーザー画面設計図](https://docs.google.com/presentation/d/14UeRYGmgPjf4JcJhtGOS6OQdGAuXuNWWYEv8fb3qXWo/edit)


# RULE

- プッシュする際は必ずプッシュ先を確認し、プロジェクトリーダーの許可なしに「本番環境」にプッシュしないこと
- コミットコメントは「Prefix」をつけること
  - feat: 新しい機能
  - fix: バグの修正
  - docs: ドキュメントのみの変更
  - style: 空白、フォーマット、セミコロン追加など
  - refactor: 仕様に影響がないコード改善(リファクタ)
  - perf: パフォーマンス向上関連
  - test: テスト関連
  - chore: ビルド、補助ツール、ライブラリ関連
 
# DEMO
 
"hoge"の魅力が直感的に伝えわるデモ動画や図解を載せる
 
# Features
 
"hoge"のセールスポイントや差別化などを説明する
 
# Requirement
 
"hoge"を動かすのに必要なライブラリなどを列挙する
 
* huga 3.5.2
* hogehuga 1.0.2
 
# Installation
 
Requirementで列挙したライブラリなどのインストール方法を説明する
 
```bash
pip install huga_package
```
 
# Usage
 
DEMOの実行方法など、"hoge"の基本的な使い方を説明する
 
```bash
git clone https://github.com/hoge/~
cd examples
python demo.py
```
 
# Note
 
注意点などがあれば書く
 
# Author
 
作成情報を列挙する
 
* 作成者
* 所属
* E-mail
 
# License
ライセンスを明示する
 
"hoge" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
 
社内向けなら社外秘であることを明示してる
 
"hoge" is Confidential.
