import tkinter as tk
import subprocess


def grab_IP():
    command = "ifconfig | grep 'inet '| grep -v 127.0.0.1 | awk 'NR==1{print $2}'"
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            label.config(text=f"Public IP:\n{stdout.strip()}")
            button.config(text="HIDE", command=reset_label)
        else:
            label.config(text=f"ERROR: {stderr.strip()}")
    except Exception as e:
        label.config(text=f"Exception: {str(e)}")


def reset_label():
    label.config(text="Public IP:\nxxx.xxx.xxx.xxx")
    button.config(text="SHOW", command=grab_IP)


root = tk.Tk()
root.title("Show My IP")
root.geometry("200x125")


root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)


label = tk.Label(root, text="Public IP:\nxxx.xxx.xxx.xxx", wraplength=380, justify="center", font=('Arial',14))
label.grid(row=0, column=0, padx=10, pady=5, sticky="ns")


button = tk.Button(root, text='SHOW', command=grab_IP)
button.grid(row=1, column=0, padx=10, pady=20, sticky="ns")

root.mainloop()