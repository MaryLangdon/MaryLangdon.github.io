import os
import time
import re

def get_clean_preview(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # 移除 <style> 和 <script> 及其内容，避免预览里出现代码
        content = re.sub(r'<(style|script)[^>]*>.*?</\1>', '', content, flags=re.DOTALL)
        # 移除所有 HTML 标签
        text = re.sub(r'<[^>]+>', '', content)
        # 将多个空格/换行符压缩为一个
        text = " ".join(text.split())
        return text[:120] + "..."
    except:
        return "No content preview."

def generate():
    posts_dir = 'posts'
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)
    
    # 扫描 posts 文件夹下的 html
    files = [f for f in os.listdir(posts_dir) if f.endswith('.html')]
    # 按最后修改时间排序
    files.sort(key=lambda x: os.path.getmtime(os.path.join(posts_dir, x)), reverse=True)

    rows_html = ""
    for file in files:
        path = os.path.join(posts_dir, file)
        mod_time = time.strftime('%Y-%m-%d', time.localtime(os.path.getmtime(path)))
        preview = get_clean_preview(path)
        
        # 生成 Apple 列表行
        rows_html += f'''
        <a href="{posts_dir}/{file}" class="article-row">
            <div class="cell name">{file}</div>
            <div class="cell date">{mod_time}</div>
            <div class="cell preview-text">{preview}</div>
        </a>'''

    # 【关键修复】：永远只读取独立的模板文件
    if not os.path.exists('template.html'):
        print("Error: template.html not found!")
        return

    with open('template.html', 'r', encoding='utf-8') as f:
        template_content = f.read()

    # 替换占位符
    final_html = template_content.replace('', rows_html)

    # 写入最终的 index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print(f"Success: {len(files)} posts indexed.")

if __name__ == "__main__":
    generate()
