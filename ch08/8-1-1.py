from bs4 import BeautifulSoup
html_doc = """
<div class="container">
    <h1 id="title">課程清單</h1>
    <ul class="course-list">
        <li>Python 基礎</li>
        <li>網路爬蟲實戰</li>
        <li>資料分析入門</li>
    </ul>
</div>
"""