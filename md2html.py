import codecs, markdown
from markdown.extensions.tables import TableExtension

# 读取 markdown 文本
input_file = codecs.open("mscoco-fsod.md", mode="r", encoding="utf-8")
text = input_file.read()

# 转为 html 文本
html = markdown.markdown(text, extensions=['nl2br', 'markdown.extensions.toc','markdown.extensions.fenced_code', 'markdown.extensions.tables'])

print(html)
# 保存为文件
output_file = codecs.open("./mscoco-fsod.html", mode="w", encoding="utf-8")

output_file.write(html)
