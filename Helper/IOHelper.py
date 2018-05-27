#方便读写的类
def Write(data):
    file_name = "./1.text"
    with open(file_name, 'a') as f:
        f.write(data)


