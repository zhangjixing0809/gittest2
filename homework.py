class Record(object):
    record_list = []

    def add_record(self):
        name = input('请输入用户名：')
        tel = input('请输入手机号：')
        d = {
            '姓名': name,
            'tel': tel
        }
        print(d)
        self.record_list.append(d.copy())
        print('保存成功')
        # print(self.record_list)

    def query_record(self):
        name = input('请输入要查询的用户名：')

        for i in self.record_list:
            if name in i.get('姓名'):
                print(i)
                break
        else:
            print('没有找到该联系人')

    def delete_recode(self):
        name = input('请输入你要删除的用户名：')
        for i in self.record_list:
            if name in i.get('姓名'):
                index = self.record_list.index(i)
                self.record_list.pop(index)
                print('用户删除成功')
                break
        else:
            print('用户不存在')

    def change_record(self):
        name = input('请输入要修改的用户名：')
        for i in self.record_list:
            if name in i['姓名']:
                tel = input('请输入修改后的手机号;')
                i['tel'] = tel
                print(i)
                print('修改成功')
                break

        else:
            print('该用户不存在')

    def main(self):
        while True:
            print('------------通讯录菜单----------')
            print('请按提示操作')
            print('1.添加联系人')
            print('2.查询联系人')
            print('3.修改联系人')
            print('4.删除联系人')
            print('5.按q退出')
            zhiling = input('请输入指令：')
            if zhiling == '1':
                self.add_record()
            elif zhiling == '2':
                self.query_record()
            elif zhiling == '3':
                self.change_record()
            elif zhiling == '4':
                self.delete_recode()
            elif zhiling == 'q':
                break
            else:
                print('指令有误，重新输入')


if __name__ == '__main__':
    # zz = []
    r = Record()
    # r.add_record()
    # print(r.record_list)
    # print(zz)
    # r.query_record()
    # r.change_record()
    # r.delete_recode()
    r.main()


