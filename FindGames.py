import os
import tomllib
import psutil
from tkinter import messagebox

def load_game_list():
    try:
        with open('./config/gamelists.toml', 'rb') as f:
            data = tomllib.load(f)
            return data.get('Game', {})
    except FileNotFoundError:
        print("游戏列表文件未找到")
        return {}

def search_by_name(root, game_list):
    found_games = []
    for game_name, game_exe in game_list.items():
        path = os.path.join(root, game_exe)
        print(f"搜索 {game_exe} 位于 {path}")  # 调试输出
        if os.path.exists(path):
            found_games.append((game_name, path))
    return found_games

def search_partition(partition, game_list):
    found_games = []
    for root, _, _ in os.walk(partition.mountpoint):
        games = search_by_name(root, game_list)
        found_games.extend(games)
    return found_games

def find_games(disk_letter):
    try:
        # 加载游戏列表
        game_list = load_game_list()
        if not game_list:
            return []


        # 获取磁盘分区信息
        partitions = psutil.disk_partitions()
        partition_to_search = None
        for partition in partitions:
            if partition.device.startswith(disk_letter + ':'):
                partition_to_search = partition
                break

        if not partition_to_search:
            print(f"磁盘 {disk_letter}")
            return []

        # 搜索分区
        found_games = search_partition(partition_to_search, game_list)

        if found_games:
            print(f"找到的游戏在分区 {partition_to_search.mountpoint}：")
            for game_name, game_path in found_games:
                print(f"{game_name}: {game_path}")
        else:
            print(f"未在分区 {partition_to_search.mountpoint} 找到任何游戏")

        return found_games
    except Exception as e:
        messagebox.showerror("错误", f"发生错误：{e}")
        return []


# 示例用法
if __name__ == "__main__":
    disk_letter = input("请输入文件所在磁盘字母（如D）：").strip().upper()
    if not disk_letter or not disk_letter.isalpha() or len(disk_letter) != 1:
        print("无效的磁盘字母")
    else:
        games_found = find_games(disk_letter)
        print("发现的游戏：", games_found)
