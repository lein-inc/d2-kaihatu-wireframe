#!/usr/bin/env python3
"""D2 Kaihatsu Giko ワイヤーフレーム＋ステートメント一括生成
藤岡EG WFのグレースケール骨格をベースに、第二開発技工のサイトマップへ適用
"""
import os, textwrap
BASE = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------
# 共通パーツ
# ------------------------------------------------------------
LOGO_HEADER = '株式会社第二開発技工'
LOGO_FOOTER = '株式会社第二開発技工'
ADDR = ('株式会社 第二開発技工<br>'
        '〒710-0845 岡山県倉敷市西富井446-2<br>'
        'TEL: 086-423-1899 ／ FAX: 086-423-2034')

NAV = [
    ('home.html', 'ホーム'),
    ('service.html', '事業案内'),
    ('strengths.html', '強み・技術'),
    ('social.html', '社会活動'),
    ('about.html', '会社案内'),
    ('recruit.html', '採用情報'),
    ('news.html', 'ニュース'),
    ('contact.html', 'お問い合わせ'),
]

def header():
    lis = ''.join(f'<li><a href="{h}">{l}</a></li>' for h, l in NAV)
    return f'''<header class="site-header">
  <div class="wrap">
    <div class="site-logo">{LOGO_HEADER}</div>
    <div class="header-right">
      <nav class="gnav"><ul>{lis}</ul></nav>
      <a href="tel:0864231899" class="tel-box">
        <div class="tel-label">お電話でのお問い合わせ</div>
        <div class="tel-num">086-423-1899</div>
        <div class="tel-hours">平日 9:00〜17:00</div>
      </a>
    </div>
  </div>
</header>'''

def footer():
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div>
      <div class="footer-logo">{LOGO_FOOTER}</div>
      <div class="addr">{ADDR}</div>
    </div>
    <div><h4>事業案内</h4><ul>
      <li><a href="service.html">事業案内 トップ</a></li>
      <li><a href="service-survey.html">測量</a></li>
      <li><a href="service-design.html">調査・設計</a></li>
      <li><a href="service-management.html">施工管理</a></li>
      <li><a href="strengths.html">強み・技術</a></li>
      <li><a href="social.html">社会活動</a></li>
    </ul></div>
    <div><h4>会社案内</h4><ul>
      <li><a href="about.html#greeting">代表あいさつ</a></li>
      <li><a href="about.html#company">会社概要</a></li>
      <li><a href="about.html#history">沿革</a></li>
      <li><a href="about.html#clients">主要取引先</a></li>
      <li><a href="about.html#access">アクセス</a></li>
    </ul></div>
    <div><h4>採用・その他</h4><ul>
      <li><a href="home.html">ホーム</a></li>
      <li><a href="recruit.html">採用情報</a></li>
      <li><a href="news.html">ニュース</a></li>
      <li><a href="contact.html">お問い合わせ</a></li>
      <li><a href="#">プライバシーポリシー</a></li>
    </ul></div>
    <div class="copyright">© 株式会社第二開発技工 All Rights Reserved.</div>
  </div>
</footer>
<script src="css/wireframe.js" defer></script>'''

def page(title, banner, body):
    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | 第二開発技工（WF）</title>
<link rel="stylesheet" href="css/wireframe.css?v=telbox">
</head>
<body>

<div class="wf-banner"><span>WIREFRAME | {banner}</span><a href="index.html">← 一覧に戻る</a></div>

{header()}

{body}

{footer()}
</body>
</html>'''

# ------------------------------------------------------------
# HOME
# ------------------------------------------------------------
HOME = '''
<!-- HERO -->
<section class="hero">
  <div class="wrap">
    <div class="catch">測る技術で未来に残す</div>
    <div class="sub">どこへでも行く。未来へも行く。公共測量・工事測量から3Dスキャナー・ドローンによる先端計測まで。岡山・倉敷から全国の現場を支える、測量・調査・施工管理のプロフェッショナル集団。<br><span style="font-size:11px; color:#888;">※キャッチコピーは 2026-08-26 定例で確定。サブコピーは5案から選定中（→ statement-main.html）</span></div>
    <div style="display:flex; gap:12px;">
      <a href="contact.html" class="btn">お問い合わせ</a>
      <a href="recruit.html" class="btn outline">採用情報</a>
    </div>
    <div class="hero-visual">[ ヒーロービジュアル ／ 3Dワイヤー地形＋高速道路・都市・川・橋のインフラCG（社会インフラのスケール感） ／ 確定コピーのタイプライター演出 → hero-infra.html 参照 ]</div>
  </div>
</section>

<!-- 3事業 -->
<section>
  <div class="wrap">
    <div class="sec-h"><h2>3つの事業</h2><span class="en">SERVICE</span></div>
    <p class="section-lead">「測量」「調査・設計」「施工管理」——専門の異なる3つの分野を、一つの会社で受け止めます。</p>
    <div class="grid-3">
      <div class="card">
        <div class="img-ph medium">測量 IMAGE</div>
        <div class="card-title">01. 測量</div>
        <p>公共測量／工事測量／全国対応。TS・GNSS・ドローン・3Dスキャナーを駆使した現場の"最初の一歩"。</p>
        <a href="service-survey.html" class="btn outline" style="margin-top:12px; font-size:12px;">詳しく見る →</a>
      </div>
      <div class="card">
        <div class="img-ph medium">調査・設計 IMAGE</div>
        <div class="card-title">02. 調査・設計</div>
        <p>土木設計（道路・河川・造成）／地質調査／環境調査。測量と地続きで現場を読み解きます。</p>
        <a href="service-design.html" class="btn outline" style="margin-top:12px; font-size:12px;">詳しく見る →</a>
      </div>
      <div class="card">
        <div class="img-ph medium">施工管理 IMAGE</div>
        <div class="card-title">03. 施工管理</div>
        <p>測量会社ならではの現場支援。一般労働者派遣許可のもと、施工管理技術者を派遣します。</p>
        <a href="service-management.html" class="btn outline" style="margin-top:12px; font-size:12px;">詳しく見る →</a>
      </div>
    </div>
  </div>
</section>

<!-- 強み -->
<section>
  <div class="wrap">
    <div class="sec-h"><h2>技術・強み</h2><span class="en">STRENGTHS</span></div>
    <div class="grid-3">
      <div class="card"><div class="img-ph medium">DRONE</div><div class="card-title">ドローン空撮測量</div><p>広域を短時間で。3次元空撮地形構造物処理システム導入済み。</p></div>
      <div class="card"><div class="img-ph medium">3D SCANNER</div><div class="card-title">3Dスキャナー</div><p>構造物・地形を高精度にデジタル化。BIM／CIMとの連携。</p></div>
      <div class="card"><div class="img-ph medium">GNSS</div><div class="card-title">GNSS測位</div><p>ネットワーク型RTK-GNSSで、現場の位置基準を素早く。</p></div>
    </div>
    <div style="text-align:right; margin-top:24px;"><a href="strengths.html" class="btn outline">技術・強みを見る →</a></div>
  </div>
</section>

<!-- 社会活動抜粋 -->
<section style="background:#f5f5f5;">
  <div class="wrap">
    <div class="sec-h"><h2>社会活動</h2><span class="en">SOCIAL ACTIVITIES</span></div>
    <div class="grid-2">
      <div class="img-ph large">災害時のドローン測量／地域活動 IMAGE</div>
      <div>
        <h3 style="margin-bottom:12px; font-size:20px;">災害の前と、災害の後に立つ。</h3>
        <p>岡山県測量設計業協会に加盟し、有事のときにすぐ動ける体制を維持しています。3次元空撮地形構造物処理システムを活用したドローン測量で、被災地の状況を短時間で把握します。</p>
        <p style="margin-top:12px;">地域の技術を次世代へ手渡す活動にも取り組んでいます。</p>
        <div style="display:flex; gap:12px; margin-top:24px;">
          <a href="social.html" class="btn outline">社会活動 →</a>
          <a href="about.html" class="btn outline">会社案内 →</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ニュース -->
<section>
  <div class="wrap">
    <div class="sec-h"><h2>ニュース</h2><span class="en">NEWS</span></div>
    <div class="news-list">
      <div class="news-item"><div class="news-date">2026.07.XX</div><div class="news-cat">お知らせ</div><div class="news-title">コーポレートサイトをリニューアルしました</div></div>
      <div class="news-item"><div class="news-date">2023.11.14</div><div class="news-cat">お知らせ</div><div class="news-title">労働者派遣法に基づく情報公開</div></div>
      <div class="news-item"><div class="news-date">2021.07.09</div><div class="news-cat">技術</div><div class="news-title">3次元空撮地形構造物処理システムを導入しました</div></div>
      <div class="news-item"><div class="news-date">2015.01.XX</div><div class="news-cat">お知らせ</div><div class="news-title">代表者交代のご挨拶</div></div>
    </div>
    <div style="text-align:right; margin-top:16px;"><a href="news.html" class="btn outline">ニュース一覧 →</a></div>
  </div>
</section>

<!-- 採用ハイライト -->
<section style="background:#eee;">
  <div class="wrap">
    <div class="sec-h"><h2>採用情報</h2><span class="en">RECRUIT</span></div>
    <div class="grid-2">
      <div>
        <h3 style="margin-bottom:12px; font-size:22px;">仕事があれば、一番に行こう。<br>どこへでも行こう。月へでも行くぞ。</h3>
        <p>創業のとき、先代が書き残した言葉です。「測量って何をする仕事？」から一緒にスタート。約1年で基本業務を習得し、ドローン・3Dスキャナーなど先端技術に触れながら、施工管理へキャリアアップできます。</p>
        <div class="numbers" style="margin-top:24px; grid-template-columns:repeat(3,1fr);">
          <div class="num-item"><div class="num-value">未経験</div><div class="num-label">歓迎</div></div>
          <div class="num-item"><div class="num-value">1年</div><div class="num-label">で基本習得</div></div>
          <div class="num-item"><div class="num-value">全国</div><div class="num-label">の現場</div></div>
        </div>
        <div style="margin-top:24px; display:flex; gap:12px;">
          <a href="recruit.html" class="btn">採用情報を見る</a>
          <a href="recruit.html#faq" class="btn outline">FAQ</a>
        </div>
      </div>
      <div class="img-ph large">若手スタッフの現場カット IMAGE</div>
    </div>
  </div>
</section>

<!-- CTA -->
<section>
  <div class="wrap">
    <div class="cta-box">
      <div class="cta-txt">測量・調査・施工管理のご相談<br>お気軽にお問い合わせください。</div>
      <div style="display:flex; gap:12px;">
        <a href="contact.html" class="btn">お問い合わせ</a>
        <a href="recruit.html" class="btn outline">採用エントリー</a>
      </div>
    </div>
  </div>
</section>
'''

