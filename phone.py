import tkinter as tk
from PIL import Image, ImageTk
import random
import pyfiglet

def generar_numeros():
    codigo_pais = codigo_pais_entry.get()
    lada = lada_entry.get()
    cantidad = int(cantidad_entry.get())
    
    numeros_generados = []
    for _ in range(cantidad):
        numero = f"{codigo_pais} {lada} {''.join(random.choices('0123456789', k=8))}"
        numero = numero[:-1]  # Eliminar el último dígito
        numeros_generados.append(numero)
    
    resultados_text.delete('1.0', tk.END)
    resultados_text.insert(tk.END, '\n'.join(numeros_generados))

def guardar_numeros():
    # Crear el arte ASCII con pyfiglet
    custom_figlet = pyfiglet.Figlet(font='block')
    ascii_text = custom_figlet.renderText("4Z3S1N0")
    
    numeros_generados = resultados_text.get("1.0", tk.END)
    
    with open("numeros_generados.txt", "w") as archivo:
        archivo.write(ascii_text)
        archivo.write("\n\n")  # Agregar una línea en blanco
        archivo.write(numeros_generados)

ventana = tk.Tk()
ventana.title("Generador de Números de Teléfono")

# Cargar el favicon
favicon = Image.open("favicon.PNG")
photo = ImageTk.PhotoImage(favicon)
ventana.tk.call('wm', 'iconphoto', ventana._w, photo)

# Estilo personalizado en modo oscuro
ventana.geometry("400x350")
ventana.configure(bg='#1E1E1E')
ventana.option_add('*TButton*highlightBackground', '#1E1E1E')
ventana.option_add('*TButton*highlightColor', '#1E1E1E')
ventana.option_add('*TButton*background', '#007BFF')
ventana.option_add('*TButton*foreground', 'white')
ventana.option_add('*TLabel*background', '#1E1E1E')
ventana.option_add('*TLabel*foreground', 'white')
ventana.option_add('*TEntry*background', '#333333')
ventana.option_add('*TEntry*foreground', 'white')

# Crear etiquetas y entradas
cantidad_label = tk.Label(ventana, text="Cantidad de números a generar:", bg='#1E1E1E', fg='white')
cantidad_label.pack()

cantidad_entry = tk.Entry(ventana)
cantidad_entry.pack()

codigo_pais_label = tk.Label(ventana, text="Código de País:", bg='#1E1E1E', fg='white')
codigo_pais_label.pack()

codigo_pais_entry = tk.Entry(ventana)
codigo_pais_entry.pack()

lada_label = tk.Label(ventana, text="Lada:", bg='#1E1E1E', fg='white')
lada_label.pack()

lada_entry = tk.Entry(ventana)
lada_entry.pack()

generar_button = tk.Button(ventana, text="Generar Números", command=generar_numeros)
generar_button.pack()

# Crear un área de texto para mostrar los resultados
resultados_text = tk.Text(ventana, height=10, width=40, bg='#333333', fg='white')
resultados_text.pack()

guardar_button = tk.Button(ventana, text="Guardar Números y Arte ASCII", command=guardar_numeros)
guardar_button.pack()

ventana.mainloop()
