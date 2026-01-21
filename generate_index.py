<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>Macintosh HD - Finder</title>
    <style>
        :root {
            --mac-grey: #E0E0E0;
            --mac-blue: #000080;
            --mac-scroll-bg: #D2D2D2;
        }

        body {
            background-color: #008080; /* 经典桌面绿 */
            margin: 0;
            font-family: "Geneva", "Chicago", sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }

        /* 窗口容器 */
        .finder-window {
            width: 90%;
            max-width: 960px;
            height: 80vh;
            background: var(--mac-grey);
            border: 2px solid #000;
            box-shadow: 6px 6px 0px rgba(0,0,0,0.3);
            display: flex;
            flex-direction: column;
        }

        /* 早期 Mac 的横纹标题栏 */
        .title-bar {
            height: 22px;
            background: repeating-linear-gradient(0deg, #000, #000 1px, transparent 1px, transparent 3px);
            background-color: var(--mac-grey);
            border-bottom: 2px solid #000;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }
        .title-text {
            background: var(--mac-grey);
            padding: 0 15px;
            font-weight: bold;
            font-size: 13px;
        }

        /* 详细列表显示区 */
        .list-container {
            flex: 1;
            overflow-y: scroll;
            background: white;
            margin: 2px;
            border: 2px solid #000;
        }

        /* 还原 Apple 系统滚动条 */
        .list-container::-webkit-scrollbar {
            width: 20px;
            background-color: var(--mac-scroll-bg);
            border-left: 1px solid #000;
        }
        .list-container::-webkit-scrollbar-thumb {
            background: var(--mac-grey);
            border: 2px solid #000;
            box-shadow: inset 1px 1px 0 #fff;
        }

        /* 列表表头 */
        .list-header {
            position: sticky; top: 0;
            display: grid;
            grid-template-columns: 200px 120px 1fr;
            background: var(--mac-grey);
            border-bottom: 1px solid #000;
            font-size: 11px;
            z-index: 10;
        }
        .header-item { padding: 4px 10px; border-right: 1px solid #999; font-weight: bold; }

        /* 文章行样式 */
        .article-row {
            display: grid;
            grid-template-columns: 200px 120px 1fr;
            text-decoration: none;
            color: black;
            font-size: 13px;
            border-bottom: 1px solid #eee;
        }
        .article-row:hover {
            background-color: var(--mac-blue);
            color: white;
        }

        .cell {
            padding: 10px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .preview-text {
            font-size: 11px;
            color: #666;
        }
        .article-row:hover .preview-text { color: #ccc; }

        /* 底部状态栏 */
        .status-bar {
            height: 20px;
            background: var(--mac-grey);
            border-top: 1px solid #000;
            padding: 0 10px;
            font-size: 11px;
            line-height: 20px;
        }
    </style>
</head>
<body>

<div class="finder-window">
    <div class="title-bar">
        <div class="title-text"> Macintosh HD : Blog</div>
    </div>
    
    <div class="list-container">
        <div class="list-header">
            <div class="header-item">Name</div>
            <div class="header-item">Date Modified</div>
            <div class="header-item">Preview Content</div>
        </div>
        </div>

    <div class="status-bar" id="item-info">0 items</div>
</div>

<script>
    const count = document.querySelectorAll('.article-row').length;
    document.getElementById('item-info').innerText = count + " items in folder";
</script>

</body>
</html>