# ------------------------------------------------------------
# SERVICE index
# ------------------------------------------------------------
SERVICE = '''
<section class="page-hero"><div class="wrap"><div class="en">SERVICE</div><h1>事業案内</h1></div></section>
<div class="breadcrumb"><div class="wrap"><a href="home.html">ホーム</a> ／ 事業案内</div></div>

<!-- イントロダクション -->
<section>
  <div class="wrap">
    <div class="sec-h"><h2>「はかる」から「支える」まで。</h2><span class="en">INTRODUCTION</span></div>
    <p class="section-lead" style="font-size:16px; color:#333; max-width:820px;">私たちの仕事は、まちのインフラをつくる工程の"最初の一歩"に立つことです。<br>道路・橋梁・河川・造成——そのすべては、地面を正確に「はかる」ことから始まります。</p>

    <div class="grid-2" style="margin-top:32px;">
      <div class="img-ph large">3事業の連なりを示すビジュアル IMAGE ／ 測量→設計→施工の流れ</div>
      <div>
        <p>1981年（昭和56年）の創業以来、私たちは公共測量・工事測量で培った「はかる技術」を軸に、調査・設計、そして施工管理へと領域を広げてきました。</p>
        <p style="margin-top:12px;">3つの事業はそれぞれ異なる専門性を持ちますが、地続きの現場で互いに補完し合います。同じ会社の中で連携できるから、精度と工程の両面でお客様の負担を減らすことができる——これが、私たちが3事業を一社で持ち続ける理由です。</p>
        <p style="margin-top:12px;">近年はドローン空撮・3Dレーザースキャナー・GNSSといった先端技術を積極的に取り入れ、i-Construction時代の現場に応えています。それでも変わらないのは、「早く・安く・良く」——技術屋の良心を軸に、現場で汗をかく姿勢です。</p>
      </div>
    </div>

    <div class="numbers" style="margin-top:48px;">
      <div class="num-item"><div class="num-value">1981〜</div><div class="num-label">創業年</div></div>
      <div class="num-item"><div class="num-value">3事業</div><div class="num-label">測量・調査設計・施工管理</div></div>
      <div class="num-item"><div class="num-value">全国</div><div class="num-label">対応エリア</div></div>
      <div class="num-item"><div class="num-value">3種類</div><div class="num-label">許可・登録<br><span style="font-size:10px;">測量業／派遣／補償コンサル</span></div></div>
    </div>

    <p style="margin-top:32px; padding:20px 24px; border-left:4px solid #333; background:#f5f5f5; font-size:14px; line-height:1.9;">
      公共測量・工事測量から3次元計測まで、"はかる"のあらゆる場面で。<br>
      土木設計・地質調査・環境調査で、次の一歩の計画を描く。<br>
      そして、労働者派遣許可のもと施工管理技術者を現場へ——<br>
      <b>「一社完結でお願いできる測量パートナー」</b>として、お客様の現場を支えます。
    </p>
  </div>
</section>

<!-- 3事業カード -->
<section style="background:#f5f5f5;">
  <div class="wrap">
    <div class="sec-h"><h2>3つの事業</h2><span class="en">3 PROFESSIONAL FIELDS</span></div>
    <p class="section-lead">それぞれの専門分野が異なるため、独立して深掘りできる構成にしています。3つの領域は互いに補完し合い、現場の"はじまりから終わりまで"を支えます。</p>
    <div class="grid-3">
      <div class="card">
        <div class="img-ph large">測量 IMAGE</div>
        <div class="card-title">01. 測量</div>
        <p>公共測量／工事測量。土木・橋梁・舗装・トンネル・造成など、あらゆる工事の"最初の一歩"を担います。</p>
        <a href="service-survey.html" class="btn outline" style="margin-top:12px; font-size:12px;">測量を見る →</a>
      </div>
      <div class="card">
        <div class="img-ph large">調査・設計 IMAGE</div>
        <div class="card-title">02. 調査・設計</div>
        <p>土木設計（道路・河川・造成）／地質調査／環境調査／設計照査。測量と地続きに現場を読み解きます。</p>
        <a href="service-design.html" class="btn outline" style="margin-top:12px; font-size:12px;">調査・設計を見る →</a>
      </div>
      <div class="card">
        <div class="img-ph large">施工管理 IMAGE</div>
        <div class="card-title">03. 施工管理</div>
        <p>測量会社ならではの現場理解を活かした施工管理。一般労働者派遣許可のもと、技術者を派遣します。</p>
        <a href="service-management.html" class="btn outline" style="margin-top:12px; font-size:12px;">施工管理を見る →</a>
      </div>
    </div>
  </div>
</section>
'''

# ------------------------------------------------------------
# SERVICE - 測量
# ------------------------------------------------------------
SERVICE_SURVEY = '''
<section class="page-hero"><div class="wrap"><div class="en">SERVICE / SURVEY</div><h1>測量</h1></div></section>
<div class="breadcrumb"><div class="wrap"><a href="home.html">ホーム</a> ／ <a href="service.html">事業案内</a> ／ 測量</div></div>

<section>
  <div class="wrap">
    <div class="sec-h"><h2>私たちはあなたの会社の測量部です</h2></div>
    <div class="grid-2">
      <div class="img-ph large">工事測量現場 IMAGE</div>
      <div>
        <p>土木工事・橋梁工事・舗装工事・トンネル工事・造成工事——あらゆる工事の"最初の一歩"を担うのが、私たちの仕事です。</p>
        <p style="margin-top:12px;">官公庁発注の調査測量から民間の工事測量まで、担当者の異動先まで追いかけていただけるほどの信頼関係を、全国の現場で築いてきました。</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-h"><h2>対応分野</h2></div>
    <div class="grid-3">
      <div class="card"><div class="img-ph medium">公共測量</div><div class="card-title">公共測量</div><p>基準点測量／水準測量／地形測量／路線測量など、公共事業に必要な各種測量。</p></div>
      <div class="card"><div class="img-ph medium">工事測量</div><div class="card-title">工事測量</div><p>丁張り／出来形／横断・縦断／構造物測量など、現場の"実施"を支える測量。</p></div>
      <div class="card"><div class="img-ph medium">深浅測量</div><div class="card-title">深浅・特殊測量</div><p>河川・港湾の深浅測量、ドローン空撮、3Dスキャナー計測などの特殊測量。</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-h"><h2>取扱機材</h2></div>
    <div class="grid-4">
      <div><div class="img-ph square">TS</div><p style="text-align:center; margin-top:8px; font-size:13px;">トータルステーション</p></div>
      <div><div class="img-ph square">GNSS</div><p style="text-align:center; margin-top:8px; font-size:13px;">GNSS受信機</p></div>
      <div><div class="img-ph square">DRONE</div><p style="text-align:center; margin-top:8px; font-size:13px;">測量用ドローン</p></div>
      <div><div class="img-ph square">3D SCAN</div><p style="text-align:center; margin-top:8px; font-size:13px;">3Dレーザースキャナー</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-h"><h2>作業フロー</h2></div>
    <div class="grid-4">
      <div class="card"><div class="card-meta">STEP 01</div><div class="card-title">ヒアリング・打合せ</div><p>目的・範囲・納期・成果物形式を確認。</p></div>
      <div class="card"><div class="card-meta">STEP 02</div><div class="card-title">現地踏査・計画立案</div><p>現場条件を確認し、最適な機材・工程を選定。</p></div>
      <div class="card"><div class="card-meta">STEP 03</div><div class="card-title">観測・計測</div><p>TS・GNSS・ドローン・3Dスキャナーで現場データを取得。</p></div>
      <div class="card"><div class="card-meta">STEP 04</div><div class="card-title">解析・成果物納品</div><p>点群処理・図化・数値計算を経て、CAD／PDF／点群等で納品。</p></div>
    </div>
  </div>
</section>

<section style="background:#eee;"><div class="wrap"><div class="cta-box"><div class="cta-txt">測量のご相談はお気軽に。</div><a href="contact.html" class="btn">お問い合わせ</a></div></div></section>
'''

# ------------------------------------------------------------
# SERVICE - 調査・設計
# ------------------------------------------------------------
SERVICE_DESIGN = '''
<section class="page-hero"><div class="wrap"><div class="en">SERVICE / SURVEY & DESIGN</div><h1>調査・設計</h1></div></section>
<div class="breadcrumb"><div class="wrap"><a href="home.html">ホーム</a> ／ <a href="service.html">事業案内</a> ／ 調査・設計</div></div>

<section>
  <div class="wrap">
    <div class="sec-h"><h2>測量と地続きで、現場を読み解く</h2></div>
    <p class="section-lead">測量で得たデータを、そのまま設計・調査へ。同じ会社の中で連携できるため、精度と工程の双方でお客様の負担を減らします。</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-h"><h2>土木設計</h2></div>
    <div class="grid-3">
      <div class="card"><div class="img-ph medium">道路設計</div><div class="card-title">道路設計</div><p>道路詳細設計・交差点設計・付属構造物設計。予備設計から詳細設計まで。</p></div>
      <div class="card"><div class="img-ph medium">河川設計</div><div class="card-title">河川設計</div><p>護岸設計・排水設計・小規模河川構造物設計。</p></div>
      <div class="card"><div class="img-ph medium">土地造成</div><div class="card-title">土地造成設計</div><p>宅地・工業用地・農地の造成計画、土量計算、切土・盛土。</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-h"><h2>地質調査</h2></div>
    <div class="grid-2">
      <div class="img-ph large">ボーリング調査 IMAGE</div>
      <div>
        <p>ボーリング調査、標準貫入試験、地下水位観測など、工事の安全性を左右する地盤情報を取得・解析します。</p>
        <p style="margin-top:12px;">測量と組み合わせることで、3次元地形＋地盤データを一体で把握することが可能です。</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-h"><h2>環境調査</h2></div>
    <div class="grid-3">
      <div class="card"><div class="img-ph medium">動植物調査</div><div class="card-title">動植物調査</div><p>事業予定地における動植物相の把握・保全対策検討。</p></div>
      <div class="card"><div class="img-ph medium">水質・大気</div><div class="card-title">水質・大気調査</div><p>工事前後の環境モニタリング。</p></div>
      <div class="card"><div class="img-ph medium">騒音・振動</div><div class="card-title">騒音・振動調査</div><p>工事・稼働時の周辺影響評価。</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-h"><h2>設計照査</h2></div>
    <p class="section-lead">設計内容の妥当性、施工可能性、コスト適正性を第三者視点でチェック。手戻りリスクを最小化します。</p>
  </div>
</section>

<section style="background:#eee;"><div class="wrap"><div class="cta-box"><div class="cta-txt">調査・設計のご相談はお気軽に。</div><a href="contact.html" class="btn">お問い合わせ</a></div></div></section>
'''

# ------------------------------------------------------------
# SERVICE - 施工管理
# ------------------------------------------------------------
SERVICE_MANAGEMENT = '''
<section class="page-hero"><div class="wrap"><div class="en">SERVICE / CONSTRUCTION MANAGEMENT</div><h1>施工管理</h1></div></section>
<div class="breadcrumb"><div class="wrap"><a href="home.html">ホーム</a> ／ <a href="service.html">事業案内</a> ／ 施工管理</div></div>

<section>
  <div class="wrap">
    <div class="sec-h"><h2>測量会社だからできる、施工管理</h2></div>
    <p class="section-lead">現場を「はかる」ことから始まる私たちが、施工の現場に立つ。だからこそ、測量精度と施工精度の橋渡しがスムーズです。</p>
    <div class="grid-3">
      <div class="card"><div class="card-title">01. 測量精度をそのまま施工へ</div><p>丁張りから出来形管理まで、同じチームで一貫対応が可能。</p></div>
      <div class="card"><div class="card-title">02. 全国の現場に対応</div><p>官公庁・ゼネコンの担当者様と共に、全国の工事現場へ派遣実績。</p></div>
      <div class="card"><div class="card-title">03. 一般労働者派遣許可</div><p>厚生労働省認可の派遣事業として、法令遵守で技術者を派遣します。</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-h"><h2>派遣スキーム</h2></div>
    <div class="grid-4">
      <div class="card"><div class="card-meta">STEP 01</div><div class="card-title">ヒアリング</div><p>案件概要／期間／技術者要件をお聞きします。</p></div>
      <div class="card"><div class="card-meta">STEP 02</div><div class="card-title">人選・ご提案</div><p>経験・保有資格を踏まえ、適任者をご提案。</p></div>
      <div class="card"><div class="card-meta">STEP 03</div><div class="card-title">派遣契約</div><p>労働者派遣契約を締結。</p></div>
      <div class="card"><div class="card-meta">STEP 04</div><div class="card-title">現場稼働・フォロー</div><p>稼働中も定期的に状況確認・フォローを行います。</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-h"><h2>派遣実績（2007年以降・分野例）</h2></div>
    <table class="info-table">
      <tr><th>道路工事</th><td>国道・県道・市道の新設／改良工事の施工管理支援</td></tr>
      <tr><th>橋梁工事</th><td>橋梁架設・耐震補強工事の施工管理支援</td></tr>
      <tr><th>造成工事</th><td>宅地造成・工業用地造成の施工管理支援</td></tr>
      <tr><th>河川工事</th><td>護岸工事・河道掘削の施工管理支援</td></tr>
      <tr><th>トンネル・その他</th><td>山岳トンネル・道路構造物の施工管理支援</td></tr>
    </table>
    <p style="font-size:12px; color:#666; margin-top:8px;">※ 具体案件・発注者名は掲載しておりません。ご希望に応じて個別にご案内します。</p>
  </div>
</section>

<section style="background:#eee;"><div class="wrap"><div class="cta-box"><div class="cta-txt">施工管理・技術者派遣のご相談</div><a href="contact.html" class="btn">お問い合わせ</a></div></div></section>
'''

