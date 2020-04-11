import os


# 作业一：装饰器函数
def permit(func):
    def inner():
        n = input('请输入用户名：')
        p = input('请输入密码：')
        if n == 'root' and p == '123456':
            print('你有权限')
            print(func())

        else:
            print('没有权限')

    return inner


@permit
def test():
    return '1, 2, 3'


# test()

# 作业二：迭代器


# 练习找出所有文件
# 不会写...
path = r'D:\PyCharm 2019.3'
for i in os.listdir(path):
    size_path = os.path.join(path, i)
    # print(size_path)
    if os.path.isfile(size_path):
        print(size_path, os.path.getsize(size_path))
#

# for i in os.walk(r'D:\python'):
#     size = os.path.getsize(i[0])
#     if size > 0:
#         print(size)





