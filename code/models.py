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

class Cli:
    def __init__(self):
        self.box = Box()
        self.prompt_menu = {    # 提示菜单
            'menu': "查看菜单",
            'exit': "退出脚本",
            'save_move':"执行存档批量导入到启动器"
        }

        self.function_menu = {     # 功能菜单
            'menu': self.show_menu,
            'save_move': self.box.move_saves
        }

    def show_menu(self):
        # 展示提示菜单
        print("\n" + "="*30)
        
        for k, v in self.prompt_menu.items():
            print(f"{k}: {v}")

        print("\n" + "="*30)
    
    def prompt(self):
        # 交互功能

        # 打印欢迎语
        print("""
        ╔══════════════════════════╗
        ║       小林工具箱 v1.5      
        ║   欢迎使用! 输入menu看菜单  
        ╚══════════════════════════╝
        """)

        while True:
            user = input("=> ")

            if user == 'exit':
                print("<期待下次与你见面>")
                input()
                break

            try:
                self.function_menu[user]()
            except KeyError:
                print("<找不到该功能>")