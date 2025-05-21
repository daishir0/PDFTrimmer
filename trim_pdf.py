import sys
import os
from PyPDF2 import PdfReader, PdfWriter

def trim_pdf(input_path, page_range, output_path=None):
    """
    PDFファイルを指定したページ範囲でトリミングします。
    
    Args:
        input_path (str): 入力PDFファイルのパス
        page_range (str): ページ範囲（例: "3-5"）
        output_path (str, optional): 出力PDFファイルのパス。指定しない場合は自動生成
    """
    try:
        # ページ範囲を解析
        start_page, end_page = map(int, page_range.split('-'))
        start_page -= 1  # 0ベースのインデックスに変換
        
        # PDFリーダーを作成
        reader = PdfReader(input_path)
        
        # ページ範囲が有効かチェック
        if start_page < 0 or end_page > len(reader.pages):
            raise ValueError(f"無効なページ範囲です。PDFのページ数は {len(reader.pages)} です。")
        
        # PDFライターを作成
        writer = PdfWriter()
        
        # 指定されたページを追加
        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])
        
        # 出力ファイル名を生成
        if output_path is None:
            base_name = os.path.splitext(input_path)[0]
            output_path = f"{base_name}_{page_range}.pdf"
        
        # PDFを保存
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        
        print(f"PDFをトリミングしました: {output_path}")
        
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("使用方法: python trim_pdf.py <入力PDFファイル> <ページ範囲> [出力PDFファイル]")
        print("例: python trim_pdf.py target.pdf 3-5")
        sys.exit(1)
    
    input_path = sys.argv[1]
    page_range = sys.argv[2]
    output_path = sys.argv[3] if len(sys.argv) > 3 else None
    
    trim_pdf(input_path, page_range, output_path) 