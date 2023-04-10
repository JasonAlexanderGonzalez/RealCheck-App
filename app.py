import psutil
import getpass
import tkinter as tk
import tkinter.ttk as ttk
import datetime

class BatteryPercent:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Battery Level")
        self.root.geometry("400x150")

        self.progressbar = ttk.Progressbar(
            self.root, orient="horizontal", length=350, mode="determinate", maximum=100
        )
        self.progressbar.pack(pady=10)

        self.percent_label = tk.Label(
            self.root, text="", font=("Helvetica", 14))
        self.percent_label.pack(pady=5)

        self.user_label = tk.Label(
            self.root, text=f"User: {getpass.getuser()}", font=("Helvetica", 12))
        self.user_label.pack(pady=5)

        self.vscode_label = tk.Label(
            self.root, text="", font=("Helvetica", 12))
        self.vscode_label.pack(pady=5)

        self.update_battery_level()

        self.root.mainloop()

    def get_percent(self):
        battery = psutil.sensors_battery()
        percent = battery.percent
        return percent

    def update_battery_level(self):
        percent = self.get_percent()
        self.progressbar["value"] = percent
        self.percent_label.config(text=f"{percent}%")

        # Obtener el proceso de Visual Studio Code
        for proc in psutil.process_iter(['pid', 'name']):
            if 'Code.exe' in proc.info['name']:
                vs_process = psutil.Process(proc.info['pid'])
                break
        else:
            vs_process = None

        # Mostrar el tiempo de ejecución de Visual Studio Code
        if vs_process:
            start_time = vs_process.create_time()
            elapsed_time = datetime.datetime.now() - datetime.datetime.fromtimestamp(start_time)
            self.vscode_label.config(text=f"VS Code runtime: {elapsed_time.total_seconds()//3600}h {elapsed_time.total_seconds()//60%60}m")
        else:
            self.vscode_label.config(text="VS Code is not running")

        self.root.after(1000, self.update_battery_level)

if __name__ == "__main__":
    app = BatteryPercent()
