import re

def markdown_to_text(markdown):
    # 去除标题标记
    markdown = re.sub(r'#+\s*', '', markdown)
    # 去除粗体标记
    markdown = re.sub(r'\*\*(.*?)\*\*', r'\1', markdown)
    # 去除斜体标记
    markdown = re.sub(r'\*(.*?)\*', r'\1', markdown)
    # 处理代码块标记
    markdown = re.sub(r'```.*?\n(.*?)```', r'\1', markdown, flags=re.DOTALL)
    # 处理行内代码标记
    markdown = re.sub(r'`(.*?)`', r'\1', markdown)
    # 处理链接和图片标记
    markdown = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', markdown)
    # 处理列表标记，保留换行
    markdown = re.sub(r'^\s*[\*\-+]\s+', '* ', markdown, flags=re.MULTILINE)
    # 去除引用标记
    markdown = re.sub(r'^>\s*', '', markdown, flags=re.MULTILINE)
    # 去除多余的空行
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    return markdown.strip()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python markdown_to_text.py <markdown_file>")
        sys.exit(1)
    
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    plain_text = markdown_to_text(markdown_content)
    print(plain_text)
