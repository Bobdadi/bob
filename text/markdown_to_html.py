import markdown
from pathlib import Path

def convert_markdown_to_html(markdown_file, output_file):
    # 读取 Markdown 文件
    markdown_text = Path(markdown_file).read_text(encoding='utf-8')
    
    # 转换 Markdown 为 HTML
    html_content = markdown.markdown(markdown_text)
    
    # 生成完整的 HTML 页面
    full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Markdown Preview</title>
    <style>
        body {{ max-width: 800px; margin: 20px auto; padding: 0 20px; }}
        pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; }}
        code {{ background: #f4f4f4; padding: 2px 5px; border-radius: 3px; }}
        blockquote {{ border-left: 4px solid #ddd; padding-left: 15px; color: #666; }}
    </style>
</head>
<body>
{html_content}
</body>
</html>"""
    
    # 写入 HTML 文件
    Path(output_file).write_text(full_html, encoding='utf-8')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python markdown_to_html.py <input.md> <output.html>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_markdown_to_html(input_file, output_file)
    print(f"Successfully converted {input_file} to {output_file}")
