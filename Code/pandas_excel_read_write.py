import pandas as pd

# 读取Excel文件
info_excel_read = pd.read_excel('窄门.xlsx')

# 删除空值（NaN）
info_excel_read.dropna(axis=0, how='all', inplace=True)
info_excel_read.dropna(axis=1, how='all', inplace=True)

# 删除空白行后重新编辑索引
info_excel_read.reset_index(drop=True, inplace=True)

# 修改列的名称
info_excel_read.columns = ['高亮标记']

## 用来删除特定的列
# info_excel_read.drop(index = 0,axis=1, inplace=True)

# 保存成新Excel表，避免覆盖原文件
info_excel_read.to_excel('窄门_modified.xlsx', index=True)

# 保存成markdown文件
info_excel_read.to_markdown('窄门.md', index=False)