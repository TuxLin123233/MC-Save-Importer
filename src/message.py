from config import *
from utils import *

class Message:
    def __init__(self, parent_window:ctk.CTk) -> None:
        self.window = ctk.CTkToplevel(parent_window)
        self.window.configure(fg_color="#D3D3D3")
        
        # 置顶于父窗口
        self.window.transient(parent_window)
        
        # 用于保存用户按钮按下的内容
        self.result = False
        
        self.btn_config = {
            "width": 90,
            "height": 40,
            "anchor": "center",      # 整体居中
            "border_width": 2,
            "border_color": "#CFCFCF",
            "corner_radius": 13,
        }
    
    def on_confirm(self, value:bool=False):
        # 确认操作
        self.result = value
        self.window.destroy()
    
    def info(self, title:str, text:str, font:ctk.CTkFont):
        """消息通知框"""
        self.window.title(title)
        
        # 启动音效
        playsound(path_config.get_sound_path('message_info.mp3'), block=False)
        
        # 通知框文本
        content = ctk.CTkLabel(
            self.window,
            text=text,
            font=font
        )
        content.pack(pady=(5, 0))
        
        # 确定按钮
        confirm_button = ctk.CTkButton(
            self.window,
            text="确定",
            font=font,
            fg_color="#5E5E5E",
            hover_color="#505050",
            command=lambda:self.on_confirm(True), 
            **self.btn_config
        )
        confirm_button.pack(pady=(10, 0))
        
        # 调整窗口大小
        auto_label_window_width(content, self.window, 95)
        center_window(self.window)
        
        # 模态化窗口
        self.window.grab_set()
        
        self.window.wait_window()
        
        return self.result

    def yes_no(self, title:str, text:str, font:ctk.CTkFont):
        """选择框"""
        self.window.title(title)
        
        # 启动音效
        playsound(path_config.get_sound_path('message_yes_no.mp3'), block=False)
        
        # 选择框文本
        content = ctk.CTkLabel(
            self.window,
            text=text, 
            font=font
        )
        content.pack(pady=(5, 0))
        
        # 选择按钮容器
        btn_frame = ctk.CTkFrame(
            self.window,
            fg_color="transparent"
        )
        btn_frame.pack(pady=(10, 0))
        
        yes_button = ctk.CTkButton(
            btn_frame,
            text="好的",
            fg_color="#86aa19",
            hover_color="#799b16",
            command=lambda:self.on_confirm(True),
            **self.btn_config
        )
        no_button = ctk.CTkButton(
            btn_frame,
            text="不要",
            command=lambda:self.on_confirm(False),
            **self.btn_config
        )
        yes_button.pack(side="left", padx=(0, 15))
        no_button.pack(side="left")
        
        # 调整窗口大小
        auto_label_window_width(content, self.window, 95)
        center_window(self.window)
        
        # 模态化窗口
        self.window.grab_set()
        self.window.wait_window()
        
        return self.result