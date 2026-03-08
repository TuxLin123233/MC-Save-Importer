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
    """获取基础路径，支持开发环境和打包环境"""
    if getattr(sys, 'frozen', False):
        # 打包环境：使用可执行文件所在目录
        return os.path.dirname(sys.executable)
    else:
        # 开发环境：使用项目根目录
        return os.path.dirname(os.path.dirname(__file__))


# 获取基础路径
BASE_PATH = get_base_path()

# 临时文件夹路径
TEMP_PATH = os.path.join(BASE_PATH, 'temp')

# 数据文件路径
DATA_PATH = os.path.join(BASE_PATH, 'data.json')