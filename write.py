from whoosh.index import create_in
from whoosh.fields import *

#创建Schema
scheam = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
ix = create_in('index', schema=scheam)  #index 是文件夹
#创建写入对象
writer = ix.writer()
#写入内容
writer.add_document(title="FirstDocument", path='/a', content="this is the first document we've add!")
writer.add_document(title="SecondDocument", path='/b', content="this is the second document we've add!")
#提交
#会在index目录下生成三个文件
writer.commit()