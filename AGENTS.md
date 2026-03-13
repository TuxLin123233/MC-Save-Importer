# Minecraft 存档管理器 - AGENTS.md

本文档为 AI 助手提供项目上下文信息，用于指导未来的交互和开发任务。

## 项目概述

**Minecraft 存档管理器** 是一个专为 Minecraft Java版 设计的图形化存档管理工具。它允许玩家轻松导入、导出和管理游戏存档，提供直观的用户界面和便捷的操作流程。

**核心功能**：
- 📥 **导入存档**：将下载的 ZIP 格式地图解压到 `.minecraft/saves` 文件夹
- 📤 **导出备份**：将现有存档打包备份（待实现）
- 📋 **存档列表**：查看和管理所有存档（待实现）
- ❤️ **赞助支持**：支持开发者（待实现）

## 技术栈

- **编程语言**：Python 3.10+
- **GUI 框架**：CustomTkinter（现代化 Tkinter 封装）
- **图像处理**：Pillow（PIL Fork）
- **打包工具**：PyInstaller
- **数据格式**：JSON（配置文件）

## 项目结构

```
存档管理器/
├── src/                    # 源代码目录
│   ├── main.py            # 程序入口点
│   ├── gui.py             # 图形用户界面类
│   ├── utils.py           # 工具函数（解压、文件操作等）
│   ├── config.py          # 配置常量和导入
│   └── __pycache__/       # Python 字节码缓存
├── img/                   # 图片资源目录
│   ├── steve.png          # 史蒂夫头像
│   ├── map.png            # 地图图标
│   ├── box.png            # 箱子图标
│   ├── book_pen.png       # 书与笔图标
│   ├── golden_apple.png   # 金苹果图标
│   └── screenshot.png     # 应用截图
├── fonts/                 # 字体资源目录
│   ├── HarmonyOS_Sans_SC_Medium.ttf   # HarmonyOS Sans SC Medium 字体
│   └── HarmonyOS_Sans_SC_Regular.ttf  # HarmonyOS Sans SC Regular 字体
├── temp/                  # 临时文件目录（解压操作使用）
├── .venv/                 # Python 虚拟环境
├── .github/workflows/     # GitHub Actions 工作流
│   └── build-exe.yml      # 自动构建 EXE 的工作流
├── data.json              # 用户配置文件（存储 .minecraft 路径）
├── icon.ico               # 应用程序图标
├── requirements.txt       # Python 依赖包列表
├── README.md              # 项目说明文档
├── AGENTS.md              # AI 助手上下文文档（本文档）
├── action_history.txt     # 开发动作历史记录
└── .gitignore             # Git 忽略规则
```

## 环境设置

### 1. 安装 Python 依赖
```bash
pip install -r requirements.txt
```

### 2. 依赖包说明
- `customtkinter==5.2.2`：现代化 Tkinter 界面库
- `pillow==12.1.1`：图像处理库
- `pyinstaller==6.19.0`：打包工具
- 其他支持包：altgraph, darkdetect, packaging 等

## 构建与运行

### 运行开发版本
```bash
cd /home/tux/编程/存档管理器
.venv/bin/python src/main.py
```

### 构建可执行文件
```bash
cd src
pyinstaller -F --noconsole --icon="../icon.ico" --name="存档管理器" --add-data="../img;img" main.py
```

构建后的可执行文件将生成在 `dist/` 目录中。参数说明：
- `-F`: 打包成单个可执行文件
- `--noconsole`: 隐藏控制台窗口（仅Windows）
- `--icon`: 设置应用程序图标
- `--name`: 可执行文件名称
- `--add-data`: 包含图片资源文件夹（源路径;目标路径）

## 打包发布

项目使用 GitHub Actions 自动构建 Windows 可执行文件。工作流配置位于 `.github/workflows/build-exe.yml`。

**手动打包步骤**：
1. 确保所有依赖已安装
2. 运行上述 PyInstaller 命令
3. 测试生成的 EXE 文件
4. 创建发布版本并上传

## 开发规范

### 代码风格
- **语言**：代码和注释使用中文，便于国内开发者理解
- **命名**：使用英文变量名和函数名，遵循 snake_case 命名约定
- **文档**：所有函数使用中文文档字符串说明参数和返回值
- **导入**：在 config.py 中集中管理导入，其他文件通过 `from config import *` 引用

### 架构模式
- **分离关注点**：GUI 逻辑、工具函数、配置常量分别位于不同文件
- **模块化设计**：每个功能模块独立封装，便于维护和测试
- **配置驱动**：用户设置存储在 data.json 中，程序状态可持久化

### 资源管理
- **图片资源**：所有图标和图片放置在 `img/` 目录
- **临时文件**：使用 `temp/` 目录处理中间文件，程序结束后清理
- **配置文件**：`data.json` 存储用户特定的 Minecraft 路径

### 错误处理
- 使用 `try-except` 处理文件操作异常
- 提供用户友好的错误提示消息
- 验证用户输入和文件路径的有效性

## 动作历史记录

项目维护 `action_history.txt` 文件，记录重要的开发操作和变更历史。该文件采用标准化格式，包含时间戳、操作者、操作类型和详细描述。

## 注意事项

### 平台兼容性
- 主要针对 Windows 平台开发
- 理论上支持 macOS 和 Linux，但未充分测试
- Minecraft Java版 的存档路径可能因操作系统而异

### 用户数据
- 程序不会收集或上传用户隐私数据
- 仅本地存储 Minecraft 路径配置
- 临时文件在处理完成后自动清理

### 已知限制
- 仅支持 ZIP 格式的存档文件
- 需要用户手动指定 .minecraft 文件夹位置
- 界面固定为 400x290 像素，不支持调整大小
- 部分功能（导出、列表、赞助）尚未实现

## 扩展开发

### 添加新功能
1. 在 `gui.py` 的 `create_buttons()` 方法中添加新按钮
2. 实现对应的功能方法
3. 如需新工具函数，在 `utils.py` 中添加
4. 更新界面图片资源到 `img/` 目录

### 修改界面样式
- 颜色主题在 `gui.py` 的按钮定义中配置
- 字体大小和样式通过 `CTkFont` 设置
- 布局使用 CustomTkinter 的 Pack 几何管理器

### 国际化支持
当前版本仅支持中文界面。如需添加多语言支持：
1. 创建语言文件（如 `locales/` 目录）
2. 修改 GUI 文本为可翻译字符串
3. 实现语言切换逻辑

## 故障排除

### 常见问题
1. **找不到 .minecraft 文件夹**：手动浏览到用户目录下的 AppData/Roaming/.minecraft
2. **ZIP 文件解压失败**：确保 ZIP 文件未损坏且包含有效的存档结构
3. **界面显示异常**：检查 PIL 和 CustomTkinter 版本兼容性

### 调试建议
- 在命令行中运行程序查看错误输出
- 检查 `temp/` 目录中的中间文件
- 验证 `data.json` 文件格式是否正确
- 查看 `action_history.txt` 了解最近的变更

---

*本文档最后更新：2026年3月13日*  
*对应项目版本：基于 git commit ef7eaa1（配置文件读取修复）*  
*文档维护：iFlow CLI 自动化系统*