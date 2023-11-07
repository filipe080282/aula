import tkinter as tk
from tkinter import ttk

import sys

sys.path.append("utils/treeviewAbs.py")
from utils.treeviewAbs import treeAbsClass



root = tk.Tk()
root.title("meu treeview")

tre_view = treeAbsClass(root)

tre_view.insert_item(("Filipe bernardes", "filipe080282@gmail.com"))
tre_view.insert_item(("aline bernardes", "alibernardes2909@gmail.com"))



root.mainloop()
