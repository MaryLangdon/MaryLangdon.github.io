import os
import time
from html.parser import HTMLParser

class TextStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []
    def handle_data(self, d): self.fed.append(d)
    def get_data(self): return "".join(self.fed)

def get_html_preview(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        stripper = TextStripper()
        stripper.feed(content)
        return stripper.get_data().strip()[:100].replace('\n', ' ')
    except:
        return ""

def generate_index():
    posts_dir = 'posts'
    if not os.path.exists(posts_dir): os.makedirs(posts_dir)
    
    files = [f for f in os.listdir(posts_dir) if f.endswith('.html')]
    # 按时间排序
    files.sort(key=lambda x: os.path.getmtime(os.path.join(posts_dir, x)), reverse=True)

    rows_html = ""
    for file in files:
        path = os.path.join(posts_dir, file)
        file_name = file # 直接显示文件名
        mod_time = time.strftime('%Y-%m-%d', time.localtime(os.path.getmtime(path)))
        preview = get_html_preview(path)
        
        rows_html += f'''
        <a href="{posts_dir}/{file}" class="article-row">
            <div class="cell name">{file_name}</div>
            <div class="cell date">{mod_time}</div>
            <div class="cell preview-text">{preview}</div>
        </a>'''

    with open('template.html', 'r', encoding='utf-8') as f:
        template = f.read()

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(template.replace('', rows_html))

if __name__ == "__main__":
    generate_index()
