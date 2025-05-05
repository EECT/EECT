# https://github.com/EECT/EECT
import maliang
from maliang import theme, toolbox
from tkinter import messagebox
import os
import datetime
import tomllib
import webbrowser

# 自制模块
import shutdown
import FindGames
import about
import reg
import settings


# 读取配置文件
with open('./config/config.toml', 'rb') as f:
    config = tomllib.load(f)
    try:
        ExperienceTheFeatures = config['ExperienceTheFeatures']
        Cache = config['Cache']
        UseRegistry = config['UseRegistry']
    except KeyError as e:
        ExperienceTheFeatures = False
        messagebox.showwarning("配置文件错误", f"读取配置文件时出错\n\n详细信息：{e}")
try:
    with open('./config/version.toml', 'rb') as f:
        version = tomllib.load(f)
except FileNotFoundError as e:
    messagebox.showerror("配置文件错误", f"无法获取当前的版本信息\n\n详细信息：{e}")

    current_version = version['version']
    current_version_code = version['version_code']


size = 600, 400
toplevel_size = 430, 350
root = maliang.Tk(size=size, icon="./img/EECT_logo.ico")
cv = maliang.Canvas(root, auto_zoom=True)
cv.place(width=600, height=400)
root.center()
root.title("电教工具箱")
root.resizable(False, False)
if ExperienceTheFeatures:
    root.title("EECT - 已启用体验功能")


# TODO: 这他妈写的太乱了，记得找个时间重构


def About():
    About = maliang.Toplevel(root, size=(800, 600), icon="./img/EECT_logo.ico")
    About.center()
    About_cv = maliang.Canvas(About, auto_zoom=False)
    About_cv.place(width=800, height=600)
    About.title("关于电教工具箱")
    theme.customize_window(About, disable_maximize_button=True, disable_minimize_button=True)
    About_title = maliang.Text(About_cv, (140, 20), text="电教工具箱——面向不太会使用电脑的电教委的小工具")
    About_text = maliang.Text(About_cv, (20, 100), text=f"Version：{current_version} ({current_version_code})")
    List_of_developers = maliang.Button(About_cv, (20, 250), text="  开 发 人 员 名 单  ", command=lambda: about.list_of_developers(About))
    thanks = maliang.Button(About_cv, (230, 250), text="          鸣 谢           ", command=lambda: about.thanks(About))
    open_source_license = maliang.Button(About_cv, (440, 250), text=" 开 放 源 代 码 许 可 ", command=lambda: about.open_source_license(About))
    free_software_statement = maliang.Button(About_cv, (20, 350), text="     免 费 软 件 声 明     ", command=lambda: about.free_software_statement(About))
    go_github = maliang.Button(About_cv, (20, 300), text="            前 往 此 项 目 仓 库            ", command=lambda: webbrowser.open_new("https://github.com/EECT/EECT"))
    issues = maliang.Button(About_cv, (385, 300), text="            问 题 反 馈            ", command=lambda: webbrowser.open_new("https://github.com/EECT/EECT/issues"))
    update = maliang.Button(About_cv, (400, 97), text="检查更新", command=about.pull_up_the_update)

    c = maliang.Label(About_cv, (20, 530), text="Copyright © 2025 EECT Team, All Rights Reserved.\nEECT开发团队 版权所有，保留所有权利。", fontsize=12)

def auto_shutdown():
    auto_shutdown_window = maliang.Toplevel(root, size=(400, 250), icon="./img/EECT_logo.ico")
    auto_shutdown_window.center()
    auto_shutdown_window_cv = maliang.Canvas(auto_shutdown_window, auto_zoom=False)
    auto_shutdown_window_cv.place(width=400, height=300)
    auto_shutdown_window.title("电教工具箱 - 设置定时关机")
    theme.customize_window(auto_shutdown_window, disable_maximize_button=True, disable_minimize_button=True)

    # 创建文本框和按钮
    shutdown_time_entry = maliang.InputBox(auto_shutdown_window_cv, (50, 20), (90, 40))
    shutdown_time_entry.insert(0, '60')  # 默认值为60秒

    shutdown_button = maliang.Button(auto_shutdown_window_cv, (150, 20), text='在设定的时间后关机',command=lambda: shutdown.set_shutdown_time(shutdown_time_entry))

    restart_time_entry = maliang.InputBox(auto_shutdown_window_cv, (50, 80), (90, 40))
    restart_time_entry.insert(0, '60')  # 默认值为60秒

    restart_button = maliang.Button(auto_shutdown_window_cv, (150, 80), text='在设定的时间后重启',command=lambda: shutdown.set_restart_time(restart_time_entry))

    cancel_button = maliang.Button(auto_shutdown_window_cv, (120, 140), text='取消关机或重启',command=shutdown.set_cancel_shutdown)

    tip = maliang.Label(auto_shutdown_window_cv, (35, 200), fontsize=12, text="Tips: 你也可以在cmd输入 shutdown /s /t [秒数] 定时关机")


