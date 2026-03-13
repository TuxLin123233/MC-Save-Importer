"""
读取字体文件的元数据，获取正确的字体 family name
"""
from PIL import ImageFont

def get_font_family_name(font_path):
    """获取字体的 family name

    Args:
        font_path (str): 字体文件路径

    Returns:
        str: 字体的 family name
    """
    try:
        font = ImageFont.truetype(font_path)
        # 尝试获取字体名称
        font_name = font.getname()
        return font_name[0] if font_name else "Unknown"
    except Exception as e:
        print(f"读取字体失败: {e}")
        return None

if __name__ == "__main__":
    import os

    # 字体文件路径
    fonts_dir = os.path.join(os.path.dirname(__file__), "fonts")
    regular_font = os.path.join(fonts_dir, "HarmonyOS_Sans_SC_Regular.ttf")
    medium_font = os.path.join(fonts_dir, "HarmonyOS_Sans_SC_Medium.ttf")

    print("正在读取字体信息...")
    print("=" * 50)

    # 读取 Regular 字体
    if os.path.exists(regular_font):
        regular_name = get_font_family_name(regular_font)
        print(f"Regular 字体 family name: {regular_name}")
    else:
        print(f"找不到字体文件: {regular_font}")

    # 读取 Medium 字体
    if os.path.exists(medium_font):
        medium_name = get_font_family_name(medium_font)
        print(f"Medium 字体 family name: {medium_name}")
    else:
        print(f"找不到字体文件: {medium_font}")

    print("=" * 50)
    print("\n请在 config.py 中使用正确的 family name:")
    print("FONT_FAMILY_NAME = \"字体名称\"")
    print("\n然后在 gui.py 中使用:")
    print("self.font_button = ctk.CTkFont(family=FONT_FAMILY_NAME, size=16, weight=\"medium\")")