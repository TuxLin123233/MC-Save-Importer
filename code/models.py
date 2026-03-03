from config import *
from utils import zip_extract

class Box:
    def __init__(self):
        if not os.path.exists(TEMP_PATH):   # 如果没有./temp文件夹
            os.makedirs(TEMP_PATH)
    
    def move_saves(self):
        """移动存档"""
        from_path = input("粘贴你下载好的地图文件夹路径：")
        to_path = input("粘贴.minecraft文件夹路径: ")
        # 获取所有zip的迭代器
        zip_files = glob.glob(os.path.join(from_path, "*.zip"))
        to_path = os.path.join(to_path, 'saves')
        # 进行逐个解压
        for i in zip_files:
            # 获取每个zip文件的路径
            zip_path = os.path.join(i)  
            # 获取zip文件名
            name = os.path.splitext(os.path.basename(i))[0]
            # 执行解压操作
            zip_extract(zip_path=zip_path, extract_path=to_path, name=name)
            print(f"存档: {name} 解压完成!")