# ------------------------------------------------------------
# STRENGTHS
# ------------------------------------------------------------
STRENGTHS = '''
<section class="page-hero"><div class="wrap"><div class="en">STRENGTHS</div><h1>強み・技術</h1></div></section>
<div class="breadcrumb"><div class="wrap"><a href="home.html">ホーム</a> ／ 強み・技術</div></div>

<!-- イントロダクション：伊能忠敬から現代へ -->
<section>
  <div class="wrap">
    <div class="sec-h"><h2>200年前の一歩と、今日の点群。</h2><span class="en">INTRODUCTION</span></div>
    <p class="section-lead" style="font-size:16px; color:#333; max-width:820px;">
      「はかる」という仕事は、200年以上ずっと続いてきました。<br>
      道具が変わっても、そこにある責任だけは、まったく同じです。
    </p>

    <div class="grid-2" style="margin-top:32px;">
      <div class="img-ph large">伊能忠敬モチーフ IMAGE ／ 古地図・量程車・天体観測</div>
      <div>
        <h3 style="font-size:18px; margin-bottom:12px;">1800年、日本地図をつくった男</h3>
        <p>伊能忠敬は、55歳から日本地図の測量を始めました。歩いた距離、およそ4万キロ。地球一周分にも及ぶ道のりを、17年かけて歩き切った男です。</p>
        <p style="margin-top:12px;">彼が持っていたのは、<b>量程車（歩数を測る道具）、間縄（距離を測る縄）、そして天体観測用の望遠鏡</b>だけ。それでも彼は、当時の世界水準に匹敵する精度で日本の輪郭を描き出しました。</p>
        <p style="margin-top:12px;">「まちの形を、正しく次の世代に手渡す」——測量の仕事の本質は、この時代からずっと変わっていません。</p>
      </div>
    </div>

    <div class="grid-2" style="margin-top:64px; align-items:center;">
      <div>
        <h3 style="font-size:18px; margin-bottom:12px;">2026年、点群で現場を描く私たち</h3>
        <p>200年経った今、私たちが持っているのは、<b>ドローン、3Dレーザースキャナー、GNSS受信機</b>。伊能忠敬が数日かけて歩いた範囲を、私たちは数時間で計測できるようになりました。</p>
        <p style="margin-top:12px;">広域を空から撮り、地形を点群にする。構造物をミリ単位でデジタル化する。衛星電波で位置を数センチの精度で決める——工事のための"最初のデータ"のかたちが、いま更新され続けています。</p>
        <p style="margin-top:12px;">i-Construction、BIM／CIM、3次元設計。国が進めるインフラのデジタル化にも、私たちは対応済みです。</p>
      </div>
      <div class="img-ph large">現代のテクノロジー IMAGE ／ ドローン・点群・GNSS</div>
    </div>

    <p style="margin-top:48px; padding:24px 28px; border-left:4px solid #333; background:#f5f5f5; font-size:15px; line-height:1.9;">
      それでも、私たちが大切にしているのは、<b>「現場に立つこと」</b>です。<br>
      どんなに機材が進化しても、地面に立ち、風を読み、目で確かめる感覚は絶対に手放さない。<br>
      伊能忠敬が歩いた一歩と、私たちの今日の一歩は、まっすぐつながっています。
    </p>
  </div>
</section>

<nav class="section-nav"><div class="wrap"><ul>
  <li><a href="#drone">ドローン測量</a></li>
  <li><a href="#3d">3Dスキャナー</a></li>
  <li><a href="#gnss">GNSS</a></li>
  <li><a href="#workflow">作業工程</a></li>
  <li><a href="#allrounder">全国対応・多分野</a></li>
</ul></div></nav>

<section id="drone">
  <div class="wrap">
    <div class="sec-h"><h2>ドローン測量・空撮</h2><span class="en anchor-tag">#drone</span></div>
    <div class="grid-2">
      <div class="img-ph large">ドローン空撮 IMAGE</div>
      <div>
        <p>2021年、3次元空撮地形構造物処理システムを導入。広域の地形を短時間で計測でき、精度・工期の両面でお客様に貢献します。</p>
        <ul style="margin-top:12px; padding-left:20px; list-style:disc; font-size:14px;">
          <li>広域地形の高速計測</li>
          <li>危険箇所・立入困難地の非接触計測</li>
          <li>点群・オルソ画像・DTM／DSM生成</li>
          <li>i-Construction 対応</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section id="3d">
  <div class="wrap">
    <div class="sec-h"><h2>3Dレーザースキャナー</h2><span class="en anchor-tag">#3d</span></div>
    <div class="grid-2">
      <div>
        <p>構造物・地形を高精度でデジタル化。既存構造物のBIM／CIMモデル化、災害調査、出来形管理などで威力を発揮します。</p>
        <ul style="margin-top:12px; padding-left:20px; list-style:disc; font-size:14px;">
          <li>点群データ取得・後処理</li>
          <li>BIM／CIM連携</li>
          <li>変位観測・出来形計測</li>
        </ul>
      </div>
      <div class="img-ph large">3Dスキャナー IMAGE</div>
    </div>
  </div>
</section>

<section id="gnss">
  <div class="wrap">
    <div class="sec-h"><h2>GNSS 測位</h2><span class="en anchor-tag">#gnss</span></div>
    <p class="section-lead">ネットワーク型RTK-GNSSの活用で、基準点の設置・観測を効率化。社内ではGNSS勉強会も継続的に実施し、技術者のスキル底上げを図っています。</p>
    <div class="img-ph wide">GNSS 現場カット IMAGE</div>
  </div>
</section>

<section id="workflow" style="background:#f5f5f5;">
  <div class="wrap">
    <div class="sec-h"><h2>作業工程の可視化</h2><span class="en anchor-tag">#workflow</span></div>
    <p class="section-lead">「測量って何をしているの？」を、動画・アニメーションでわかりやすく紹介。若手・未経験者にも仕事の中身が伝わる構成です。</p>
    <div class="img-ph wide">作業工程アニメ／動画 プレースホルダー</div>
  </div>
</section>

<section id="allrounder">
  <div class="wrap">
    <div class="sec-h"><h2>全国対応・多分野の実績</h2><span class="en anchor-tag">#allrounder</span></div>
    <p class="section-lead">担当者様の異動先までお声がけいただくケースが多く、結果として全国規模で実績を重ねてきました。分野も、道路・橋梁・河川・造成・トンネルと幅広くカバーしています。</p>
    <div class="numbers">
      <div class="num-item"><div class="num-value">全国</div><div class="num-label">対応エリア</div></div>
      <div class="num-item"><div class="num-value">5+</div><div class="num-label">工事分野</div></div>
      <div class="num-item"><div class="num-value">2007年〜</div><div class="num-label">派遣実績</div></div>
      <div class="num-item"><div class="num-value">3事業</div><div class="num-label">一貫対応</div></div>
    </div>
  </div>
</section>

<section style="background:#eee;"><div class="wrap"><div class="cta-box"><div class="cta-txt">技術のご相談はお気軽に。</div><a href="contact.html" class="btn">お問い合わせ</a></div></div></section>
'''

