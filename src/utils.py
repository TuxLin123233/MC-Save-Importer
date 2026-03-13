from config import *


def zip_extract(zip_path: str, extract_path: str, name: str) -> None:
    """解压ZIP存档到指定目录

    Args:
        zip_path (str): ZIP压缩包路径
        extract_path (str): 解压目标目录路径
        name (str): 存档名称（与ZIP文件名相同）
    """
    # 检查临时目录是否存在，如果不存在则创建
    if not os.path.exists(TEMP_PATH):
        os.makedirs(TEMP_PATH)

    # 先解压到临时文件夹
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(TEMP_PATH)

    # 获取临时目录中的所有文件和文件夹
    extracted_items = glob.glob(os.path.join(TEMP_PATH, '*'))
    # 检查ZIP文件是否包含任何内容（防止空ZIP文件）
    if not extracted_items:
        raise ValueError(f"ZIP文件 {zip_path} 中没有找到可提取的内容")

    origin_path = extracted_items[0]
    # 移动文件夹并重新命名
    shutil.move(origin_path, os.path.join(extract_path, name))


def get_image(image_name: str, size: tuple) -> ctk.CTkImage:
    """获取CTkImage图像对象（支持缩放）

    Args:
        image_name (str): img文件夹中的PNG文件名（不含扩展名）
        size (tuple): 图片尺寸元组 (width, height)

    Returns:
        ctk.CTkImage: 可缩放图像对象
    """
    import sys
    
    # 检查是否在PyInstaller打包环境中运行
    if getattr(sys, 'frozen', False):
        # 打包环境：使用sys._MEIPASS获取临时解压目录
        # PyInstaller会将数据文件解压到sys._MEIPASS目录
        base_path = sys._MEIPASS # type: ignore
        img_path = os.path.join(base_path, 'img', f"{image_name}.png")
    else:
        # 开发环境：图片在项目根目录的img文件夹中
        # utils.py在src目录，所以需要../img
        base_dir = os.path.dirname(__file__)  # src目录
        project_root = os.path.dirname(base_dir)  # 项目根目录
        img_path = os.path.join(project_root, 'img', f"{image_name}.png")
    
    pil_image = Image.open(img_path)
    
    return ctk.CTkImage(
        light_image=pil_image,
        dark_image=pil_image,
        size=size
    )


def folder_dialog(title: str) -> str:
    """调用文件管理器选择文件夹路径

    Args:
        title (str): 对话框标题

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
        data (dict): 要写入的数据字典
    """
    try:
        # 确保目录存在
        data_dir = os.path.dirname(DATA_PATH)
        if data_dir and not os.path.exists(data_dir):
            os.makedirs(data_dir, exist_ok=True)
        
        # 写入数据
        with open(DATA_PATH, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except (IOError, OSError, json.JSONEncodeError) as e: # type: ignore
        # 记录错误但不影响程序运行（可以添加日志记录）
        print(f"写入配置文件失败: {e}")
        # 可以选择重新抛出异常或静默处理
        raise


def read_data() -> dict:
    """从配置文件读取数据

    Returns:
        dict: 配置数据字典，如果文件不存在则返回默认配置
    """
    if not os.path.exists(DATA_PATH):
        # 文件不存在，返回默认配置
        return {"minecraft_path": ""}
    
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        # 文件损坏或读取失败，返回默认配置
        return {"minecraft_path": ""}