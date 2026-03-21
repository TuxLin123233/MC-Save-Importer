from config import *


def zip_extract(zip_path: str, extract_path: str, name: str) -> None:
    """解压ZIP存档到指定目录

    Args:
        zip_path: ZIP压缩包路径
        extract_path: 解压目标目录路径
        name: 存档名称（与ZIP文件名相同）

    Returns:
        None
    """
    # 检查临时目录是否存在，如果不存在则创建
    if not path_config.TEMP_PATH.exists():
        path_config.TEMP_PATH.mkdir(exist_ok=True)

    # 先解压到临时文件夹
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(path_config.TEMP_PATH)

    # 获取临时目录中的所有文件和文件夹
    extracted_items = list(Path(path_config.TEMP_PATH).glob('*'))
    # 检查ZIP文件是否包含任何内容（防止空ZIP文件）
    if not extracted_items:
        raise ValueError(f"ZIP文件 {zip_path} 中没有找到可提取的内容")

    origin_path = extracted_items[0]
    # 移动文件夹并重新命名
    shutil.move(origin_path, Path(extract_path) / name)


def get_image(image_name: str, size: tuple) -> ctk.CTkImage:
    """获取CTkImage图像对象（支持缩放）

    Args:
        image_name: img文件夹中的PNG文件名（不含扩展名）
        size: 图片尺寸元组 (width, height)

    Returns:
        ctk.CTkImage: 可缩放图像对象
    """
    import sys
    
    # 检查是否在PyInstaller打包环境中运行
    if getattr(sys, 'frozen', False):
        # 打包环境：使用sys._MEIPASS获取临时解压目录
        # PyInstaller会将数据文件解压到sys._MEIPASS目录
        base_path = sys._MEIPASS # type: ignore
        img_path = Path(base_path, 'img', f"{image_name}.png")
    else:
        # 开发环境：图片在项目根目录的img文件夹中
        # utils.py在src目录，所以需要../img
        base_dir = Path(__file__).parent  # src目录
        project_root = base_dir.parent  # 项目根目录
        img_path = project_root / 'img' / f"{image_name}.png"
    
    pil_image = Image.open(img_path)
    
    return ctk.CTkImage(
        light_image=pil_image,
        dark_image=pil_image,
        size=size
    )


def folder_dialog(title: str) -> str:
    """调用文件管理器选择文件夹路径

    Args:
        title: 对话框标题

    Returns:
        str: 选择的文件夹路径，如果取消则为空字符串
    """
    folder_path = filedialog.askdirectory(title=title, mustexist=True)
    # 如果用户取消了对话框，返回空字符串；否则返回选择的路径
    if folder_path:
        return folder_path
    else:
        return ""


def write_data(data: dict) -> None:
    """写入数据到配置文件

    Args:
        data: 要写入的数据字典

    Returns:
        None
    """
    # 写入数据
    with open(path_config.DATA_PATH, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)    # 如果文件没有也会自动创建

def read_data() -> dict:
    """从配置文件读取数据

    Args:
        无

    Returns:
        dict: 配置数据字典，如果文件不存在则返回默认配置
    """
    if not path_config.DATA_PATH.exists():
        return {
            "minecraft_path": "",
            "migrate": False
        }
    with open(path_config.DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def center_window(window:ctk.CTk|ctk.CTkToplevel):
    """让窗口居中显示

    Args:
        window: 窗口对象

    Returns:
        None
    """

    window.update_idletasks()  # 确保窗口尺寸已计算
        
    # 获取屏幕尺寸
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # 获取窗口大小
    win_width = window.winfo_width()
    win_height = window.winfo_height()
    
    # 计算居中位置
    x = (screen_width - win_width) // 2
    y = (screen_height - win_height) // 2
    
    # 一次性设置位置(不改变大小)
    window.geometry(f"+{x}+{y}")
        

def auto_label_window_width(label:ctk.CTkLabel, window:ctk.CTk|ctk.CTkToplevel, window_height:int) -> None:
    """自动根据Label文字宽度设置窗口宽度

    Args:
        label: Label组件对象
        window: 窗口对象
        window_height: 窗口高度

    Returns:
        None
    """
    # 先渲染才能获取尺寸
    window.update_idletasks()
    
    # 获取文本尺寸
    text_width = label.winfo_reqwidth()
    window.geometry(f"{text_width + 40}x{window_height}")    

def is_minecraft_folder(minecraft_path) -> dict:
    """判断是否为minecraft路径

    Args:
        minecraft_path: 要检查的文件夹路径

    Returns:
        dict: 包含检查结果的字典
            - find (bool): 是否为有效的.minecraft文件夹
            - migrate (bool): 是否为版本迁移结构（存档在versions目录下）
    """
    result:dict = {
        "find": False,
        "migrate": False
    }
    
    if not Path(minecraft_path, 'launcher_profiles.json').exists():     # 不是一个.minecraft目录
        return result
    
    if Path(minecraft_path, 'saves').exists() :  # 标准结构
        result['find'] = True
    elif Path(minecraft_path, 'versions').exists():     # 版本迁移结构
        result['find'] = True
        result['migrate'] = True
        
    return result