# ------------------------------------------------------------
# ABOUT（1ページアンカー）
# ------------------------------------------------------------
ABOUT = '''
<section class="page-hero"><div class="wrap"><div class="en">ABOUT</div><h1>会社案内</h1></div></section>
<div class="breadcrumb"><div class="wrap"><a href="home.html">ホーム</a> ／ 会社案内</div></div>

<nav class="section-nav"><div class="wrap"><ul>
  <li><a href="#greeting">代表あいさつ</a></li>
  <li><a href="#founder">創業者の想い</a></li>
  <li><a href="#company">会社概要</a></li>
  <li><a href="#history">沿革</a></li>
  <li><a href="#clients">主要取引先</a></li>
  <li><a href="#access">アクセス</a></li>
</ul></div></nav>

<!-- 代表あいさつ -->
<section id="greeting">
  <div class="wrap">
    <div class="sec-h"><h2>代表あいさつ</h2><span class="en anchor-tag">#greeting</span></div>
    <div class="grid-2">
      <div class="img-ph large">代表 ポートレート IMAGE</div>
      <div>
        <h3 style="margin-bottom:12px; font-size:20px;">「はかる」技術を、「ものづくり」の現場へ。</h3>
        <p>当社は、公共測量・工事測量で培った「はかる」技術を「ものづくり」の現場で活かすことをコンセプトに、「建設工事の施工管理及び工事測量のパイオニア」として1981年（昭和56年）に設立いたしました。創業以来、顧客企業様をはじめ様々な方のご理解・ご支援を賜り、心より感謝申し上げます。</p>
        <p style="margin-top:12px;">私共は今後も顧客の皆様の立場に立ち、早く・安く・良く（技術屋の良心）、安心・安全をモットーに、技術力を提供し、社会に貢献したいと考えておりますので、いっそうのお引立てをお願い申し上げます。</p>
        <p style="margin-top:24px; font-size:13px; color:#666;">代表取締役社長　灰佐 計祐</p>
      </div>
    </div>
  </div>
</section>

<!-- 創業者の想い・ロゴの由来（2026-08-26 定例で掲載決定） -->
<section id="founder" style="background:#f5f5f5;">
  <div class="wrap">
    <div class="sec-h"><h2>創業者の想い ／ ロゴの由来</h2><span class="en anchor-tag">#founder</span></div>
    <div class="grid-2">
      <div>
        <div style="border-left:4px solid #333; background:#fff; padding:28px 32px; line-height:2;">
          <div style="font-size:19px; font-weight:700; line-height:1.9;">仕事があれば、一番に行こう。<br>仕事があれば、どこへでも行こう。<br>月へでも行くぞ。</div>
          <div style="font-size:11px; color:#888; font-family:monospace; margin-top:12px;">— 創業者・灰佐 英児（現会長）／ 2012年 社内資料より</div>
        </div>
        <p style="margin-top:16px;">1981年の創業以来、変わらない当社の原点です。フットワークと開拓者精神で、岡山・倉敷から全国の現場へ。この言葉は、いまも私たちの行動指針として受け継がれています。</p>
      </div>
      <div>
        <div class="img-ph medium">ロゴマーク IMAGE</div>
        <p style="margin-top:16px;"><b>ロゴの由来</b><br>三角形は「21世紀」をデザイン化したもの。他者の真似をせず、人の後についていかない——パイオニアスピリットを表しています。</p>
        <p style="margin-top:12px; font-size:12px; color:#888;">※ 原典資料は光田氏よりデータ化共有予定（9月中）。文言は共有後に確定。</p>
      </div>
    </div>
  </div>
</section>

<!-- 会社概要 -->
<section id="company">
  <div class="wrap">
    <div class="sec-h"><h2>会社概要</h2><span class="en anchor-tag">#company</span></div>
    <table class="info-table">
      <tr><th>商号</th><td>株式会社 第二開発技工</td></tr>
      <tr><th>本社所在地</th><td>〒710-0845 岡山県倉敷市西富井446-2<br>TEL: 086-423-1899 ／ FAX: 086-423-2034</td></tr>
      <tr><th>代表者</th><td>代表取締役社長　灰佐 計祐</td></tr>
      <tr><th>創業・設立</th><td>昭和56年（1981年）12月</td></tr>
      <tr><th>資本金</th><td>1,000万円</td></tr>
      <tr><th>加盟団体</th><td>社団法人 日本測量協会<br>社団法人 岡山県測量設計業協会<br>倉敷測量設計業協会<br>倉敷地区測量設計事業協同組合</td></tr>
      <tr><th>営業種目</th><td>測量・土木設計・地質調査<br>施工管理（労働者派遣事業）<br>各種許認可申請</td></tr>
      <tr><th>許可・登録</th><td>測量業登録　大臣(6)-18685号<br>労働者派遣事業許可　派33-300110号<br>補償コンサルタント業登録　補29-4015号</td></tr>
    </table>
  </div>
</section>

<!-- 沿革 -->
<section id="history">
  <div class="wrap">
    <div class="sec-h"><h2>沿革</h2><span class="en anchor-tag">#history</span></div>
    <table class="info-table">
      <tr><th>昭和56年12月<br><span style="font-weight:400; color:#666; font-size:12px;">1981年</span></th><td>有限会社 第二開発技工として設立<br>測量業登録</td></tr>
      <tr><th>昭和58年6月<br><span style="font-weight:400; color:#666; font-size:12px;">1983年</span></th><td>資本金500万円に増額</td></tr>
      <tr><th>昭和61年8月<br><span style="font-weight:400; color:#666; font-size:12px;">1986年</span></th><td>倉敷市西富井に本社移転</td></tr>
      <tr><th>平成元年7月<br><span style="font-weight:400; color:#666; font-size:12px;">1989年</span></th><td>株式会社 第二開発技工に組織変更<br>資本金1,000万円に増額</td></tr>
      <tr><th>平成13年11月<br><span style="font-weight:400; color:#666; font-size:12px;">2001年</span></th><td>建設業許可</td></tr>
      <tr><th>平成14年1月<br><span style="font-weight:400; color:#666; font-size:12px;">2002年</span></th><td>補償コンサルタント業登録</td></tr>
      <tr><th>平成18年5月<br><span style="font-weight:400; color:#666; font-size:12px;">2006年</span></th><td>労働者派遣事業許可</td></tr>
      <tr><th>平成27年4月<br><span style="font-weight:400; color:#666; font-size:12px;">2015年</span></th><td>代表者交代<br>　代表取締役社長　灰佐 英児　代表取締役会長に就任<br>　取締役専務　　　灰佐 計祐　代表取締役社長に就任</td></tr>
      <tr><th>令和3年7月<br><span style="font-weight:400; color:#666; font-size:12px;">2021年</span></th><td>3次元空撮地形構造物処理システム導入</td></tr>
      <tr><th>令和8年<br><span style="font-weight:400; color:#666; font-size:12px;">2026年</span></th><td>コーポレートサイトリニューアル</td></tr>
    </table>
  </div>
</section>

<!-- 主要取引先 -->
<section id="clients">
  <div class="wrap">
    <div class="sec-h"><h2>主要取引先</h2><span class="en anchor-tag">#clients</span></div>
    <p class="section-lead">官公庁・ゼネコン・地域建設会社まで、全国規模でお取引をいただいております（五十音順・敬称略）。</p>
    <div class="grid-3" style="gap:0; border-top:1px solid #ccc; border-left:1px solid #ccc;">
      <div style="padding:14px 20px; border-right:1px solid #ccc; border-bottom:1px solid #ccc;">天野産業株式会社</div>
      <div style="padding:14px 20px; border-right:1px solid #ccc; border-bottom:1px solid #ccc;">株式会社 荒木組</div>
      <div style="padding:14px 20px; border-right:1px solid #ccc; border-bottom:1px solid #ccc;">宇部興産機械株式会社</div>
      <div style="padding:14px 20px; border-right:1px solid #ccc; border-bottom:1px solid #ccc;">株式会社 大本組</div>
      <div style="padding:14px 20px; border-right:1px solid #ccc; border-bottom:1px solid #ccc;">岡山県</div>
      <div style="padding:14px 20px; border-right:1px solid #ccc; border-bottom:1px solid #ccc;">鹿島建設株式会社</div>
      <div style="padding:14px 20px; border-right:1px solid #ccc; border-bottom:1px solid #ccc;">極東興和株式会社</div>
      <div style="padding:14px 20px; border-right:1px solid #ccc; border-bottom:1px solid #ccc;">倉敷市</div>
      <div style="padding:14px 20px; border-right:1px solid #ccc; border-bottom:1px solid #ccc;">株式会社 三幸工務店</div>
      <div style="padding:14px 20px; border-right:1px solid #ccc; border-bottom:1px solid #ccc;">世紀東急工業株式会社</div>
      <div style="padding:14px 20px; border-right:1px solid #ccc; border-bottom:1px solid #ccc;">瀧上工業株式会社</div>
      <div style="padding:14px 20px; border-right:1px solid #ccc; border-bottom:1px solid #ccc;">東急建設株式会社</div>
      <div style="padding:14px 20px; border-right:1px solid #ccc; border-bottom:1px solid #ccc;">株式会社 ピーエス三菱</div>
      <div style="padding:14px 20px; border-right:1px solid #ccc; border-bottom:1px solid #ccc;">株式会社 富士ピー・エス</div>
      <div style="padding:14px 20px; border-right:1px solid #ccc; border-bottom:1px solid #ccc;">前田建設工業株式会社</div>
    </div>
  </div>
</section>

<!-- アクセス -->
<section id="access">
  <div class="wrap">
    <div class="sec-h"><h2>アクセス</h2><span class="en anchor-tag">#access</span></div>
    <div class="grid-2">
      <div>
        <table class="info-table">
          <tr><th>所在地</th><td>〒710-0845 岡山県倉敷市西富井446-2</td></tr>
          <tr><th>TEL</th><td>086-423-1899</td></tr>
          <tr><th>FAX</th><td>086-423-2034</td></tr>
        </table>
      </div>
      <div class="img-ph large">GOOGLE MAP EMBED</div>
    </div>
  </div>
</section>

<section style="background:#eee;"><div class="wrap"><div class="cta-box"><div class="cta-txt">お問い合わせはこちらから</div><a href="contact.html" class="btn">お問い合わせ</a></div></div></section>
'''

# ------------------------------------------------------------
# 社会活動（トップメニュー・災害時支援／ドローン測量が中心）
# ------------------------------------------------------------
SOCIAL = '''
<section class="page-hero"><div class="wrap"><div class="en">SOCIAL ACTIVITIES</div><h1>社会活動</h1></div></section>
<div class="breadcrumb"><div class="wrap"><a href="home.html">ホーム</a> ／ 社会活動</div></div>

<!-- イントロダクション -->
<section>
  <div class="wrap">
    <div class="sec-h"><h2>"はかる技術"で、地域の安全を支える。</h2><span class="en">INTRODUCTION</span></div>
    <p class="section-lead" style="font-size:16px; color:#333; max-width:820px;">
      私たちの仕事は、まちのインフラをつくる工程の一部です。<br>
      だからこそ、まちが傷ついたときにも動ける準備を、日ごろから続けています。
    </p>
    <p>岡山県倉敷市に本拠を置き、地元のまちづくり・インフラ整備・防災に関わり続けてきました。地域社会と共に歩む測量会社として、平時の業務にとどまらず、災害時の緊急測量支援・地域活動・次世代育成にも取り組んでいます。</p>
  </div>
</section>

<!-- 災害時の測量支援 -->
<section style="background:#f5f5f5;">
  <div class="wrap">
    <div class="sec-h"><h2>災害時の測量支援</h2><span class="en">DISASTER RESPONSE</span></div>
    <div class="grid-2">
      <div class="img-ph large">被災地での緊急測量 IMAGE</div>
      <div>
        <h3 style="margin-bottom:12px; font-size:18px;">災害の前と後に立つ、測量の仕事</h3>
        <p><b>[ 災害の前 ]</b><br>地盤・地形の変化を計測し、リスクの高い箇所を可視化する。日常の測量業務で得たデータが、防災の基礎資料になります。</p>
        <p style="margin-top:12px;"><b>[ 災害の後 ]</b><br>被災地の状況を素早く測量し、復旧計画に必要な"最初のデータ"を提供する。道路・河川・宅地——復旧の判断材料は、正確な計測から生まれます。</p>
        <p style="margin-top:12px;">私たちは<b>岡山県測量設計業協会</b>に加盟し、地域の測量会社としての社会的責任を果たすべく、有事の際にはすぐに動ける体制を維持しています。</p>
      </div>
    </div>
  </div>
</section>

<!-- 災害時におけるドローン測量 -->
<section>
  <div class="wrap">
    <div class="sec-h"><h2>災害時におけるドローン測量</h2><span class="en">DRONE FOR DISASTER</span></div>
    <p class="section-lead">私たちは<b>3次元空撮地形構造物処理システム</b>を導入しています。ドローンによる空撮は、災害時に「早く・広く・安全に」現場を捉えるための、いまや欠かせない手段です。</p>

    <div class="grid-3" style="margin-top:32px;">
      <div class="card">
        <div class="img-ph medium">迅速な被災把握</div>
        <div class="card-title">01. 迅速な被災状況の把握</div>
        <p>広範囲の被災地を、上空から短時間で計測。地上からのアクセスが困難なエリアも、その日のうちに状況を捉えられます。</p>
      </div>
      <div class="card">
        <div class="img-ph medium">非接触計測</div>
        <div class="card-title">02. 危険箇所への非接触計測</div>
        <p>崩落現場・浸水域・地滑り箇所など、人が入れない危険地帯でも、ドローンならリスクなしで計測が可能です。</p>
      </div>
      <div class="card">
        <div class="img-ph medium">3Dモデル生成</div>
        <div class="card-title">03. 3Dモデル・点群での可視化</div>
        <p>被災前後の地形を3次元で比較。土砂の流出量、変位、崩落規模などを数値で把握し、復旧計画の初動を早めます。</p>
      </div>
    </div>

    <h3 style="margin:48px 0 16px;">対応可能な災害シーン</h3>
    <table class="info-table">
      <tr><th>豪雨・河川氾濫</th><td>浸水域の空撮、河川護岸の被災範囲把握、堆積土砂量の算定</td></tr>
      <tr><th>土砂災害・地滑り</th><td>崩落斜面の3Dモデル生成、土量計算、二次災害リスクエリアの可視化</td></tr>
      <tr><th>地震</th><td>地表の変位計測、道路・構造物の損傷把握、被災地の広域概観</td></tr>
      <tr><th>その他</th><td>台風被害、火災跡地、地盤沈下 等の緊急計測に対応</td></tr>
    </table>

    <div class="cta-box" style="margin-top:32px;">
      <div class="cta-txt">災害時の緊急測量ご依頼<br>まずはお電話ください。</div>
      <div style="display:flex; gap:12px;"><a href="tel:0864231899" class="btn">086-423-1899</a><a href="contact.html" class="btn outline">お問い合わせフォーム</a></div>
    </div>
  </div>
</section>

<!-- 地域活動・貢献 -->
<section style="background:#f5f5f5;">
  <div class="wrap">
    <div class="sec-h"><h2>地域活動・貢献</h2><span class="en">COMMUNITY</span></div>
    <p class="section-lead">まちのインフラをつくる仕事と地続きで、地域社会への貢献にも取り組んでいます。</p>
    <div class="grid-2">
      <div>
        <h3 style="margin-bottom:12px; font-size:18px;">加盟団体を通じた活動</h3>
        <ul style="padding-left:20px; list-style:disc; font-size:14px; line-height:1.9;">
          <li>社団法人 日本測量協会</li>
          <li>社団法人 岡山県測量設計業協会</li>
          <li>倉敷測量設計業協会</li>
          <li>倉敷地区測量設計事業協同組合</li>
        </ul>
        <p style="margin-top:16px; font-size:13px; color:#555;">業界団体を通じた技術交流、地域の防災協力、若手技術者の育成活動に参加しています。</p>
      </div>
      <div class="img-ph large">地域活動 IMAGE</div>
    </div>
  </div>
</section>

<!-- 次世代の育成 -->
<section>
  <div class="wrap">
    <div class="sec-h"><h2>次世代の育成</h2><span class="en">NEXT GENERATION</span></div>
    <p class="section-lead">測量技術者の高齢化が進むなか、次の世代を育てることも私たちの社会的責任です。未経験者を受け入れ、社内で育てる仕組みを整え、地域の技術を次に手渡していきます。</p>
    <div class="grid-3">
      <div class="card"><div class="card-title">GNSS勉強会の継続開催</div><p>社内で技術勉強会を定期的に開催。若手・ベテランが一緒に学ぶ場を設けています。</p></div>
      <div class="card"><div class="card-title">未経験者の受け入れ</div><p>「測量って何？」から始まる方も歓迎。約1年で基本業務を習得できる育成プログラム。</p></div>
      <div class="card"><div class="card-title">資格取得の支援</div><p>測量士補・測量士など、キャリアに必要な資格の取得を会社としてサポート。</p></div>
    </div>
  </div>
</section>

<section style="background:#eee;"><div class="wrap"><div class="cta-box"><div class="cta-txt">災害時の緊急対応・地域活動のご相談</div><div style="display:flex; gap:12px;"><a href="tel:0864231899" class="btn">086-423-1899</a><a href="contact.html" class="btn outline">お問い合わせ</a></div></div></div></section>
'''

