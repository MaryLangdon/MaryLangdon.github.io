import os
import time
import re

def get_preview(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        text = re.sub(r'<(style|script)[^>]*>.*?</\1>', '', content, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', '', text)
        return " ".join(text.split())[:100] + "..."
    except:
        return ""

def main():
    posts_dir = 'posts'
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)
    
    files = [f for f in os.listdir(posts_dir) if f.endswith('.html')]
    files.sort(key=lambda x: os.path.getmtime(os.path.join(posts_dir, x)), reverse=True)

    rows = ""
    for f in files:
        full_path = os.path.join(posts_dir, f)
        m_time = time.strftime('%Y-%m-%d', time.localtime(os.path.getmtime(full_path)))
        preview = get_preview(full_path)
        rows += f'''
        <a href="{posts_dir}/{f}" class="article-row">
            <div class="cell name">{f}</div>
            <div class="cell date">{m_time}</div>
            <div class="cell preview-text">{preview}</div>
        </a>'''

    with open('template.html', 'r', encoding='utf-8') as t:
        tpl = t.read()
    
    with open('index.html', 'w', encoding='utf-8') as i:
        i.write(tpl.replace('', rows))

if __name__ == "__main__":
    main()
