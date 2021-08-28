# Calculadora con interfaz gráfica de usuario en Python con la librería Tkinter
# Importamos todos los módulos necesarios  
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import math


# declaramos una variable global en la cual se almacenará la operación a realizar
# en forma de cadena de texto
expression = ""


# Creamos una función la cual será llamada al momento de pulsar un botón
# como argumento recibirá el caracter que se impuso al pulsar el botón
def number_pressed(num):
    global expression
    
    # el argumento lo convertimos en un string y lo sumamos a la variable global
    # e imprimimos la variable 'expression' en nuestro widget 'Entry' de la pantalla inferior
    expression += str(num)
    printed_number.set(expression)


# Creamos una función 'equal_press'
# la cual será llamada al momento de pulsar el botón de igual 
def equal_press():
    # Asignamos una excepción 
    # para avisarnos si existe un error
    # como el error al dividir entre cero o errores de sintaxis
    try:
 
        global expression
 
        # con la función 'eval()' evaluamos el string de la variable 'expression'
        # convirtiendo la variable al tipo 'float', luego al tipo entero de forma explícita
        # pero con 'str' lo pasamos al tipo cadena de texto
        total = str(eval(expression))
        # imprimimos el resultado en el widget 'Entry' de la pantalla superior
        printed_result.set(total)
 
        # y la variable global la igualamos a cadena vacía
        expression = ""
 
    # Si todo lo que se encuentra en el 'try' no se ejecuta
    # pasa a mostrarnos el 'except'
    # e imprime el mensaje de error
    except:
 
        printed_result.set(" error!!! ")
        expression = ""


# La función 'clear' será llamada cuando pulsamos el botón 'C'
# nos borrará lo que se encuentre tanto en la pantalla superior como inferior
def clear():
    global expression
    expression = ""
    printed_number.set("")
    printed_result.set("")


# Las últimas funciones son de ventanas desplegables con información 
def aditional_info():
    messagebox.showinfo('Calculadora', 'Calculadora versión 1.0.0\nAño 2021\nProgramada en Python 3.9.5')


def leave():
    yesornot = messagebox.askokcancel('Salir', '¿Deseas salir de la aplicación "Calculadora"?')
    if yesornot == True:
        root.destroy()


# código principal
if __name__ == "__main__":
    # creación de interfaz gráfica
    # creación de la raíz
    root = Tk()
    # agregamos un título a nuestra interfaz gráfica
    root.title("CALCULADORA")
    # agregamos una imagen .ico
    root.iconbitmap('calculator.ico')
    root.resizable(False, False)
    # configuramos una variable para darle características a nuestros botones
    # la cual vamos a utilizar más adelante en los widgets de tipo 'Button'
    all_font = Font(family='Roboto Cn', size=9)


    # creación del frame el cual será el cuerpo de nuestra GUI
    body = Frame(root)
    # damos características al frame como el alto, ancho, color de fondo,
    # tamaño de borde, tipo de borde y cursor. 
    body.config(width='380', height='486', bg="#8000FF", bd=20, relief='ridge', cursor='hand2')
    # expandimos el tamaño de nuestro frame al tamaño de la raíz
    body.pack(fill='both', expand='True')


    # creamos menús desplegables directamente en la raíz
    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    about = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Ayuda', menu=about)
    about.add_command(label='Acerca de...', command=aditional_info)

    app_file = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Bye!', menu=app_file)
    app_file.add_command(label='Salir', command=leave)


    # asignamos variables de control 'StringVar' que están asociadas a los widgets 'Entry'
    # al momento que las variables de control reciban valores los widgets 'Entry' los mostrarán
    printed_number = StringVar()
    printed_result = StringVar() 
    # creación de la caja de texto la cual nos muestra los valores en pantalla
    text_box_down = Entry(body, textvariable=printed_number)
    text_box_up = Entry(body, textvariable=printed_result)
    # con el método grid le damos posicionamiento a nuestro widget "caja de texto"
    text_box_down.grid(column=0, row=1, columnspan=4, pady=3)
    text_box_up.grid(column=0, row=0, columnspan=4, pady=3)
    # le brindamos características a nuestro widget
    # (borde, color de fondo, color de texto, justificación, tipo y tamaño de letra)
    text_box_down.config(bd=5, bg="black", fg="#01FD01", justify="right", font=('Comic Sans MS', 16))
    text_box_up.config(bd=5, bg="black", fg="#01FD01", justify="right", font=('Comic Sans MS', 16))


    # fila 1 de botones
    par_button = Button(body, text='(', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:number_pressed('('))
    par_button.grid(row=2, column=0, pady=7, padx=5)
    par2_button = Button(body, text=')', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:number_pressed(')'))
    par2_button.grid(row=2, column=1, padx=4)
    pi_button = Button(body, text='π', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:number_pressed(math.pi))
    pi_button.grid(row=2, column=2, padx=5)
    clear_button = Button(body, text='C', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:clear())
    clear_button.grid(row=2, column=3, padx=4)


    # fila 2 de botones
    button7 = Button(body, text='7', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:number_pressed(7))
    button7.grid(row=3, column=0)
    button8 = Button(body, text='8', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:number_pressed(8))
    button8.grid(row=3, column=1, padx=4)
    button9 = Button(body, text='9', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:number_pressed(9))
    button9.grid(row=3, column=2)
    divide_button = Button(body, text='÷', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:number_pressed('/'))
    divide_button.grid(row=3, column=3, padx=4)


    # fila 3 de botones
    button4 = Button(body, text='4', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:number_pressed(4))
    button4.grid(row=4, column=0, pady=7)
    button5 = Button(body, text='5', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:number_pressed(5))
    button5.grid(row=4, column=1, padx=4)
    button6 = Button(body, text='6', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:number_pressed(6))
    button6.grid(row=4, column=2)
    multiply_button = Button(body, text='X', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:number_pressed('*'))
    multiply_button.grid(row=4, column=3, padx=4)


    # fila 4 de botones
    button1 = Button(body, text='1', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:number_pressed(1))
    button1.grid(row=5, column=0)
    button2 = Button(body, text='2', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:number_pressed(2))
    button2.grid(row=5, column=1, padx=4)
    button3 = Button(body, text='3', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:number_pressed(3))
    button3.grid(row=5, column=2)
    subtract_button = Button(body, text='-', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:number_pressed('-'))
    subtract_button.grid(row=5, column=3, padx=4)


    # fila 5 de botones
    point_button = Button(body, text=',', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:number_pressed('.'))
    point_button.grid(row=6, column=0, pady=7)
    button0 = Button(body, text='0', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:number_pressed('0'))
    button0.grid(row=6, column=1, padx=4)
    equal_button = Button(body, text='=', height=2, width=7, bd=5, relief='ridge', font=all_font, command=equal_press)
    equal_button.grid(row=6, column=2)
    plus_button = Button(body, text='+', height=2, width=7, bd=5, relief='ridge', font=all_font, command=lambda:number_pressed('+'))
    plus_button.grid(row=6, column=3, padx=4)


    # esta instrucción mantiene ejecutada en pantalla nuestra GUI
    # algo así como un bucle infinito
    root.mainloop()