# ------------------------------------------------------------
# RECRUIT
# ------------------------------------------------------------
RECRUIT = '''
<section class="page-hero"><div class="wrap"><div class="en">RECRUIT</div><h1>採用情報</h1></div></section>
<div class="breadcrumb"><div class="wrap"><a href="home.html">ホーム</a> ／ 採用情報</div></div>

<nav class="section-nav"><div class="wrap"><ul>
  <li><a href="#top">採用トップ</a></li>
  <li><a href="#jobs">募集要項</a></li>
  <li><a href="#first-step">未経験からの1年</a></li>
  <li><a href="#support">資格取得支援</a></li>
  <li><a href="#people">社員紹介</a></li>
  <li><a href="#faq">よくある質問</a></li>
</ul></div></nav>

<!-- 採用トップ -->
<section id="top">
  <div class="wrap">
    <div class="sec-h"><h2>はかることから、はじまる仕事があります。</h2><span class="en anchor-tag">#top</span></div>
    <div class="grid-2">
      <div class="img-ph large">若手スタッフ 現場カット IMAGE</div>
      <div>
        <p>「測量って、何をする仕事？」</p>
        <p style="margin-top:12px;">その問いから始まる方を、私たちは歓迎します。学生時代の専攻も、それまでの職歴も、関係ありません。大切なのは、"新しいことを覚えたい"という気持ちだけです。</p>
        <p style="margin-top:12px;">約1年で基本業務を習得し、ドローン・3Dスキャナーといった先端技術に触れながら、測量作業員から施工管理技術者へキャリアアップできる——それが、この会社の面白さです。</p>
        <div style="margin-top:24px; display:flex; gap:12px;"><a href="contact.html" class="btn">エントリーする</a><a href="#faq" class="btn outline">よくある質問</a></div>
      </div>
    </div>

    <!-- 先代からのメッセージ（2026-08-26 定例で掲載決定） -->
    <div style="margin-top:48px; background:#f5f5f5; border:1px solid #ccc; padding:32px 36px;">
      <div style="font-family:monospace; font-size:10px; letter-spacing:0.25em; color:#888; margin-bottom:12px;">FOUNDER'S SPIRIT</div>
      <div style="font-size:22px; font-weight:700; line-height:1.9;">仕事があれば、一番に行こう。<br>仕事があれば、どこへでも行こう。月へでも行くぞ。</div>
      <p style="margin-top:16px; font-size:13.5px; color:#555; line-height:1.9;">1981年の創業のとき、先代が書き残した言葉です。他者の真似をしない。人の後についていかない。そのパイオニアスピリットは、ドローンや3Dスキャナーといった新しい技術に真っ先に挑む、いまの私たちにそのまま受け継がれています。<a href="about.html#founder" style="color:#222;">→ 創業者の想い・ロゴの由来</a></p>
    </div>

    <h3 style="margin:48px 0 16px;">こんな方を歓迎しています</h3>
    <div class="numbers">
      <div class="num-item"><div class="num-value">未経験</div><div class="num-label">歓迎</div></div>
      <div class="num-item"><div class="num-value">若手</div><div class="num-label">重点採用</div></div>
      <div class="num-item"><div class="num-value">女性</div><div class="num-label">活躍中</div></div>
      <div class="num-item"><div class="num-value">全国</div><div class="num-label">の現場</div></div>
    </div>
  </div>
</section>

<!-- 募集要項 -->
<section id="jobs">
  <div class="wrap">
    <div class="sec-h"><h2>募集要項</h2><span class="en anchor-tag">#jobs</span></div>
    <div class="grid-3">
      <div class="card">
        <div class="img-ph medium">測量助手</div>
        <div class="card-title">測量助手（未経験可・35歳以下）</div>
        <p>測量現場のサポート業務からスタート。器械の設置、記帳、後方整理などを通じて、測量の基本を学びます。</p>
        <ul style="margin-top:8px; padding-left:20px; list-style:disc; font-size:12px; color:#555;">
          <li>資格不要</li>
          <li>普通自動車免許（AT可）</li>
          <li>入社後に測量士補取得を支援</li>
        </ul>
      </div>
      <div class="card">
        <div class="img-ph medium">測量作業員</div>
        <div class="card-title">測量作業員</div>
        <p>測量業務全般を担当。TS・GNSS・ドローン等の機材操作を含む、現場の主軸を担う仕事です。</p>
        <ul style="margin-top:8px; padding-left:20px; list-style:disc; font-size:12px; color:#555;">
          <li>測量士補以上（または同等の実務経験）</li>
          <li>普通自動車免許（AT可）</li>
          <li>測量士取得を支援</li>
        </ul>
      </div>
      <div class="card">
        <div class="img-ph medium">施工管理技術者</div>
        <div class="card-title">施工管理技術者</div>
        <p>工事現場に派遣され、施工管理業務を担当。測量経験を活かして、精度の高い管理をおこないます。</p>
        <ul style="margin-top:8px; padding-left:20px; list-style:disc; font-size:12px; color:#555;">
          <li>土木施工管理技士 または同等の実務経験</li>
          <li>普通自動車免許（AT可）</li>
          <li>資格取得支援あり</li>
        </ul>
      </div>
    </div>
    <div class="cta-box" style="margin-top:32px;"><div class="cta-txt">興味を持たれた方はエントリーへ</div><a href="contact.html" class="btn">エントリーフォームへ</a></div>
  </div>
</section>

<!-- 未経験からの1年 -->
<section id="first-step" style="background:#f5f5f5;">
  <div class="wrap">
    <div class="sec-h"><h2>未経験からの1年 ／ キャリアパス</h2><span class="en anchor-tag">#first-step</span></div>
    <p class="section-lead">「1年後に何ができるようになっているか」を、はっきりお伝えします。イメージが持てれば、未経験でも安心してスタートできます。</p>

    <div class="grid-4">
      <div class="card"><div class="card-meta">MONTH 1-3</div><div class="card-title">まずは"見る"</div><p>先輩の現場に同行し、機材と作業の流れを覚える。安全講習・器械操作の基礎。</p></div>
      <div class="card"><div class="card-meta">MONTH 4-6</div><div class="card-title">"手を動かす"</div><p>器械の据付、記帳、簡単な観測を任される。図面の読み方も並行して学習。</p></div>
      <div class="card"><div class="card-meta">MONTH 7-9</div><div class="card-title">"任される"</div><p>小規模現場を担当。ドローン・3Dスキャナーの基本操作を習得。</p></div>
      <div class="card"><div class="card-meta">MONTH 10-12</div><div class="card-title">"独り立ち"</div><p>測量作業員として現場を回せるように。測量士補資格の取得を目指す。</p></div>
    </div>

    <div style="border:2px solid #333; padding:32px; margin-top:32px; background:#fff;">
      <h3 style="margin-bottom:12px;">その先のキャリア</h3>
      <p>測量作業員として3〜5年経験を積んだ後、施工管理技術者へキャリアシフトする社員も多くいます。会社としても、この流れを積極的にサポートしています。</p>
    </div>
  </div>
</section>

<!-- 資格取得支援 -->
<section id="support">
  <div class="wrap">
    <div class="sec-h"><h2>資格取得支援</h2><span class="en anchor-tag">#support</span></div>
    <p class="section-lead">キャリアに必要な資格の取得を、会社としてバックアップします。</p>
    <table class="info-table">
      <tr><th>測量士補</th><td>受験料・テキスト代を会社負担／勤務時間内の学習時間を確保</td></tr>
      <tr><th>測量士</th><td>受験料・登録料を会社負担／実務経験のフォロー</td></tr>
      <tr><th>土木施工管理技士（2級／1級）</th><td>受験料・登録料を会社負担／過去問対策の勉強会あり</td></tr>
      <tr><th>ドローン国家資格</th><td>取得費用を会社負担／指定講習の受講機会</td></tr>
      <tr><th>その他</th><td>業務に関連する資格は個別相談。取得実績あり</td></tr>
    </table>
    <p style="font-size:12px; color:#666; margin-top:12px;">※ 詳細な運用ルール（勤続年数の要件・支給上限等）は入社時にご案内します。</p>
  </div>
</section>

<!-- 社員紹介 -->
<section id="people" style="background:#f5f5f5;">
  <div class="wrap">
    <div class="sec-h"><h2>社員紹介 ／ 1日の流れ</h2><span class="en anchor-tag">#people</span></div>
    <div class="grid-3">
      <div class="card">
        <div class="img-ph medium">社員写真 01</div>
        <div class="card-meta">測量作業員 ／ 入社3年目</div>
        <div class="card-title">「未経験からドローン操縦者に」</div>
        <p style="font-size:13px;">前職は接客業。まったく違う世界に飛び込みましたが、先輩がゼロから教えてくれたので不安はありませんでした。</p>
      </div>
      <div class="card">
        <div class="img-ph medium">社員写真 02</div>
        <div class="card-meta">施工管理技術者 ／ 入社12年目</div>
        <div class="card-title">「測量から施工管理へシフト」</div>
        <p style="font-size:13px;">測量の現場感覚があるからこそ、施工管理で"実際に施工可能な計画"が立てられる。この会社のキャリアパスの強みです。</p>
      </div>
      <div class="card">
        <div class="img-ph medium">社員写真 03</div>
        <div class="card-meta">測量作業員 ／ 入社5年目</div>
        <div class="card-title">「女性でも、現場は変わりません」</div>
        <p style="font-size:13px;">最初は「女性でも大丈夫？」と聞かれることが多かったけど、機材が軽くなり、現場も進化しています。</p>
      </div>
    </div>

    <h3 style="margin:48px 0 16px;">ある日のスケジュール</h3>
    <table class="info-table">
      <tr><th>7:30</th><td>出社／機材・車両の準備、当日の作業内容確認</td></tr>
      <tr><th>8:00</th><td>現場到着／安全確認、作業開始</td></tr>
      <tr><th>12:00</th><td>お昼休憩（現場近くで各自）</td></tr>
      <tr><th>13:00</th><td>午後の観測・記帳</td></tr>
      <tr><th>16:30</th><td>撤収／会社へ戻り、データ整理・報告書作成</td></tr>
      <tr><th>17:30</th><td>退社</td></tr>
    </table>
  </div>
</section>

<!-- FAQ -->
<section id="faq">
  <div class="wrap">
    <div class="sec-h"><h2>よくある質問</h2><span class="en anchor-tag">#faq</span></div>
    <div style="border-top:1px solid #ccc;">
      <div style="border-bottom:1px solid #ccc; padding:16px 0;"><b>Q. 未経験でも本当に大丈夫ですか？</b><p style="margin-top:8px; font-size:13px; color:#555;">A. 未経験からスタートした社員が多数在籍しています。約1年で基本業務を習得できるカリキュラムを用意しています。</p></div>
      <div style="border-bottom:1px solid #ccc; padding:16px 0;"><b>Q. 年齢制限はありますか？</b><p style="margin-top:8px; font-size:13px; color:#555;">A. 職種によっては年齢の目安があります（例：測量助手は35歳以下）。詳しくは募集要項をご確認ください。</p></div>
      <div style="border-bottom:1px solid #ccc; padding:16px 0;"><b>Q. 転勤はありますか？</b><p style="margin-top:8px; font-size:13px; color:#555;">A. 本社勤務が基本ですが、現場は全国に及ぶことがあります。長期の出張については事前にご相談・調整いたします。</p></div>
      <div style="border-bottom:1px solid #ccc; padding:16px 0;"><b>Q. 女性でも働けますか？</b><p style="margin-top:8px; font-size:13px; color:#555;">A. 現在も女性社員が現場で活躍しています。機材の軽量化・現場環境の改善が進み、性別を問わず活躍できる環境です。</p></div>
      <div style="border-bottom:1px solid #ccc; padding:16px 0;"><b>Q. 資格がないと応募できませんか？</b><p style="margin-top:8px; font-size:13px; color:#555;">A. 測量助手は資格不要です。入社後に測量士補などの資格取得を会社が支援します。</p></div>
      <div style="border-bottom:1px solid #ccc; padding:16px 0;"><b>Q. 繁忙期はいつですか？</b><p style="margin-top:8px; font-size:13px; color:#555;">A. 公共工事の年度末（1〜3月）は繁忙期になります。事前に予定を組み、無理のない働き方ができるよう調整しています。</p></div>
    </div>
  </div>
</section>

<section style="background:#eee;"><div class="wrap"><div class="cta-box"><div class="cta-txt">エントリー・お問い合わせはこちら</div><a href="contact.html" class="btn">エントリーフォームへ</a></div></div></section>
'''

