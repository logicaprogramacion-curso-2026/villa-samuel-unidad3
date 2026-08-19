# main.py

import tkinter as tk

from interfaz import MiniTiendaApp


def main():

    ventana = tk.Tk()

    MiniTiendaApp(ventana)

    ventana.mainloop()


if __name__ == "__main__":
    main()