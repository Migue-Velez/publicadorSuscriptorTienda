import tkinter as tk
from publisher import publishMessage

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Publisher')
        self.root.geometry("350x250")
        self.root.resizable(False, False)

        self.frame = tk.Frame(root)
        self.frame.pack(pady = 20)

        tk.Label(self.frame, text = "Nombre del artículo:").grid(row = 0, column = 0, padx = 10, pady = 5)
        self.entryArticle = tk.Entry(self.frame)
        self.entryArticle.grid(row = 0, column = 1, padx = 10, pady = 5)
        
        tk.Label(self.frame, text = "Cantidad del artículo:").grid(row = 1, column = 0, padx = 10, pady = 5)
        self.entryQuantity = tk.Entry(self.frame)
        self.entryQuantity.grid(row = 1, column = 1, padx = 10, pady = 5)

        tk.Label(self.frame, text = "Precio del artículo:").grid(row = 2, column = 0, padx = 10, pady = 5)
        self.entryPrice = tk.Entry(self.frame)
        self.entryPrice.grid(row = 2, column = 1, padx = 10, pady = 5)

        self.btnPublishsed = tk.Button(root, text = "Publicar", command = self.getValues)
        self.btnPublishsed.pack(pady = 10)

        self.labelMessage = tk.Label(root, text = "",highlightthickness = 1 , highlightbackground = "#5c6983")
        self.labelMessage.pack(pady = 10)
                                         
    def getValues(self):
        articleName = self.entryArticle.get()
        quantity = self.entryQuantity.get()
        price = self.entryPrice.get()
        message = articleName + ";" + quantity + ";" + price
        try:
            publishMessage(message)
            self.labelMessage.config(text = "Mensaje enviado")

        except Exception as e:
            self.labelMessage.config(text = f"Ha sucedido un error")
            print(e)

if __name__ == '__main__':
    root = tk.Tk()
    window = GUI(root)
    root.mainloop()