# ------------------------------------------------------------
# NEWS
# ------------------------------------------------------------
NEWS = '''
<section class="page-hero"><div class="wrap"><div class="en">NEWS</div><h1>ニュース</h1></div></section>
<div class="breadcrumb"><div class="wrap"><a href="home.html">ホーム</a> ／ ニュース</div></div>

<section>
  <div class="wrap">
    <div style="display:flex; gap:8px; margin-bottom:24px;">
      <div style="padding:8px 16px; background:#333; color:#fff; font-size:13px;">すべて</div>
      <div style="padding:8px 16px; background:#f5f5f5; color:#333; font-size:13px;">お知らせ</div>
      <div style="padding:8px 16px; background:#f5f5f5; color:#333; font-size:13px;">技術</div>
      <div style="padding:8px 16px; background:#f5f5f5; color:#333; font-size:13px;">採用</div>
    </div>

    <div class="news-list">
      <div class="news-item"><div class="news-date">2026.07.XX</div><div class="news-cat">お知らせ</div><div class="news-title">コーポレートサイトをリニューアルしました</div></div>
      <div class="news-item"><div class="news-date">2023.11.14</div><div class="news-cat">お知らせ</div><div class="news-title">労働者派遣法に基づく情報公開</div></div>
      <div class="news-item"><div class="news-date">2021.07.09</div><div class="news-cat">技術</div><div class="news-title">3次元空撮地形構造物処理システムを導入しました</div></div>
      <div class="news-item"><div class="news-date">2020.01.XX</div><div class="news-cat">お知らせ</div><div class="news-title">新年のご挨拶</div></div>
      <div class="news-item"><div class="news-date">2015.02.XX</div><div class="news-cat">お知らせ</div><div class="news-title">代表者交代のご挨拶</div></div>
      <div class="news-item"><div class="news-date">2014.06.XX</div><div class="news-cat">技術</div><div class="news-title">GNSS勉強会を実施しました</div></div>
      <div class="news-item"><div class="news-date">2014.05.XX</div><div class="news-cat">採用</div><div class="news-title">新入社員が入社しました</div></div>
      <div class="news-item"><div class="news-date">2013.09.XX</div><div class="news-cat">技術</div><div class="news-title">スキルアップ勉強会を開きました</div></div>
      <div class="news-item"><div class="news-date">2013.07.XX</div><div class="news-cat">お知らせ</div><div class="news-title">ホームページをリニューアルしました</div></div>
    </div>
  </div>
</section>
'''

# ------------------------------------------------------------
# CONTACT
# ------------------------------------------------------------
CONTACT = '''
<section class="page-hero"><div class="wrap"><div class="en">CONTACT</div><h1>お問い合わせ</h1></div></section>
<div class="breadcrumb"><div class="wrap"><a href="home.html">ホーム</a> ／ お問い合わせ</div></div>

<section>
  <div class="wrap">
    <div class="sec-h"><h2>お問い合わせ種別を選択してください</h2></div>
    <div class="grid-3">
      <div class="card"><div class="card-title">01. 業務のご相談</div><p>測量・調査・設計・施工管理のご依頼、お見積り、技術的なご相談。</p></div>
      <div class="card"><div class="card-title">02. 採用に関するお問い合わせ</div><p>求人へのエントリー、会社見学、インターンシップのご相談。</p></div>
      <div class="card"><div class="card-title">03. その他・取材</div><p>取材依頼、パートナー企業からのご連絡、その他。</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-h"><h2>お問い合わせフォーム</h2></div>
    <form>
      <div class="form-row">
        <label>お問い合わせ種別</label>
        <select>
          <option>業務のご相談</option>
          <option>採用に関するお問い合わせ</option>
          <option>その他・取材</option>
        </select>
      </div>
      <div class="form-row"><label>お名前</label><input type="text" placeholder="例）山田 太郎"></div>
      <div class="form-row"><label>会社名（任意）</label><input type="text"></div>
      <div class="form-row"><label>メールアドレス</label><input type="email" placeholder="example@example.com"></div>
      <div class="form-row"><label>電話番号（任意）</label><input type="tel"></div>
      <div class="form-row"><label>お問い合わせ内容</label><textarea placeholder="ご相談内容をご記入ください"></textarea></div>
      <div class="form-row"><label><input type="checkbox"> プライバシーポリシーに同意する</label></div>
      <div style="margin-top:24px;"><button type="submit" class="btn">送信する</button></div>
    </form>
  </div>
</section>

<section style="background:#f5f5f5;">
  <div class="wrap">
    <div class="sec-h"><h2>お電話でのお問い合わせ</h2></div>
    <div class="grid-2">
      <div>
        <p style="font-size:32px; font-weight:700; color:#111;">086-423-1899</p>
        <p style="margin-top:8px; color:#555;">平日 9:00〜17:00（土日祝休み）</p>
      </div>
      <div>
        <p>FAX: 086-423-2034</p>
        <p style="margin-top:8px;">〒710-0845 岡山県倉敷市西富井446-2</p>
      </div>
    </div>
  </div>
</section>
'''

# ------------------------------------------------------------
# STATEMENTS（A〜G）
# ------------------------------------------------------------
STATEMENTS = [
    {
        'id': 'a',
        'angle': '王道 ／ 未来を測る',
        'tagline': '未来のかたちを、いま測る。',
        'body': (
            'まちの下には、たくさんの数字が眠っています。\n'
            '道路の中心線、河川の水位、宅地の勾配、橋脚の位置。\n'
            'そのひとつひとつを、私たちは正確に測ってきました。\n'
            '\n'
            'いま測っているものは、いつか誰かの通勤路になり、\n'
            '住む場所になり、まちの防災を支える護岸になります。\n'
            '\n'
            '私たちの仕事は、未来のかたちを先に見る仕事です。\n'
            '\n'
            '<b>未来のかたちを、いま測る。</b>'
        ),
    },
    {
        'id': 'b',
        'angle': '生活者視点 ／ 見えないインフラ',
        'tagline': 'まちの下に、私たちの仕事がある。',
        'body': (
            '朝、あなたが歩いた道。\n'
            '通勤で渡った橋。\n'
            '休日にでかけたショッピングモール。\n'
            '\n'
            'そのすべての「地面」は、\n'
            '誰かが正確に測ったところから始まっています。\n'
            '\n'
            '見えないけれど、確かにそこにある。\n'
            '私たちは、まちの下でずっと働く仕事です。\n'
            '\n'
            '<b>まちの下に、私たちの仕事がある。</b>'
        ),
    },
    {
        'id': 'c',
        'angle': '採用 ／ 未経験からの物語',
        'tagline': 'はかることから、はじまる。',
        'body': (
            '「測量って、何をする仕事？」\n'
            'そこから始まってくれる人を、私たちは待っています。\n'
            '\n'
            '学生時代の専攻も、それまでの職歴も、関係ありません。\n'
            '大切なのは、"新しいことを覚えたい"という気持ちだけ。\n'
            '\n'
            '約1年で、基本の仕事はひととおりできるようになります。\n'
            'ドローンを飛ばし、3Dスキャナーで地形をデジタル化する——\n'
            '「はかる」の常識も、いま更新されているところ。\n'
            '\n'
            '<b>はかることから、はじまる。</b>'
        ),
    },
    {
        'id': 'd',
        'angle': '技術 ／ 先端技術 × 測量',
        'tagline': '地図の続きは、ドローンが描いていく。',
        'body': (
            '手描きから、レーザーへ。\n'
            '巻尺から、GNSSへ。\n'
            '航空写真から、ドローンへ。\n'
            '\n'
            '測量の道具は、200年で変わり続けてきました。\n'
            'そしていま、地図はもう「線」ではなく、\n'
            '3次元の点群でできています。\n'
            '\n'
            'まちを、地形を、構造物を、丸ごとデジタル化する。\n'
            '私たちは、その最前線にいます。\n'
            '\n'
            '<b>地図の続きは、ドローンが描いていく。</b>'
        ),
    },
    {
        'id': 'e',
        'angle': '歴史 ／ 伊能忠敬から現代へ',
        'tagline': '200年ぶんの一歩を、この足で継ぐ。',
        'body': (
            '伊能忠敬が日本地図の測量を始めたのは、55歳のとき。\n'
            '彼が歩いた距離は、地球一周分にも及びました。\n'
            '\n'
            '道具は、量程車と間縄と、天体観測。\n'
            'いまの私たちから見れば、あまりに素朴な機材です。\n'
            '\n'
            'それでも、彼の仕事と私たちの仕事は、\n'
            '本質的なところで、まったく同じです。\n'
            '\n'
            '「まちの形を、正しく次の世代に手渡す」。\n'
            '\n'
            '<b>200年ぶんの一歩を、この足で継ぐ。</b>'
        ),
    },
    {
        'id': 'f',
        'angle': '社会性 ／ 地域と防災',
        'tagline': '災害の前と、災害の後に立つ。',
        'body': (
            '災害の前——\n'
            '地形の変化を測り、リスクの高い場所を見つけ出す。\n'
            '\n'
            '災害の後——\n'
            '被害の範囲を素早く測り、復旧計画の最初のデータを届ける。\n'
            '\n'
            'まちを支える仕事は、平時よりも有事のときに、\n'
            'その本当の価値が試されます。\n'
            '\n'
            '私たちは、岡山県の測量会社として、\n'
            '有事のときにすぐ動ける体制を守り続けています。\n'
            '\n'
            '<b>災害の前と、災害の後に立つ。</b>'
        ),
    },
    {
        'id': 'g',
        'angle': '問いかけ ／ 責任と誇り',
        'tagline': 'はかった数字は、誰の未来になりますか。',
        'body': (
            'あなたが今日出したその数字は、\n'
            '来年、道路の中心線になります。\n'
            '\n'
            '10年後、通学路になります。\n'
            '\n'
            '30年後、その道を、あなたのお子さんが歩きます。\n'
            '\n'
            '私たちの仕事の重みは、そういうところにあります。\n'
            '数字を軽く扱わない——それだけが、\n'
            '「技術屋の良心」を守る唯一の方法です。\n'
            '\n'
            '<b>はかった数字は、誰の未来になりますか。</b>'
        ),
    },
]

