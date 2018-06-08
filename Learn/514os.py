import os

# 获取当前路径
print(os.getcwd())
# 输出D:\Scrapy\tutorial\tutorial

# 用来将包含 ~ 符号（表示当前用户Home 目录）的路径扩展为完整的路径。
print(os.path.expanduser('~'))
# 输出C:\Users\Administrator


# os.path.join() 可以接受任何数量的参数。
# 无论你使用哪种形式的斜杠，Python 都可以访问到文件。
# os.path.join()  函数从一个或多个路径片段中构造一个路径名。
print(os.path.join(os.path.expanduser('~'),'diveintopython3','examples','humansize.py'))
# 输出C:\Users\Administrator\diveintopython3\examples\humansize.py

# split  函数分割一个完整路径并返回目录和文件名
pathname = '/Users/pilgrim/diveintopython3/examples/humansize.py'
print(os.path.split(pathname))
# 输出('/Users/pilgrim/diveintopython3/examples', 'humansize.py')
dirname,filename=os.path.split(pathname)
print (dirname,filename)
# 输出('/Users/pilgrim/diveintopython3/examples', 'humansize.py')

# glob  模块
# 获得一个目录的内容
import os
os.chdir('/Users/pilgrim/diveintopython3/')
import glob
glob.glob('examples/*.xml')
