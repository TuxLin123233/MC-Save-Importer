import os
import zipfile
import shutil
import glob
import json
from tkinter import messagebox, filedialog

from PIL import Image
import customtkinter as ctk


TEMP_PATH = os.path.join('.', 'temp')   # ./temp文件夹路径
DATA_PATH = os.path.join('.', 'data.json')  # ./data.json文件夹路径