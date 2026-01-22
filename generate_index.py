import os, time, re

def get_clean_preview(p):
    try:
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        c = re.sub(r'<(style|script)[^>]*>.*?</\1>', '', c, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', '', c)
        return " ".join(text.split())[:110] + "..."
    except:
        return ""

def build_site():
    posts_dir = 'posts'
    if not os.path.exists(posts_dir): os.makedirs(posts_dir)
    files = [f for f in os.listdir(posts_dir) if f.endswith('.html')]
    files.sort(key=lambda x: os.path.getmtime(os.path.join(posts_dir, x)), reverse=True)

    rows = ""
    for f in files:
        f_path = os.path.join(posts_dir, f)
        m_time = time.strftime('%Y-%m-%d', time.localtime(os.path.getmtime(f_path)))
        preview = get_clean_preview(f_path)
        rows += f'''<a href="{posts_dir}/{f}" class="row"><div class="c"><span>{f}</span></div><div class="c">{m_time}</div><div class="c p">{preview}</div></a>'''

    html_content = f'''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title> Macintosh HD</title>
    <style>
        body {{ background:#008080; margin:0; font-family:"Geneva",sans-serif; display:flex; justify-content:center; align-items:center; height:100vh; }}
        .win {{ width:92%; max-width:880px; height:82vh; background:#E0E0E0; border:2px solid #000; display:flex; flex-direction:column; box-shadow:4px 4px 0 #000; }}
        .bar {{ height:22px; background:repeating-linear-gradient(0deg,#000,#000 1px,transparent 1px,transparent 3px); background-color:#E0E0E0; border-bottom:2px solid #000; display:flex; justify-content:center; align-items:center; }}
        .bar-t {{ background:#E0E0E0; padding:0 10px; font-weight:bold; font-size:12px; }}
        .main {{ flex:1; background:#FFF; margin:2px; border:2px solid #000; overflow-y:scroll; }}
        .main::-webkit-scrollbar {{ width:22px; background:#D2D2D2; border-left:2px solid #000; }}
        .main::-webkit-scrollbar-thumb {{ background:#E0E0E0; border:2px solid #000; box-shadow:inset 1px 1px 0 #fff; }}
        .hd {{ position:sticky; top:0; display:grid; grid-template-columns:180px 110px 1fr; background:#E0E0E0; border-bottom:1px solid #000; font-size:11px; z-index:9; }}
        .row {{ display:grid; grid-template-columns:180px 110px 1fr; text-decoration:none; color:#000; border-bottom:1px solid #EEE; font-size:13px; }}
        .row:hover {{ background:#000080; color:#FFF; }}
        .c {{ padding:8px 10px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; border-right:1px solid #EEE; }}
        .p {{ font-size:11px; color:#666; }}
        .row:hover .p {{ color:#CCC; }}
    </style>
</head>
<body>
    <div class="win">
        <div class="bar"><div class="bar-t"> Macintosh HD</div></div>
        <div class="main">
            <div class="hd"><div class="c">Name</div><div class="c">Date</div><div class="c">Preview</div></div>
            {rows}
        </div>
    </div>
</body>
</html>'''
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == "__main__":
    build_site()
