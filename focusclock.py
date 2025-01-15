# Clock
import tkinter as tk
import time
import winsound  # 仅适用于 Windows 系统

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        master.title("专注时钟")

        self.time_left = 25 * 60  # 25 分钟
        self.running = False

        self.label = tk.Label(master, text="剩余时间:")
        self.label.pack()

        self.time_display = tk.Label(master, text=self.format_time(self.time_left))
        self.time_display.pack()

        self.start_button = tk.Button(master, text="开始", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="停止", command=self.stop_timer)
        self.stop_button.pack()

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02}:{seconds:02}"

    def update_timer(self):
        if self.running:
            if self.time_left > 0:
                self.time_left -= 1
                self.time_display.config(text=self.format_time(self.time_left))
                self.master.after(1000, self.update_timer)
            else:
                self.running = False
                self.time_display.config(text="时间到!")
                # 播放提示音
                winsound.Beep(1000, 1000)  # 1000 Hz, 1秒

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def stop_timer(self):
        self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    timer_app = PomodoroTimer(root)
    root.mainloop()
