import os
import time
import re

def get_clean_preview(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # 移除样式、脚本、标签，只留纯文本
        content = re.sub(r'<(style|script)[^>]*>.*?</\1>', '', content, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', '', content)
        text = " ".join(text.split())
        return text[:100] + "..."
    except:
        return "No content preview available."

def generate():
    posts_dir = 'posts'
    # 确保文件夹存在
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)
    
    # 只识别 html 文件
    files = [f for f in os.listdir(posts_dir) if f.endswith('.html')]
    # 按最后修改时间排序
    files.sort(key=lambda x: os.path.getmtime(os.path.join(posts_dir, x)), reverse=True)

    rows_html = ""
    for file in files:
        path = os.path.join(posts_dir, file)
        mod_time = time.strftime('%Y-%m-%d', time.localtime(os.path.getmtime(path)))
        preview = get_clean_preview(path)
        
        # 严格按照 Finder 列表格式生成行
        rows_html += f'''
        <a href="{posts_dir}/{file}" class="article-row">
            <div class="cell name">{file}</div>
            <div class="cell date">{mod_time}</div>
            <div class="cell preview-text">{preview}</div>
        </a>'''

    # 读取模板
    with open('template.html', 'r', encoding='utf-8') as f:
        template = f.read()

    # 替换占位符并写回 index.html
    # 确保只替换一次，防止出现循环嵌套
    final_html = template.replace('', rows_html)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

if __name__ == "__main__":
    generate()
