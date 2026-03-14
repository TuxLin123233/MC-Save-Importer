import os
import sys
import zipfile
import shutil
import glob
import json
from tkinter import messagebox, filedialog

from PIL import Image
import customtkinter as ctk


def get_base_path():
    """获取基础路径，支持开发环境和打包环境

    Returns:
        str: 基础路径字符串，开发环境返回项目根目录，打包环境返回可执行文件所在目录
    """
    if getattr(sys, 'frozen', False):
        # 打包环境：使用可执行文件所在目录
        return os.path.dirname(sys.executable)
    else:
        # 开发环境：使用项目根目录
        return os.path.dirname(os.path.dirname(__file__))

def get_font_path(font_name):
    """获取字体文件完整路径

    Args:
        font_name (str): 字体文件名称（含扩展名）

    Returns:
        str: 字体文件的完整绝对路径
    """
    # 检查是否在PyInstaller打包环境中运行
    if getattr(sys, 'frozen', False):
        # 打包环境：使用sys._MEIPASS获取临时解压目录
        base_path = sys._MEIPASS # type: ignore
        return os.path.join(base_path, 'fonts', font_name)
    else:
        # 开发环境：使用项目根目录的fonts文件夹
        return os.path.join(FONTS_PATH, font_name)

def get_sound_path(sound_name:str):
    """获取音频文件完整路径

    Args:
        sound_name (str): 音频文件名(含扩展名)
    """
    if getattr(sys, 'frozen', False):
        # 打包环境
        base_path = sys._MEIPASS # type:ignore
        return os.path.join(base_path, 'sounds', sound_name)
    else:
        # 开发环境
        return os.path.join(SOUND_PATH, sound_name)

# 获取基础路径(即以项目为开头)
BASE_PATH = get_base_path()

# 临时文件夹路径
TEMP_PATH = os.path.join(BASE_PATH, 'temp')

# 数据文件路径
DATA_PATH = os.path.join(BASE_PATH, 'data.json')

# 字体文件夹路径（仅用于开发环境）
FONTS_PATH = os.path.join(BASE_PATH, 'fonts')

# 字体文件名（用于加载文件）
FONT_REGULAR_FILENAME = "HarmonyOS_Sans_SC_Regular.ttf"
FONT_MEDIUM_FILENAME = "HarmonyOS_Sans_SC_Medium.ttf"

# 字体系统名称（用于创建字体）
FONT_REGULAR_NAME = "HarmonyOS Sans SC"           # 注意：有空格，没有下划线
FONT_MEDIUM_NAME = "HarmonyOS Sans SC Medium"     # 注意：有空格，没有下划线

# 字体文件路径
FONT_REGULAR_PATH = get_font_path(FONT_REGULAR_FILENAME)
FONT_MEDIUM_PATH = get_font_path(FONT_MEDIUM_FILENAME)

# 音频文件夹路径
SOUND_PATH = os.path.join(BASE_PATH, 'sounds')