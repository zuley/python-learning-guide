import json
def main():
    with open('./data/1.json', 'r+', encoding='utf-8') as fs:
        # load 读取并格式化数据为字典，loads，只格式化数据
        data = json.load(fs)
        data['name'] = '猪猪侠'
        # dump 将字典转换为字符串并写入文件，dumps 将字典数据转换为字符串
        data = json.dumps(data, indent=4)
        # 将指针移动到文件开头，因为文件读取后，指针默认在尾部。
        fs.seek(0)
        # 写入数据
        fs.write(data)
        # 关闭文件
        fs.close()


if __name__ == '__main__':
    main()