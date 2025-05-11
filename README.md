# Image to PDF Converter (mkpdf)

様々な形式の画像を高品質なPDFに変換するPythonライブラリです。バッチ変換やメタデータ付与、コマンドライン操作、設定ファイルによるカスタマイズなど、実用的な機能を多数搭載しています。

---

## 特徴
- **多様な画像形式対応**: JPG, PNG, GIF, BMP, TIFF など主要フォーマットをサポート
- **単一・複数画像のPDF変換**: 1枚から大量画像まで一括変換
- **画像の回転・リサイズ・配置**: ページごとに細かく指定可能
- **PDFメタデータ設定**: タイトル・作成者・キーワード等を自由に付与
- **CLI/GUI不要の自動化**: コマンドラインやPythonスクリプトから簡単操作
- **進捗バー・詳細ログ**: バッチ処理時も進捗やエラーを見やすく表示
- **設定ファイルでデフォルト値管理**: よく使う設定を保存し再利用
- **カスタム例外で堅牢なエラーハンドリング**

---

## インストール

```bash
pip install mkpdf
```

---

## クイックスタート

### 単一画像をPDFに変換（Python API）
```python
from mkpdf import ImageToPDF
converter = ImageToPDF()
converter.convert_single_image(
    image_path="sample.jpg",
    output_path="output.pdf"
)
```

### 複数画像を1つのPDFにまとめる（Python API）
```python
from mkpdf import ImageToPDF
converter = ImageToPDF()
image_list = ["img1.png", "img2.jpg", "img3.bmp"]
converter.convert_multiple_images(
    image_paths=image_list,
    output_path="merged.pdf"
)
```

### コマンドラインで一括変換
```bash
mkpdf multiple "images/*.jpg" merged.pdf --page-size A4 --resize --quality 90
```

---

## Python API 詳細例

### メタデータ・ページサイズ・配置・回転・品質指定
```python
from mkpdf import ImageToPDF, PageSize, ImagePosition, PDFMetadata
converter = ImageToPDF()
metadata = PDFMetadata(
    title="旅行アルバム",
    author="山田太郎",
    subject="2024年春の旅行",
    keywords="旅行,アルバム,PDF"
)
converter.metadata = metadata
converter.convert_single_image(
    image_path="photo.png",
    output_path="album.pdf",
    page_size=PageSize.A4_LANDSCAPE,
    rotate=90,
    resize=True,
    position=ImagePosition.BOTTOM_RIGHT,
    quality=85
)
```

### エラー処理・ロギング・進捗バー連携
```python
from mkpdf import ImageToPDF, PDFError
from mkpdf.logger import setup_logger
import logging
logger = setup_logger(level=logging.INFO)
converter = ImageToPDF()
try:
    converter.convert_single_image("notfound.jpg", "out.pdf")
except PDFError as e:
    logger.error(f"PDF変換エラー: {e}")
```

---

## コマンドライン詳細例

### 画像のワイルドカード指定
```bash
mkpdf multiple "images/*.png" output.pdf --resize --quality 90
```

### ディレクトリ内の全画像を変換
```bash
mkpdf multiple "mydir/*.jpg" all.pdf --page-size LETTER
```

### メタデータ・配置・回転・品質を指定
```bash
mkpdf single input.jpg out.pdf --title "作品集" --author "作者名" --position bottom_left --rotate 270 --quality 80
```

### 設定ファイルを使ったデフォルト値の利用
```bash
mkpdf config set --page-size A4 --quality 95 --position center
mkpdf single img.png out.pdf  # 上記設定が自動適用される
```

---

## 設定ファイルのカスタマイズ例

`~/.mkpdf/config.json` を直接編集して、デフォルト値を細かく調整できます。

```json
{
  "default_page_size": "A4_LANDSCAPE",
  "default_quality": 90,
  "default_position": "bottom_right",
  "default_resize": true,
  "default_rotate": 90,
  "default_metadata": {
    "title": "アルバム",
    "author": "自分の名前",
    "subject": "思い出",
    "keywords": "写真,PDF,アルバム",
    "creator": "mkpdf"
  }
}
```

---

## 画像フォーマットごとの注意点
- **PNG/GIFの透過**: 透過部分は白で塗りつぶされます
- **CMYK画像**: 自動的にRGBに変換されます
- **TIFF**: マルチページTIFFは1ページ目のみ変換されます
- **大きな画像**: メモリ消費に注意してください

---

## テスト・CI/CDへの組み込み例

### pytestによる自動テスト
```bash
pip install -r requirements-dev.txt
pytest
```

### GitHub Actions例
```yaml
name: mkpdf CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install -r requirements-dev.txt
      - name: Run tests
        run: pytest
```

---

## FAQ

### Q. サポートされている画像形式は？
A. JPG, JPEG, PNG, GIF, BMP, TIFF です。

### Q. 画像が大きすぎてエラーになります
A. `resize=True` を指定するか、画像を事前に縮小してください。

### Q. 透過PNGはどうなりますか？
A. 透過部分は白で塗りつぶされます。

### Q. 画像の順番は？
A. `image_paths`リストやワイルドカードの並び順でPDFに追加されます。

### Q. CLIでエラーが出た場合の対処は？
A. `--debug`オプションで詳細ログを出力できます。

---

## 依存パッケージ
- Pillow>=10.2.0
- reportlab>=4.1.0
- click>=8.0.0
- tqdm>=4.65.0

---

## ライセンス
MIT License 