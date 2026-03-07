import customtkinter as ctk

class App:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("🗃存档管理器")
        self.window.geometry("400x300")

        ctk.set_appearance_mode("light")

        # 大标题
        title = ctk.CTkLabel(
            self.window,
            text="Minecraft 存档管理器",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#546EA0"  # 主题蓝色
        )
        title.pack(pady=20)

        # 按钮容器(整个区域)
        btn_container = ctk.CTkFrame(self.window, fg_color="transparent")
        btn_container.pack(expand=True, fill="both", padx=40, pady=20)

        # 第一行容器(flex row)
        row1 = ctk.CTkFrame(btn_container, fg_color="transparent")
        row1.pack(expand=True, fill="both", pady=10)

        # 第一行两个按钮
        btn1 = ctk.CTkButton(
            row1,
            text="导入存档",
            font=ctk.CTkFont(size=20),
            command=self.import_save,
            fg_color="#96CA25",
            hover_color="#88B723",
            text_color="#EDFFEB"
        )
        btn1.pack(side="left", expand=True, fill="both", padx=10)

        btn2 = ctk.CTkButton(
            row1, 
            text="导出备份", 
            font=ctk.CTkFont(size=20),
            fg_color="#B03855",
            hover_color="#9B2944",
            text_color="#E0D9DB",
        )
        btn2.pack(side="left", expand=True, fill="both", padx=10)

        # 第二行容器(flex row)
        row2 = ctk.CTkFrame(btn_container, fg_color="transparent")
        row2.pack(expand=True, fill="both", pady=10)

        # 第二行两个按钮
        btn3 = ctk.CTkButton(
            row2, 
            text="查看列表", 
            font=ctk.CTkFont(size=20),
            fg_color="#3b8ed0",
            hover_color="#2978b8",
            text_color="#DCE6E8"
        )
        btn3.pack(side="left", expand=True, fill="both", padx=10)

        btn4 = ctk.CTkButton(
            row2, 
            text="赞助一下", 
            font=ctk.CTkFont(size=20),
            fg_color="#F0A054",
            hover_color="#DC893C",
            text_color="#FFFFFF"
        )
        btn4.pack(side="left", expand=True, fill="both", padx=10)

    def import_save(self):
        # 创建新窗口
        import_window = ctk.CTk()
        import_window.title("导入存档")
        import_window.geometry("500x400")

app = App()
app.window.mainloop()