def Windows_tools_toplevel():
    windows_tools_window = maliang.Toplevel(root, size=toplevel_size, icon="./img/EECT_logo.ico")
    windows_tools_window.center()
    windows_tools_window_cv = maliang.Canvas(windows_tools_window, auto_zoom=False)
    windows_tools_window_cv.place(width=400, height=350)
    windows_tools_window.title("电教工具箱 - Windows工具")
    windows_tools_window.resizable(False, False)
    theme.customize_window(windows_tools_window, disable_maximize_button=True, disable_minimize_button=True)

    warning = maliang.Label(windows_tools_window_cv, (10, 20), fontsize=12, text="tips: 带有*的工具务必在专业指导下使用！")
    windows_reg = maliang.Button(windows_tools_window_cv, (10, 70), text='*注册表编辑器', command=lambda: os.system("start regedit"))
    windows_gpedit = maliang.Button(windows_tools_window_cv, (170, 70), text='*组策略编辑器',command=lambda: os.system("start gpedit.msc"))
    windows_cleanmgr = maliang.Button(windows_tools_window_cv, (10, 120), text='磁盘清理', command=lambda: os.system("start cleanmgr"))
    windows_compmgmt = maliang.Button(windows_tools_window_cv, (120, 120), text='*计算机管理', command=lambda: os.system("start compmgmt.msc"))
    windows_taskschd = maliang.Button(windows_tools_window_cv, (260, 120), text='任务计划程序', command=lambda: os.system("start taskschd.msc"))
    windows_df = maliang.Button(windows_tools_window_cv, (10, 170), text='*高级安全 Windows Defender 防火墙', command=lambda: os.system("start WF.msc"))
    more_tools = maliang.Button(windows_tools_window_cv, (10, 290), text='*更多高级工具', command=lambda: os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Administrative Tools"))


def find_games_toplevel():
    find_games_window = maliang.Toplevel(root, size=toplevel_size, icon="./img/EECT_logo.ico")
    find_games_window.center()
    find_games_window_cv = maliang.Canvas(find_games_window, auto_zoom=False)
    find_games_window_cv.place(width=400, height=350)
    find_games_window.title("电教工具箱 - 查找电脑上的游戏")
    find_games_window.resizable(False, False)
    theme.customize_window(find_games_window, disable_maximize_button=True, disable_minimize_button=True)


    def find_games_window_def(root):
        find_games_windows = maliang.Toplevel(find_games_window, size=(250, 70), title="正在查找……")
        find_games_windows.toolwindow(True)
        find_games_windows.center()
        find_games_windows_cv = maliang.Canvas(find_games_windows, auto_zoom=False)
        find_games_windows_cv.place(width=400, height=350)

        find_spinner = maliang.Spinner(find_games_windows_cv, (10, 15), mode="indeterminate")
        finding_text = maliang.Text(find_games_windows_cv, (55, 10), text=f"正在扫描{root}，请稍后……\n具体耗时由文件数量决定", fontsize=14)

        data = FindGames.find_games(root)

        if not Cache:
            finding_text.destroy()
            find_spinner = maliang.Spinner(find_games_windows_cv, (10, 15), mode="indeterminate")
            finding_text = maliang.Text(find_games_windows_cv, (55, 10), text=f"扫描失败\n当前配置不允许使用缓存。\n因为 Cache={Cache}", fontsize=14)
            messagebox.showerror("功能被锁定", "当前配置不允许使用缓存相关功能。")
            find_games_windows.topmost(True)
            return

        # 获取当前时间
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")

        try:
            with open("./cache/cache", "w") as f:
                f.write("")
        except FileNotFoundError:
            os.makedirs("./cache")
            with open("./cache/cache", "w") as f:
                f.write("")

        with open(f"./cache/查找游戏-{current_time}.txt", "w", encoding="utf-8") as f:
            f.write("查找游戏结果：\n")
            for game_name, game_path in data:
                f.write(f"{game_name}: {game_path}\n")

        find_games_windows_cv.destroy()
        find_games_windows_cv = maliang.Canvas(find_games_windows, auto_zoom=False)
        find_games_windows_cv.place(width=400, height=350)
        button = maliang.Button(find_games_windows_cv, (10, 10), text="查看结果", command=lambda: os.startfile(os.path.abspath(f"./cache/查找游戏-{current_time}.txt")))



    find_games_text = maliang.Text(find_games_window_cv, (20, 20), text="在以下分区查找游戏【如：D（D盘）】：", fontsize=18)
    find_games_entry = maliang.InputBox(find_games_window_cv, (20, 60), (90, 40))
    find_games_button = maliang.Button(find_games_window_cv, (150, 60), text="查找", command=lambda: find_games_window_def(find_games_entry.get()))
    find_games_label = maliang.Label(find_games_window_cv, (65, 260), text="注意：\n查找结果仅供参考，并非100%准确！\n如果找出游戏，请前往对应目录检查。", fontsize=14)


def software_recommendations_toplevel():
    software_recommendations_window = maliang.Toplevel(root, size=toplevel_size, icon="./img/EECT_logo.ico")
    software_recommendations_window.center()
    software_recommendations_window_cv = maliang.Canvas(software_recommendations_window, auto_zoom=False)
    software_recommendations_window_cv.place(width=400, height=350)
    software_recommendations_window.title("电教工具箱 - 软件推荐")
    software_recommendations_window.resizable(False, False)
    theme.customize_window(software_recommendations_window, disable_maximize_button=True, disable_minimize_button=True)


def taskbar():
    if not UseRegistry:
        messagebox.showerror("功能被锁定", "当前配置不允许使用注册表相关功能。")
        return

    taskbar_window = maliang.Toplevel(root, size=toplevel_size, icon="./img/EECT_logo.ico")
    taskbar_window.center()
    taskbar_window_cv = maliang.Canvas(taskbar_window, auto_zoom=False)
    taskbar_window_cv.place(width=450, height=350)
    taskbar_window.title("电教工具箱 - 设置任务栏")
    taskbar_window.resizable(False, False)
    theme.customize_window(taskbar_window, disable_maximize_button=True, disable_minimize_button=True)

    show_seconds = maliang.Button(taskbar_window_cv, (10, 20), text='在任务栏上显示秒', command=lambda: reg.show_seconds_in_system_clock(1))
    hide_seconds = maliang.Button(taskbar_window_cv, (200, 20), text='在任务栏上隐藏秒', command=lambda: reg.show_seconds_in_system_clock(0))

    show_weekday = maliang.Button(taskbar_window_cv, (10, 70), text='`在任务栏上显示星期', command=lambda: reg.show_weekday_in_taskbar(1))
    hide_weekday = maliang.Button(taskbar_window_cv, (220, 70), text='`在任务栏上隐藏星期', command=lambda: reg.show_weekday_in_taskbar(0))

    tips = maliang.Label(taskbar_window_cv, (10, 250), text="带`的功能有点问题，请谨慎使用。", fontsize=14)

    restart_explorer = maliang.Button(taskbar_window_cv, (10, 300), text='重启资源管理器', command=lambda: os.system("taskkill /f /im explorer.exe & start explorer.exe"))


home_text = maliang.Text(cv, (20, 20), text="“实用”小工具", fontsize=16)
home_button1 = maliang.Button(cv, (20, 60), text="定时关机", command=auto_shutdown)
home_button2 = maliang.Button(cv, (130, 60), text="查找电脑上的游戏", command=find_games_toplevel)
windows_tools_text = maliang.Text(cv, (20, 120), text="Windows工具 ∨", fontsize=16)
home_button3 = maliang.Button(cv, (20, 160), text="Windows工具", command=Windows_tools_toplevel)
home_button6 = maliang.Button(cv, (180, 160), text="设置任务栏", command=taskbar)

if ExperienceTheFeatures:
    software_recommendations_text = maliang.Text(cv, (20, 220), text="其他 ∨", fontsize=16)
    home_button4 = maliang.Button(cv, (20, 260), text="软件推荐`", command=software_recommendations_toplevel)

home_button5 = maliang.Button(cv, (20, 355), text="    关于    ", command=About)
settings_button = maliang.Button(cv, (130, 355), text="设置", command=lambda: settings.settingsGUI(root))


root.mainloop()
