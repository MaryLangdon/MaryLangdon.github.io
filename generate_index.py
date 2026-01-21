import os
import time
import re

def get_clean_preview(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # 移除脚本和样式块
        content = re.sub(r'<(style|script)[^>]*>.*?</\1>', '', content, flags=re.DOTALL)
        # 移除HTML标签
        text = re.sub(r'<[^>]+>', '', content)
        return " ".join(text.split())[:100] + "..."
    except:
        return ""

def generate():
    posts_dir = 'posts'
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)
    
    # 获取所有html文件并按时间排序
    files = [f for f in os.listdir(posts_dir) if f.endswith('.html')]
    files.sort(key=lambda x: os.path.getmtime(os.path.join(posts_dir, x)), reverse=True)

    rows_html = ""
    for file in files:
        path = os.path.join(posts_dir, file)
        mod_time = time.strftime('%Y-%m-%d', time.localtime(os.path.getmtime(path)))
        preview = get_clean_preview(path)
        
        # 这里的 rows_html 只是纯数据填充
        rows_html += f'''
        <a href="{posts_dir}/{file}" class="article-row">
            <div class="cell name">{file}</div>
            <div class="cell date">{mod_time}</div>
            <div class="cell preview-text">{preview}</div>
        </a>'''

    # 读取母版
    with open('template.html', 'r', encoding='utf-8') as f:
        template = f.read()

    # 替换并生成 index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(template.replace('', rows_html))

if __name__ == "__main__":
    generate()
