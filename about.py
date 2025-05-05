import maliang
import webbrowser
import update
from tkinter import messagebox


def thanks(window):
    thanks_window = maliang.Toplevel(window, size=(400, 250), icon="./img/EECT_logo.ico")
    thanks_window.center()
    thanks_window_cv = maliang.Canvas(thanks_window, auto_zoom=False)
    thanks_window_cv.place(width=400, height=250)
    thanks_window.title("鸣谢")
    thanks_window.resizable(False, False)

    thanks_text = maliang.Text(thanks_window_cv, (20, 20), text="此程序使用了以下开源项目：")
    thanks_maliang = maliang.IconButton(thanks_window_cv, (20, 60), text="Maliang", image=maliang.PhotoImage(file="./img/maliang_logo.png").resize(32, 32), command=lambda: webbrowser.open_new_tab("https://github.com/Xiaokang2022/maliang"))


def list_of_developers(window):
    developers_window = maliang.Toplevel(window, size=(400, 250), icon="./img/EECT_logo.ico")
    developers_window.center()
    developers_window_cv = maliang.Canvas(developers_window, auto_zoom=False)
    developers_window_cv.place(width=400, height=250)
    developers_window.title("开发人员名单")
    developers_window.resizable(False, False)

    developers_text = maliang.Text(developers_window_cv, (20, 20), text="开发者：\n\nLyang1273 - 代码、图标\nWakana-0 - 图标")

    # 前往贡献页
    contributors = maliang.Button(developers_window_cv, (20, 210), text="在GitHub上查看所有贡献者", fontsize=12, command=lambda: webbrowser.open_new("https://github.com/EECT/EECT/graphs/contributors"))


def open_source_license(window):
    license_window = maliang.Toplevel(window, size=(584, 430), icon="./img/EECT_logo.ico")
    license_window.center()
    license_window_cv = maliang.Canvas(license_window, auto_zoom=False)
    license_window_cv.place(width=584, height=445)
    license_window.title("开放源代码许可")
    license_window.resizable(False, False)

    license_text = maliang.Text(license_window_cv, (20, 5), text="本软件遵照 MIT License 开源协议开放源代码")
    license = maliang.Label(license_window_cv, (5, 50), text="""MIT License

Copyright (c) 2025 EECT Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""", fontsize=12)


def free_software_statement(window):
    free_software_window = maliang.Toplevel(window, size=(400, 350), icon="./img/EECT_logo.ico")
    free_software_window.center()
    free_software_window_cv = maliang.Canvas(free_software_window, auto_zoom=False)
    free_software_window_cv.place(width=400, height=350)
    free_software_window.title("声明")
    free_software_window.resizable(False, False)

    free_software_text = maliang.Text(free_software_window_cv, (20, 20), text="""感谢您选择电教工具箱 (EECT)，为了保护您的合法
权益，您需要仔细阅读此声明，避免受到诈骗、盗版软
件的侵害。

本软件禁止任何形式的商业倒卖，包括但不限于：
未经允许直接出售本软件或修改版本，以及源代码；
捆绑销售、预装收费；以“服务费”“授权费”等名义
变相收费。

如果您发现此类情况，请及时向EECT团队反馈；如果
您已经购买，请立即退款。""", fontsize=14)

    open_source_license_button = maliang.Button(free_software_window_cv, (20, 260), text="开放源代码许可", command=lambda: open_source_license(free_software_window))
    go_github = maliang.Button(free_software_window_cv, (210, 260), text="前往项目仓库", command=lambda: webbrowser.open_new("https://github.com/EECT/EECT"))


def pull_up_the_update():
        ud = update.update()
        if ud[0]:
            compare = "有可用更新！"
        else:
            compare = "当前已是最新版本！"
        messagebox.showinfo("EECT update", f"{compare}\n\n当前版本：{update.check_version(1)}\n版本码：{update.check_version(0)}              \n\n最新版本：{ud[1]}\n版本码：{ud[2]}\n发布日期：{ud[3]}\n更新日志：{ud[4]}\n重要程度：{ud[5]}")


def update_window(window):
    new_version, new_version_code, date, changelog, importance = "--", "--", "--", "--", "--"

    update_window = maliang.Toplevel(window, size=(500, 350), icon="./img/EECT_logo.ico")
    update_window.center()
    update_window_cv = maliang.Canvas(update_window, auto_zoom=False)
    update_window_cv.place(width=400, height=350)
    update_window.title("EECT更新")
    update_window.resizable(False, False)
    '''这一块暂时不动
    update_text = maliang.Text(update_window_cv, (90, 20), text="EECT更新", fontsize=32)
    update_img = maliang.Image(update_window_cv, (20, 16), image=maliang.PhotoImage(file="./img/EECT_update.png").resize(60, 50))
    update_info = maliang.Text(update_window_cv, (20, 80), text="点击“检查更新”检查当前使用的EECT是否是最新的", fontsize=14)
    version_info = maliang.Text(update_window_cv, (20, 160), text=f"当前版本：{update.check_version(1)}\n版本码：{update.check_version(0)}\n\n最新版本：{new_version}\n版本码：{new_version_code}\n发布日期：{date}\n更新日志：{changelog}\n重要程度：{importance}", fontsize=14)
    '''

    update_button = maliang.Button(update_window_cv, (20, 120), text="检查更新", command=pull_up_the_update)


if __name__ == "__main__":
    root = maliang.Tk()
    thanks(root)
    list_of_developers(root)
    open_source_license(root)
    free_software_statement(root)
    root.mainloop()
