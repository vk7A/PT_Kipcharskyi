import tkinter as tk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Funkcia na generovanie a spracovanie čísiel
def generate_numbers():
    # Generovanie 18 náhodných čísel
    numbers = [random.randint(-100, 100) for _ in range(18)]
    updated_numbers = [num + 10 for num in numbers]
    negative_numbers = [num for num in updated_numbers if num < 0]

    # Aktualizácia textu so zoznamom čísel
    result_text.set(f"Pôvodné čísla: {numbers}\n\nUpravené čísla: {updated_numbers}\n\nZáporné čísla: {negative_numbers}")

    # Vyčistenie predchádzajúceho grafu, ak existuje
    for widget in graph_frame.winfo_children():
        widget.destroy()

    # Vytvorenie nového grafu
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(range(len(updated_numbers)), updated_numbers, marker="o", color="#4CAF50", label="Hodnoty +10")
    ax.axhline(0, color="#FF5722", linestyle="--", label="Nula")
    ax.set_title("Graf hodnôt", fontsize=14, color="#333")
    ax.set_xlabel("Index", fontsize=12)
    ax.set_ylabel("Hodnota", fontsize=12)
    ax.legend()

    # Vloženie grafu do GUI
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# GUI aplikácia
window = tk.Tk()
window.title("Moderný Generátor Čísel")
window.geometry("900x700")
window.configure(bg="#F3F4F6")

# Základný popis
header_frame = tk.Frame(window, bg="#2D2F36", pady=10)
header_frame.pack(fill=tk.X)
header_label = tk.Label(
    header_frame, text="Programovacie techniky\nVladyslav Kipcharskyi\nZadanie: Generátor čísel",
    font=("Arial", 16, "bold"), fg="#FFFFFF", bg="#2D2F36", justify="center"
)
header_label.pack()

# Sekcia na tlačidlo
button_frame = tk.Frame(window, bg="#F3F4F6", pady=10)

button_frame.pack()
generate_button = tk.Button(
    button_frame, text="Vygenerovať čísla", command=generate_numbers,
    font=("Arial", 14), bg="#4CAF50", fg="white", relief="flat", padx=20, pady=10
)
generate_button.pack()

# Výstupný text
result_text = tk.StringVar()
result_label = tk.Label(
    window, textvariable=result_text, font=("Arial", 12), bg="#F3F4F6", fg="#333",
    justify="left", wraplength=850
)
result_label.pack(pady=20)

# Sekcia na graf
graph_frame = tk.Frame(window, bg="#F3F4F6", relief="sunken", bd=2)
graph_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Spustenie aplikácie
window.mainloop()
