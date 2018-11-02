from whoosh.qparser import QueryParser
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.query import *

#创建Schema
scheam = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
#创建索引
ix = create_in('index', schema=scheam)  #index 是文件夹
#开始搜索
with ix.searcher() as searcher:
    #构建查询分析器
    #first 是搜索的关键字
    #content搜索类型
    query = QueryParser('content', ix.schema).parse('f')
    #查询 返回whoosh.searching.Results
    searResult = searcher.search(query)

    findResult = searcher.find('content', 'first')
    print(searResult)