def build_statement(idx, s):
    nav_items = ''.join(
        f'<a class="{"current" if t["id"] == s["id"] else ""}" href="statement-{t["id"]}.html">{t["id"].upper()}</a>'
        for t in STATEMENTS
    )
    prev_link = f'<a href="statement-{STATEMENTS[idx-1]["id"]}.html">← 前へ ({STATEMENTS[idx-1]["id"].upper()})</a>' if idx > 0 else '<span style="color:#999;">← 前へ</span>'
    next_link = f'<a href="statement-{STATEMENTS[idx+1]["id"]}.html">次へ ({STATEMENTS[idx+1]["id"].upper()}) →</a>' if idx < len(STATEMENTS)-1 else '<span style="color:#999;">次へ →</span>'

    body_html = s['body'].replace('\n', '<br>')
    inner = f'''
<nav class="slide-nav"><div class="wrap">
  <div class="items">{nav_items}</div>
  <div class="prev-next">{prev_link} ／ <a href="index.html">一覧</a> ／ {next_link}</div>
</div></nav>

<section class="slide">
  <div class="wrap">
    <span class="label"><b>{s["id"].upper()}</b>{s["angle"]}</span>
    <div class="tagline">{s["tagline"]}</div>
    <div class="body">{body_html}</div>
    <div class="meta">STATEMENT {s["id"].upper()} ／ D2 KAIHATSU GIKO ／ 2026</div>
  </div>
</section>
'''
    return page(f'ステートメント {s["id"].upper()} ／ {s["tagline"]}',
                f'STATEMENT {s["id"].upper()} ／ {s["angle"]}', inner)

# ------------------------------------------------------------
# INDEX
# ------------------------------------------------------------
def build_index():
    st_cards = ''
    for s in STATEMENTS:
        st_cards += f'''
        <div class="st-card">
          <div class="st-label">{s["id"].upper()}</div>
          <div class="st-angle">{s["angle"]}</div>
          <div class="st-tagline">{s["tagline"]}</div>
          <a href="statement-{s["id"]}.html" class="link">開く</a>
        </div>'''

    pages_data = [
        ('01', 'ホーム', '/', 'ヒーロー（スコープ／スカウター風演出）、3事業、強み、ブランド抜粋、ニュース、採用CTA。', 'home.html'),
        ('02', '事業案内', '/service/', 'イントロ＋サービス3事業のインデックスページ。', 'service.html'),
        ('03', 'SERVICE ／ 測量', '/service/survey/', '公共測量／工事測量／全国対応／取扱機材／作業フロー。', 'service-survey.html'),
        ('04', 'SERVICE ／ 調査・設計', '/service/design/', '土木設計／地質調査／環境調査／設計照査。', 'service-design.html'),
        ('05', 'SERVICE ／ 施工管理', '/service/management/', '測量会社ならではの強み／派遣スキーム／派遣実績。', 'service-management.html'),
        ('06', '強み・技術', '/strengths/', '伊能忠敬〜現代テックのイントロ＋ドローン／3Dスキャナー／GNSS／作業工程／全国対応。<br>アンカー: #drone #3d #gnss #workflow #allrounder', 'strengths.html'),
        ('07', '社会活動', '/social/', '災害時の測量支援／災害時におけるドローン測量／地域活動・貢献／次世代育成。', 'social.html'),
        ('08', '会社案内（ABOUT）', '/about/', '代表あいさつ／会社概要／沿革／主要取引先／アクセスの1ページ集約。<br>アンカー: #greeting #company #history #clients #access', 'about.html'),
        ('09', '採用情報', '/recruit/', '採用トップ／募集要項／未経験からの1年／資格支援／社員紹介／FAQ。<br>アンカー: #top #jobs #first-step #support #people #faq', 'recruit.html'),
        ('10', 'ニュース', '/news/', 'カテゴリ絞込＋一覧。既存9本の移行想定。', 'news.html'),
        ('11', 'お問い合わせ', '/contact/', '業務／採用／取材の3種別＋フォーム＋電話案内。', 'contact.html'),
    ]
    page_cards = ''
    for n, title, url, desc, href in pages_data:
        page_cards += f'''
        <div class="page-card">
          <div class="n">{n}</div>
          <h2>{title}</h2>
          <p>{desc}</p>
          <div class="anchors">{url}</div>
          <a href="{href}" class="link">開く</a>
        </div>'''

    design_cards = ''
    for n, title, url, desc, href in pages_data:
        d_href = 'design-top.html' if href == 'home.html' else 'design-' + href
        design_cards += f'''
        <div class="page-card">
          <div class="n">D-{n}</div>
          <h2>{title}</h2>
          <div class="anchors">/{d_href}</div>
          <a href="{d_href}" class="link">デザイン案を開く</a>
        </div>'''

    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>第二開発技工 リニューアル ワイヤーフレーム 一覧</title>
