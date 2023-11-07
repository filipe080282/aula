import tkinter as tk
from tkinter import ttk

class treeAbsClass:
    def __init__(self, parent):
        self.tree = ttk.Treeview(parent, columns=("Column 1", "Column 2"), show="headings")
        self.tree.heading("Column 1", text="Nome", anchor="w")
        self.tree.heading("Column 2", text="E-mail", anchor="w")
        self.tree.pack()

        # Associar um evento de clique ao TreeView
        self.tree.bind("<ButtonRelease-1>", self.on_treeview_click)

    def insert_item(self, values):
        self.tree.insert("", "end", values=values)

    def delete_item(self, item):
        self.tree.delete(item)

    def on_treeview_click(self, event):
        item = self.tree.selection()
        if item:
            selected_item = self.tree.item(item)
            values = selected_item['values']
            print("Item selecionado:", values)

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("TreeView Wrapper Example")
    
#     tree_view = treeAbsClass(root)

#     # Exemplo de uso:
#     tree_view.insert_item(("Item 1", "Value 1"))
#     tree_view.insert_item(("Item 2", "Value 2"))

#     selected_item = tree_view.get_selected_item()
#     if selected_item:
#         print("Item selecionado:", selected_item)

#     root.mainloop()





