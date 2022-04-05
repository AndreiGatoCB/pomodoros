from tkinter import *
import math


# -------------------------- CONSTANTES -------------------------- #
ROSA = "#e2979c"
ROJO = "#e7305b"
VERDE = "#9bdeac"
AMARILLO = "#f7f5dd"
FUENTE = "Courier"
MINUTOS_TRABAJO = 25
MIN_BREAK_CORTO = 5
MIN_BREAK_LARGO = 20
reps = 0
timer = None


# -------------------------- RESETEO DE TEMPORIZADOR -------------------------- #
def reseteo():
    ventana.after_cancel(timer)
    canvas.itemconfig(texto_temporizador_1, text="00:00")
    canvas.itemconfig(texto_temporizador_2, text="00:00")
    temporizador_label.config(text="Temporizador", fg=VERDE)
    check_label.config(text="")
    global reps
    reps = 0


# -------------------------- MECANISMO DE TEMPORIZADOR -------------------------- #
def iniciar():
    global reps

    trabajo_seg = MINUTOS_TRABAJO * 60
    descanso_corto = MIN_BREAK_CORTO * 60
    descanso_largo = MIN_BREAK_LARGO * 60

    reps += 1

    if reps % 8 == 0:
        cuenta_atras(descanso_largo)
        temporizador_label.config(text="Descanso", fg=ROJO)
    elif reps % 2 == 0:
        cuenta_atras(descanso_corto)
        temporizador_label.config(text="Descanso", fg=ROSA)
    else:
        cuenta_atras(trabajo_seg)
        temporizador_label.config(text="Trabajo", fg=VERDE)


# -------------------------- MECANISMO DE CUENTA ATRÁS -------------------------- #
def cuenta_atras(conteo):

    cuenta_min = math.floor(conteo / 60)
    cuenta_seg = conteo % 60
    if cuenta_seg <= 9:
        cuenta_seg = f"0{cuenta_seg}"

    canvas.itemconfig(texto_temporizador_1, text=f"{cuenta_min}:{cuenta_seg}")
    canvas.itemconfig(texto_temporizador_2, text=f"{cuenta_min}:{cuenta_seg}")
    if conteo > 0:
        global timer
        timer = ventana.after(1000, cuenta_atras, conteo - 1)
    else:
        iniciar()
        marcas = ""
        sesiones = math.floor(reps/2)
        for _ in range(sesiones):
            marcas += "✔"
        if sesiones % 4 == 0:
            check_label.config(text=marcas, fg=ROJO)
        else:
            check_label.config(text=marcas, fg=VERDE)


# -------------------------- UI SETUP -------------------------- #
ventana = Tk()
ventana.title("¡POMODORO!")
ventana.config(padx=20, pady=20, bg=AMARILLO)

temporizador_label = Label(text="Temporizador", font=(FUENTE, 30, "bold"), fg=VERDE, bg=AMARILLO)
temporizador_label.grid(column=1, row=0)

canvas = Canvas(width=286, height=288, bg=AMARILLO, highlightthickness=0)
tomate_img = PhotoImage(file="pomodoros.png")
canvas.create_image(143, 144, image=tomate_img)
texto_temporizador_1 = canvas.create_text(150, 144, text="00:00", fill="black", font=(FUENTE, 35, "bold"))
texto_temporizador_2 = canvas.create_text(150, 144, text="00:00", fill="white", font=(FUENTE, 35))
canvas.grid(column=1, row=1)

check_label = Label(font=(FUENTE, 20, "bold"), fg=VERDE, bg=AMARILLO)
check_label.grid(column=1, row=3)

boton = Button(text="Inicio", command=iniciar, highlightthickness=0)
boton.grid(column=0, row=2)

boton = Button(text="Restaurar", command=reseteo, highlightthickness=0)
boton.grid(column=2, row=2)

ventana.mainloop()
