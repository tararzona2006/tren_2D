from tkinter import *
# ---------------------
#--variables globales--
#----------------------
BASE = 460
ALTURA = 400

#---------------------
#--ventana principal--
#---------------------
ventana_principal = Tk()
ventana_principal.title("graficas 2D")
ventana_principal.resizable(False,False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg= "white")

#------------------------
#--frame de graficacion--
#------------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg= "green", width=480,height=450)
frame_graficacion.place(x=10,y=10)

#creacion canvas
c = Canvas(frame_graficacion, width=BASE,height=ALTURA)
c.config(bg="white")
c.place(x=10,y=10)
# dibujar rectangulos
circ_1 = c.create_oval(BASE/2-185,ALTURA/2+10,BASE/2-110,ALTURA-100, fill ="black")
rect_1 = c. create_rectangle(BASE/2-115,ALTURA-75,BASE-30,ALTURA/2,fill="light grey")



#dibujar circulos
circ_1 = c.create_oval(BASE/2-115,ALTURA/2+60,BASE/2-10,ALTURA-50, fill ="dark gray")
circ_2 = c.create_oval(BASE/2+105,ALTURA/2+60,BASE/2,ALTURA-50, fill="dark gray")
circ_3 = c.create_oval(BASE/2+110,ALTURA-50,BASE-15,ALTURA/2+60, fill="dark gray")


rect_2 = c. create_rectangle(BASE/2-40,ALTURA-90,BASE-200,ALTURA/2+90, fill="black")
rect_3 = c. create_rectangle(BASE/2+75,ALTURA-90,BASE-90,ALTURA/2+90, fill="BLACK")
rect_4 = c. create_rectangle(BASE/2,ALTURA/2-115,BASE-45,ALTURA/2, fill="dark gray")
rect_5 = c. create_rectangle(BASE/2-105,ALTURA/2-60,BASE-290,ALTURA/2, fill="dark gray")
rect_6 = c. create_rectangle(BASE/2-115,ALTURA/2-70,BASE-280,ALTURA/2-50, fill="dark gray")
rect_7 = c. create_rectangle(BASE/2-20,ALTURA/2-115,BASE-30,ALTURA/2-140, fill="black")
rect_8 = c. create_rectangle(BASE/2+30,ALTURA/2-140,BASE-70,ALTURA/2-170, fill="black")
rect_9 = c. create_rectangle(BASE/2+20,ALTURA-220,BASE-65,ALTURA/2-95,fill="light grey")
rect_10 = c. create_rectangle(BASE/2-135,ALTURA-100,BASE/2-115,ALTURA/2+15,fill="dark gray")
rect_10 = c. create_rectangle(BASE/2-155,ALTURA-75,BASE/2-130,ALTURA/2,fill="dark gray")
circ_4 = c.create_oval(BASE/2+50,ALTURA/2-20,BASE/2+130,ALTURA-295, fill="yellow")
circ_5 = c.create_oval(BASE/2+100,ALTURA/2-60,BASE/2+120,ALTURA-280, fill="white")
circ_5 = c.create_oval(BASE/2+60,ALTURA/2-60,BASE/2+80,ALTURA-280, fill="white")
linea_1 = c. create_line(BASE/2+80,ALTURA/2-40,BASE/2+100,ALTURA-240, fill="black",width=2)
nombre_1 = c. create_text(BASE/2,ALTURA/1.8,anchor="center",text="tarazona",font=("arial",25, "bold"),fill="blue",activefill="yellow")

# desplegar ventana
ventana_principal.mainloop()
