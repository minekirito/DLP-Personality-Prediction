from pip._vendor import chardet

# 文件编码格式检测

f = open ('kaggle.xlsx', 'rb')
print ( chardet.detect ( f.read ( 100 ) ) )
