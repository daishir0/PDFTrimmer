# PDFTrimmer

## Overview
PDFTrimmer is a simple command-line utility that allows you to extract specific page ranges from PDF files. It enables you to create a new PDF containing only the pages you need, without altering the original file.

## Installation
To install PDFTrimmer, follow these steps:

```bash
# Clone the repository
git clone https://github.com/daishir0/PDFTrimmer

# Navigate to the project directory
cd PDFTrimmer

# Install required dependencies
pip install -r requirements.txt
```

## Usage
You can use PDFTrimmer by running the Python script with the following arguments:

```bash
python trim_pdf.py <input_pdf_file> <page_range> [output_pdf_file]
```

### Parameters:
- `input_pdf_file`: Path to the PDF file you want to trim
- `page_range`: Page range in the format "start-end" (e.g., "3-5")
- `output_pdf_file` (optional): Path for the output PDF file. If not specified, the output will be saved as `[original_filename]_[page_range].pdf`

### Examples:
```bash
# Extract pages 3 to 5 from document.pdf
python trim_pdf.py document.pdf 3-5

# Extract pages 10 to 15 and save to specified file
python trim_pdf.py document.pdf 10-15 extracted_pages.pdf
```

## Notes
- Page numbers are 1-indexed (the first page is page 1)
- Both the start and end pages are included in the extracted PDF
- The original PDF file is not modified
- Make sure the page range is valid for the input PDF

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

# PDFTrimmer

## 概要
PDFTrimmerは、PDFファイルから特定のページ範囲を抽出するためのシンプルなコマンドラインユーティリティです。元のファイルを変更せずに、必要なページのみを含む新しいPDFを作成することができます。

## インストール方法
PDFTrimmerをインストールするには、以下の手順に従ってください：

```bash
# リポジトリをクローン
git clone https://github.com/daishir0/PDFTrimmer

# プロジェクトディレクトリに移動
cd PDFTrimmer

# 必要な依存関係をインストール
pip install -r requirements.txt
```

## 使い方
PDFTrimmerは、以下の引数でPythonスクリプトを実行することで使用できます：

```bash
python trim_pdf.py <入力PDFファイル> <ページ範囲> [出力PDFファイル]
```

### パラメータ：
- `入力PDFファイル`：トリミングしたいPDFファイルのパス
- `ページ範囲`："開始-終了"の形式でのページ範囲（例："3-5"）
- `出力PDFファイル`（オプション）：出力PDFファイルのパス。指定しない場合、`[元のファイル名]_[ページ範囲].pdf`として保存されます

### 例：
```bash
# document.pdfから3〜5ページを抽出
python trim_pdf.py document.pdf 3-5

# document.pdfから10〜15ページを抽出し、指定したファイルに保存
python trim_pdf.py document.pdf 10-15 extracted_pages.pdf
```

## 注意点
- ページ番号は1から始まります（最初のページはページ1）
- 開始ページと終了ページの両方が抽出されたPDFに含まれます
- 元のPDFファイルは変更されません
- 入力PDFに対して有効なページ範囲であることを確認してください

## ライセンス
このプロジェクトはMITライセンスの下でライセンスされています。詳細はLICENSEファイルを参照してください。
