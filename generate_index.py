import os, time, re

def get_text(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        c = re.sub(r'<(style|script)[^>]*>.*?</\1>', '', c, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', '', c)
        return " ".join(text.split())[:120] + "..."
    except:
        return ""

def build():
    posts_dir = 'posts'
    if not os.path.exists(posts_dir): os.makedirs(posts_dir)
    
    files = [f for f in os.listdir(posts_dir) if f.endswith('.html')]
    files.sort(key=lambda x: os.path.getmtime(os.path.join(posts_dir, x)), reverse=True)

    rows = ""
    for f in files:
        f_p = os.path.join(posts_dir, f)
        dt = time.strftime('%Y-%m-%d', time.localtime(os.path.getmtime(f_p)))
        pv = get_text(f_p)
        rows += f'''
        <a href="{posts_dir}/{f}" class="article-row">
            <div class="cell">{f}</div>
            <div class="cell">{dt}</div>
            <div class="cell preview">{pv}</div>
        </a>'''

    with open('template.html', 'r', encoding='utf-8') as t:
        html = t.read().replace('', rows)
    
    with open('index.html', 'w', encoding='utf-8') as i:
        i.write(html)

if __name__ == "__main__":
    build()