<link rel="stylesheet" href="css/wireframe.css?v=telbox">
<style>
  .index-hero {{ background:#f5f5f5; padding:64px 24px; border-bottom:1px solid #ccc; }}
  .index-hero h1 {{ font-size:32px; margin-bottom:8px; }}
  .index-hero p {{ color:#555; }}
  .index-hero .meta {{ font-size:12px; color:#999; margin-top:16px; font-family:monospace; }}
  .page-grid {{ display:grid; grid-template-columns:repeat(3,1fr); gap:24px; padding:48px 0; }}
  .page-card {{ border:1px solid #ccc; padding:24px; background:#fff; display:flex; flex-direction:column; gap:12px; }}
  .page-card .n {{ font-family:monospace; color:#999; font-size:12px; }}
  .page-card h2 {{ font-size:18px; }}
  .page-card p {{ font-size:13px; color:#555; flex-grow:1; }}
  .page-card .anchors {{ font-size:11px; color:#666; font-family:monospace; border-top:1px solid #eee; padding-top:8px; }}
  .page-card a.link {{ display:inline-block; margin-top:8px; padding:8px 16px; background:#222; color:#fff; text-align:center; font-size:13px; letter-spacing:0.05em; }}
  .page-card a.link:hover {{ background:#555; text-decoration:none; }}
</style>
</head>
<body>

<section class="index-hero">
  <div class="wrap">
    <h1>第二開発技工 リニューアル ワイヤーフレーム</h1>
    <p>コンパクトサイトマップに基づくグレースケール構成案。角丸なし・装飾なしのレイアウト骨格のみ。</p>
    <div class="meta">Grayscale wireframe / v0.2 / 2026-08-26 定例反映版</div>
  </div>
</section>

<div class="wrap">
  <h2 style="font-size:22px; margin-top:48px; padding-bottom:12px; border-bottom:2px solid #333;">
    新規提案（9/8 定例用）<span style="font-size:12px; color:#666; font-weight:400; margin-left:12px;">— 2026-08-26 定例の決定事項を反映</span>
  </h2>
  <p style="color:#555; margin-top:12px; font-size:13px;">キャッチコピー「<b>測る技術で未来に残す</b>」確定を受けた、ステートメント展開・ファーストビュー新案・公開スケジュール。</p>
</div>

<div class="wrap">
<div class="page-grid" style="grid-template-columns:1fr;">
  <div class="page-card" style="flex-direction:row; align-items:center; gap:32px;">
    <div style="flex-shrink:0; width:160px; padding:20px; background:#f5f5f5; border:1px solid #ccc; text-align:center;">
      <div style="color:#888; font-family:monospace; font-size:10px; letter-spacing:0.25em; margin-bottom:6px;">DESIGN</div>
      <div style="color:#222; font-size:15px; font-weight:700;">TOPデザイン案</div>
    </div>
    <div style="flex:1;">
      <h2>TOPページ デザイン案（ヒーロー：インフラ案ベース）</h2>
      <p>確定コピー「測る技術で未来に残す」＋インフラ3D FVを軸に、ブランドカラー・フォントを適用したTOPの本デザイン案。ステートメント／3事業／強み／創業者の想い・ロゴ由来／採用／ニュース／CTAの全セクション構成。写真はダミー（本番は実写差替）。</p>
      <div class="anchors">/design-top.html</div>
    </div>
    <a href="design-top.html" class="link" style="align-self:stretch; display:flex; align-items:center; padding:12px 24px;">開く</a>
  </div>
  <div class="page-card" style="flex-direction:row; align-items:center; gap:32px;">
    <div style="flex-shrink:0; width:160px; padding:20px; background:#f5f5f5; border:1px solid #ccc; text-align:center;">
      <div style="color:#888; font-family:monospace; font-size:10px; letter-spacing:0.25em; margin-bottom:6px;">STATEMENT</div>
      <div style="color:#222; font-size:15px; font-weight:700;">確定コピー展開</div>
    </div>
    <div style="flex:1;">
      <h2>ステートメント確定案「測る技術で未来に残す」（本文3案）</h2>
      <p>確定コピーの本文3案（案1: 創業ビジョン継承 ／ 案2: 生活者・インフラスケール ／ 案3: 歴史と技術）＋サブコピー5案＋創業者資料・ロゴ由来の原典整理＋サイト内展開マップ。</p>
      <div class="anchors">/statement-main.html</div>
    </div>
    <a href="statement-main.html" class="link" style="align-self:stretch; display:flex; align-items:center; padding:12px 24px;">開く</a>
  </div>
  <div class="page-card" style="flex-direction:row; align-items:center; gap:32px;">
    <div style="flex-shrink:0; width:160px; padding:20px; background:#f5f5f5; border:1px solid #ccc; text-align:center;">
      <div style="color:#888; font-family:monospace; font-size:10px; letter-spacing:0.25em; margin-bottom:6px;">HERO ／ 新C案</div>
      <div style="color:#222; font-size:15px; font-weight:700;">インフラ案</div>
    </div>
    <div style="flex:1;">
      <h2>ヒーロー：インフラ案（3D地形 × 高速道路・都市・川・橋）</h2>
      <p>「技術者個人・抽象表現→社会インフラのスケール感へ」の決定を反映。白塗りの3Dワイヤー地形（山並みのみブルー）に、高速道路・ビル群・川・トラス橋が「発生→描画→消滅→別の場所に再発生」をループする演出＋確定コピーのタイプライター。</p>
      <div class="anchors">/hero-infra.html + terrain-infra-embed.html</div>
    </div>
    <a href="hero-infra.html" class="link" style="align-self:stretch; display:flex; align-items:center; padding:12px 24px;">開く</a>
  </div>
  <div class="page-card" style="flex-direction:row; align-items:center; gap:32px;">
    <div style="flex-shrink:0; width:160px; padding:20px; background:#f5f5f5; border:1px solid #ccc; text-align:center;">
      <div style="color:#888; font-family:monospace; font-size:10px; letter-spacing:0.25em; margin-bottom:6px;">SCHEDULE</div>
      <div style="color:#222; font-size:15px; font-weight:700;">公開スケジュール</div>
    </div>
    <div style="flex:1;">
      <h2>公開スケジュール案（2026年11月末公開）</h2>
      <p>11月末公開に向けた全体ガント＋マイルストーン。撮影（緑が残る9〜10月）がクリティカルパス。遅延時の2段階公開オプション付き。</p>
      <div class="anchors">/schedule.html</div>
    </div>
    <a href="schedule.html" class="link" style="align-self:stretch; display:flex; align-items:center; padding:12px 24px;">開く</a>
  </div>
</div>
</div>

<div class="wrap">
  <h2 style="font-size:22px; margin-top:48px; padding-bottom:12px; border-bottom:2px solid #333;">
    デザイン案（全ページ）<span style="font-size:12px; color:#666; font-weight:400; margin-left:12px;">— TOP＋下層10ページ。ブランドカラー・フォント適用（写真・画像はダミー）</span>
  </h2>
  <p style="color:#555; margin-top:12px; font-size:13px;">ワイヤーフレームと同じ構成のまま、ブランドガイドライン（ロゴブルー＋Noto Sans JP／Inter）のデザインを適用した全ページ一式。</p>
</div>

<div class="wrap">
<div class="page-grid">{design_cards}
</div>
</div>

<div class="wrap">
  <h2 style="font-size:22px; margin-top:48px; padding-bottom:12px; border-bottom:2px solid #333;">
    ステートメント案（A〜G・アーカイブ）<span style="font-size:12px; color:#666; font-weight:400; margin-left:12px;">— 8/26 定例で「測る技術で未来に残す」に確定。検討経緯として保存</span>
  </h2>
  <p style="color:#555; margin-top:12px; font-size:13px;">7つの角度から起こしたタグライン＋ステートメント。クリックでスライドを表示。</p>
</div>
<div class="wrap">
<div class="st-grid">{st_cards}
</div>
</div>

<div class="wrap">
  <h2 style="font-size:22px; margin-top:32px; padding-bottom:12px; border-bottom:2px solid #333;">
    サイトマップ 各ページ<span style="font-size:12px; color:#666; font-weight:400; margin-left:12px;">— コンパクトサイトマップ 11ページ</span>
  </h2>
</div>

<div class="wrap">
<div class="page-grid">{page_cards}
</div>
</div>

<div class="wrap">
  <h2 style="font-size:22px; margin-top:32px; padding-bottom:12px; border-bottom:2px solid #333;">
    参考資料・試作<span style="font-size:12px; color:#666; font-weight:400; margin-left:12px;">— カラー／フォント／ロゴ規定＋ヒーロー試作</span>
  </h2>
</div>

<div class="wrap">
<div class="page-grid" style="grid-template-columns:1fr;">
  <div class="page-card" style="flex-direction:row; align-items:center; gap:32px;">
    <div style="flex-shrink:0; width:160px; padding:20px; background:#f5f5f5; border:1px solid #ccc; text-align:center;">
      <div style="color:#666; font-family:monospace; font-size:10px; letter-spacing:0.25em; margin-bottom:6px;">BRAND GUIDELINE</div>
      <div style="color:#222; font-size:16px; font-weight:700;">v0.1</div>
    </div>
    <div style="flex:1;">
      <h2>ブランドガイドライン</h2>
      <p>ロゴブルー（#015B9E）をメイン、淡いアクア／イエローを差し色にした配色ルール／Noto Sans JP＋Inter＋Noto Serif JPのフォント選定／ボタン・見出し等の適用例。</p>
      <div class="anchors">/guidelines.html + #logo #color #font #applications</div>
    </div>
    <a href="guidelines.html" class="link" style="align-self:stretch; display:flex; align-items:center; padding:12px 24px;">開く</a>
  </div>
  <div class="page-card" style="flex-direction:row; align-items:center; gap:32px;">
    <div style="flex-shrink:0; width:160px; padding:20px; background:#f5f5f5; border:1px solid #ccc; text-align:center;">
      <div style="color:#666; font-family:monospace; font-size:10px; letter-spacing:0.25em; margin-bottom:6px;">HERO ／ A案</div>
      <div style="color:#222; font-size:15px; font-weight:700;">テクノロジー案</div>
    </div>
    <div style="flex:1;">
      <h2>ヒーロー：テクノロジー案</h2>
      <p>Three.js 製の3Dワイヤーメッシュ地形が呼吸のようにうねり、0.3秒のグリット回転＋2秒ホールドを繰返し。ドラッグで自由に回転できる。左上に日本語⇔英語のループタイプライター。下部にブランドカラー／空パララックス／中央ロゴのスクロールセクション付き。</p>
      <div class="anchors">/hero-anim.html + terrain-embed.html</div>
    </div>
    <a href="hero-anim.html" class="link" style="align-self:stretch; display:flex; align-items:center; padding:12px 24px;">開く</a>
  </div>
  <div class="page-card" style="flex-direction:row; align-items:center; gap:32px;">
    <div style="flex-shrink:0; width:160px; padding:20px; background:#f5f5f5; border:1px solid #ccc; text-align:center;">
      <div style="color:#666; font-family:monospace; font-size:10px; letter-spacing:0.25em; margin-bottom:6px;">HERO ／ B案</div>
      <div style="color:#222; font-size:15px; font-weight:700;">技術者案</div>
    </div>
    <div style="flex:1;">
      <h2>ヒーロー：技術者案</h2>
      <p>「人」を主役にした案。現場スタッフの4写真がブルー背景から丸ワイプで切り替わる（20秒ループ／空・山岳・都市・建設現場）。左上に白色のタイプライター（日⇔英）。</p>
      <div class="anchors">/hero-engineer.html + eng1-4.jpg</div>
    </div>
    <a href="hero-engineer.html" class="link" style="align-self:stretch; display:flex; align-items:center; padding:12px 24px;">開く</a>
  </div>
</div>
</div>

<script src="css/wireframe.js" defer></script>
</body>
</html>'''

# ------------------------------------------------------------
# 出力
# ------------------------------------------------------------
files = [
    ('home.html', 'ホーム | /', HOME),
    ('service.html', '事業案内 | /service/', SERVICE),
    ('service-survey.html', '事業案内 ／ 測量 | /service/survey/', SERVICE_SURVEY),
    ('service-design.html', '事業案内 ／ 調査・設計 | /service/design/', SERVICE_DESIGN),
    ('service-management.html', '事業案内 ／ 施工管理 | /service/management/', SERVICE_MANAGEMENT),
    ('strengths.html', '強み・技術 | /strengths/', STRENGTHS),
    ('social.html', '社会活動 | /social/', SOCIAL),
    ('about.html', '会社案内 | /about/', ABOUT),
    ('recruit.html', '採用情報 | /recruit/', RECRUIT),
    ('news.html', 'ニュース | /news/', NEWS),
    ('contact.html', 'お問い合わせ | /contact/', CONTACT),
]

titles = {
    'home.html': 'ホーム',
    'service.html': '事業案内',
    'service-survey.html': '測量',
    'service-design.html': '調査・設計',
    'service-management.html': '施工管理',
    'strengths.html': '強み・技術',
    'social.html': '社会活動',
    'about.html': '会社案内',
    'recruit.html': '採用情報',
    'news.html': 'ニュース',
    'contact.html': 'お問い合わせ',
}

for filename, banner, content in files:
    title = titles[filename]
    html = page(title, banner, content)
    with open(os.path.join(BASE, filename), 'w') as f:
        f.write(html)
    print(f'✓ {filename}')

# ステートメント
for i, s in enumerate(STATEMENTS):
    html = build_statement(i, s)
    with open(os.path.join(BASE, f'statement-{s["id"]}.html'), 'w') as f:
        f.write(html)
    print(f'✓ statement-{s["id"]}.html')

# インデックス
with open(os.path.join(BASE, 'index.html'), 'w') as f:
    f.write(build_index())
print('✓ index.html')

print(f'\n完了: {BASE}')

# ------------------------------------------------------------
# デザイン版出力（design-*.html）
# ------------------------------------------------------------
import re

DESIGN_MAP = {fn: ('design-top.html' if fn == 'home.html' else 'design-' + fn) for fn, _, _ in files}

def to_design_links(html):
    def rep(m):
        tail = m.group(2) or ''
        return f'href="{DESIGN_MAP.get(m.group(1), m.group(1))}{tail}"'
    return re.sub(r'href="([a-z0-9-]+\.html)(#[A-Za-z0-9_-]+)?"', rep, html)

def design_header():
    lis = ''.join(f'<li><a href="{DESIGN_MAP.get(h, h)}">{l}</a></li>' for h, l in NAV)
    return f'''<header class="site-header">
  <div class="wrap">
    <a href="design-top.html" class="site-logo"><img src="img/logo.png" alt="株式会社第二開発技工"></a>
    <div class="header-right">
      <nav class="gnav"><ul>{lis}</ul></nav>
      <a href="tel:0864231899" class="tel-box">
        <div class="tel-label">お電話でのお問い合わせ</div>
        <div class="tel-num">086-423-1899</div>
        <div class="tel-hours">平日 9:00〜17:00</div>
      </a>
    </div>
  </div>
</header>'''

def design_page(title, banner, body):
    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}（デザイン案） | 株式会社第二開発技工</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&family=Inter:wght@400;500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/design.css?v=1">
</head>
<body>

<div class="wf-banner"><span>DESIGN | {banner}（写真はダミー・本番は実写差替）</span><a href="index.html">← 一覧に戻る</a></div>

{design_header()}

{to_design_links(body)}

{to_design_links(footer())}
</body>
</html>'''

for filename, banner, content in files:
    if filename == 'home.html':
        continue
    out = 'design-' + filename
    with open(os.path.join(BASE, out), 'w') as f:
        f.write(design_page(titles[filename], banner, content))
    print(f'✓ {out}')
