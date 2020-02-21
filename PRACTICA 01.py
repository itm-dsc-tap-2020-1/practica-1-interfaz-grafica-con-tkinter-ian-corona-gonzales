import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mbox

################################  METODOS  ##########################################################################################
ventana=tk.Tk()
caja=scrolledtext.ScrolledText(ventana, width=50, height=5, wrap=tk.WORD)

def reg():
    if nombre.get()!="" and ap.get()!="" and am.get()!="" and dire.get()!="" and col.get()!="" and mun.get()!="":
        v2=tk.Tk()
        v2.title("Sistema Escolar")
        imp=ttk.LabelFrame(v2, text='Datos Personales')
        imp.pack(expand=1,fill='both')
        ttk.Label(imp, text="Nombre Completo: \n"+nombre.get()+" "+ap.get()+" "+am.get()+"\n").grid(column=0, row=0, sticky=tk.W)
        ttk.Label(imp, text="Dirección: \n"+dire.get()+" "+col.get()+". "+cd.get()+", "+mun.get()).grid(column=0, row=1, sticky=tk.W)
        imp.grid(column=0, row=0, padx=10, pady=10)
        v2.mainloop() 
    else:
        mbox.showerror('Datos Incompletos', 'Faltan campos por llenar')
       
def datos():
    if caja.get("1.0", "end-1c")=="":
        mbox.showerror('Datos Incompletos', 'Llene el campo "Objetivo de la vida"')
    else:
        v3=tk.Tk()
        v3.title("Sistema Escolar")
        v3.resizable(0,0)
        imp=ttk.LabelFrame(v3, text='Datos Extras')
        f1=ttk.LabelFrame(imp)
        f2=ttk.LabelFrame(imp)
        f3=ttk.LabelFrame(imp)
        imp.grid(column=0, row=0, padx=10, pady=10,sticky=tk.W)
        r=2
        rb.get()
        est=["Union Libre","Soltero", "Viudo", "Casado", "Divorciado"]
        TG=ttk.Label(f1, text="Te Gusta:")
        g1=ttk.Label(f1, text="Escuchar Musica")
        g2=ttk.Label(f1, text="Bailar")
        g3=ttk.Label(f1, text="Jugar")
        g4=ttk.Label(f1, text="Leer")
        g5=ttk.Label(f1, text="Correr")
        Es=ttk.Label(f2, text="Estado:")
        selec=0
        
        if "selected" in c1.state():
            selec=1
            g1.grid(column=0, row=r, padx=10, pady=5,sticky=tk.W)
            r+=1
        if "selected" in c2.state():
            selec=1
            g2.grid(column=0, row=r, padx=10, pady=5,sticky=tk.W)
            r+=1
        if "selected" in c3.state():
            selec=1
            g3.grid(column=0, row=r, padx=10, pady=5,sticky=tk.W)
            r+=1
        if "selected" in c4.state():
            selec=1
            g4.grid(column=0, row=r, padx=10, pady=5,sticky=tk.W)
            r+=1
        if "selected" in c5.state():
            selec=1
            g5.grid(column=0, row=r, padx=10, pady=5,sticky=tk.W)
            r+=1
        r+=1
        if selec==0:
            TG.configure(text="No tienes pasatiempos")
        TG.grid(column=0, row=0, padx=10, pady=10,sticky=tk.W)
        f1.grid(column=0, row=0, padx=10, pady=10,sticky=tk.W, columnspan=2)
        ttk.Label(imp).grid(column=1, row=0)
        Es.grid(column=0, row=0, padx=10, pady=10,sticky=tk.W)
        r+=1

        g6=ttk.Label(f2, text=est[rb.get()])
        g6.grid(column=0,row=1, padx=10, pady=5,sticky=tk.W)
        f2.grid(column=0, row=1, padx=10, pady=10,sticky=tk.W,columnspan=2)

        
        ttk.Label(f3, text="Objetivo de la Vida:").grid(column=0, row=r, padx=10, pady=10,sticky=tk.W)
        ttk.Label(f3, text=caja.get("1.0", "end-1c")).grid(column=0, row=r+1, padx=10, pady=10,sticky=tk.W)
        f3.grid(column=0, row=2, padx=10, pady=10,sticky=tk.W, columnspan=2)
        
        v3.mainloop()   

def imprime():
    if nombre.get()!="" and ap.get()!="" and am.get()!="" and dire.get()!="" and col.get()!="" and mun.get()!="" and caja.get("1.0", "end-1c")!="":
        v2=tk.Tk()
        v2.title("Sistema Escolar")
        imp=ttk.LabelFrame(v2, text='Datos Personales')
        imp.pack(expand=1,fill='both')
        ttk.Label(imp, text="Nombre Completo: \n"+nombre.get()+" "+ap.get()+" "+am.get()+"\n").grid(column=0, row=0, sticky=tk.W)
        ttk.Label(imp, text="Dirección: \n"+dire.get()+" "+col.get()+". "+cd.get()+", "+mun.get()).grid(column=0, row=1, sticky=tk.W)
        
        imp.grid(column=0, row=0, padx=10, pady=10)
        imp=ttk.LabelFrame(v2, text='Datos Extras')
        f1=ttk.LabelFrame(imp)
        f2=ttk.LabelFrame(imp)
        f3=ttk.LabelFrame(imp)
        imp.grid(column=0, row=1, padx=10, pady=10,sticky=tk.W)
        r=2
        rb.get()
        est=["Union Libre","Soltero", "Viudo", "Casado", "Divorciado"]
        TG=ttk.Label(f1, text="Te Gusta:")
        g1=ttk.Label(f1, text="Escuchar Musica")
        g2=ttk.Label(f1, text="Bailar")
        g3=ttk.Label(f1, text="Jugar")
        g4=ttk.Label(f1, text="Leer")
        g5=ttk.Label(f1, text="Correr")
        Es=ttk.Label(f2, text="Estado:")
        selec=0
        
        if "selected" in c1.state():
            selec=1
            g1.grid(column=0, row=r, padx=10, pady=5,sticky=tk.W)
            r+=1
        if "selected" in c2.state():
            selec=1
            g2.grid(column=0, row=r, padx=10, pady=5,sticky=tk.W)
            r+=1
        if "selected" in c3.state():
            selec=1
            g3.grid(column=0, row=r, padx=10, pady=5,sticky=tk.W)
            r+=1
        if "selected" in c4.state():
            selec=1
            g4.grid(column=0, row=r, padx=10, pady=5,sticky=tk.W)
            r+=1
        if "selected" in c5.state():
            selec=1
            g5.grid(column=0, row=r, padx=10, pady=5,sticky=tk.W)
            r+=1
        r+=1
        if selec==0:
            TG.configure(text="No tienes pasatiempos")
        TG.grid(column=0, row=0, padx=10, pady=10,sticky=tk.W)
        f1.grid(column=0, row=0, padx=10, pady=10,sticky=tk.W, columnspan=2)
        ttk.Label(imp).grid(column=1, row=0)
        Es.grid(column=0, row=0, padx=10, pady=10,sticky=tk.W)
        r+=1

        g6=ttk.Label(f2, text=est[rb.get()])
        g6.grid(column=0,row=1, padx=10, pady=5,sticky=tk.W)
        f2.grid(column=0, row=1, padx=10, pady=10,sticky=tk.W,columnspan=2)

        
        ttk.Label(f3, text="Objetivo de la Vida:").grid(column=0, row=r, padx=10, pady=10,sticky=tk.W)
        ttk.Label(f3, text=caja.get("1.0", "end-1c")).grid(column=0, row=r+1, padx=10, pady=10,sticky=tk.W)
        f3.grid(column=0, row=2, padx=10, pady=10,sticky=tk.W, columnspan=2)
        v2.mainloop() 
    else:
        mbox.showerror('Datos Incompletos', 'Faltan campos por llenar')    

def salir():
    ventana.quit()
    ventana.destroy()
    exit()


ventana.title("Sistema Escolar - Menu")

################################  MENU ###################################################################################################

barram=Menu(ventana)
ventana.config(menu=barram)
sis=Menu(barram)
hp=Menu(barram)
sis.add_command(label="Imprimir", command=imprime)
sis.add_separator()
sis.add_command(label="Salir", command=salir)
hp.add_command(label="Acerca de")
barram.add_cascade(label="Sistema", menu=sis)
barram.add_cascade(label="Ayuda", menu=hp)

#ventana.geometry('510x580')
ventana.resizable(0, 0)

############################ PESTAÑAS ####################################################################################################

tabc=ttk.Notebook(ventana)
tabpers=ttk.Frame(tabc)
tabex=ttk.Frame(tabc)
tabc.add(tabpers, text='Datos Personales')
tabc.add(tabex, text='Datos Extra')
tabc.pack(expand=1, fill="both")

############################## DATOS PERSONALES  #########################################################################################

labnom=ttk.Label(tabpers, text="Nombre: ").grid(column=0, row=2, padx=5, pady=5)
labap=ttk.Label(tabpers, text="Apellido Paterno: ").grid(column=0, row=3, padx=5, pady=5)
lapam=ttk.Label(tabpers, text="Apellido Materno: ").grid(column=0, row=4, padx=5, pady=5)
labdir=ttk.Label(tabpers, text="Direccion: ").grid(column=0, row=5, padx=5, pady=5)
labcol=ttk.Label(tabpers, text="Colonia: ").grid(column=0, row=6, padx=5, pady=5)
labcd=ttk.Label(tabpers, text="Ciudad: ").grid(column=0, row=7, padx=5, pady=5)
labmun=ttk.Label(tabpers, text="Municipio: ").grid(column=0, row=8, padx=5, pady=5)

nombre = tk.StringVar()
ap = tk.StringVar()
am = tk.StringVar()
dire = tk.StringVar()
col = tk.StringVar()
cd = tk.StringVar()
mun = tk.StringVar()

nombrec = ttk.Entry(tabpers, width=28, textvariable=nombre).grid(column = 1, row = 2, padx=5, pady=5)
apc = ttk.Entry(tabpers, width=28, textvariable=ap).grid(column = 1, row = 3, padx=5, pady=5)
amc = ttk.Entry(tabpers, width=28, textvariable=am).grid(column = 1, row = 4, padx=5, pady=5)
direc = ttk.Entry(tabpers, width=28, textvariable=dire).grid(column = 1, row = 5, padx=5, pady=5)

colc= ttk.Combobox(tabpers, width=18, textvariable=col)
colc['values']=("Industrial", "Isaac Arriaga", "Los llanitos")
colc.grid(column = 1, row = 6, padx=5, pady=5)



cdc= ttk.Combobox(tabpers, width=18, textvariable=cd)
cdc['values']=("Morelia", "Lazaro Cardenas", "Uruapan")
cdc.grid(column = 1, row = 7, padx=5, pady=5)


munc= ttk.Combobox(tabpers, width=18, textvariable=mun)
munc['values']=("Morelia", "Lazaro Cardenas", "Uruapan")
munc.grid(column = 1, row = 8, padx=5, pady=5)

registrar = ttk.Button(tabpers, text="Imprimir Datos", command=reg)
registrar.grid(column=3, row=10, sticky=tk.E, padx=20, pady=15)

########################## DATOS EXTRA #####################################################################################################

opc1=tk.IntVar()
opc2=tk.IntVar()
opc3=tk.IntVar()
opc4=tk.IntVar()
opc5=tk.IntVar()

cont_pas=ttk.LabelFrame(tabex, text='Pasatiempos')

c1=ttk.Checkbutton(cont_pas, text="Escuchar Musica", variable=opc1)
c2=ttk.Checkbutton(cont_pas, text="Bailar", variable=opc2)
c3=ttk.Checkbutton(cont_pas, text="Jugar", variable=opc3)
c4=ttk.Checkbutton(cont_pas, text="Leer", variable=opc4)
c5=ttk.Checkbutton(cont_pas, text="Correr", variable=opc5)

c1.grid(column = 0, row = 10, padx=10, pady=10)
c2.grid(column = 1, row = 10, padx=10, pady=10)
c3.grid(column = 2, row = 10, padx=10, pady=10)
c4.grid(column = 3, row = 10, padx=10, pady=10)
c5.grid(column = 4, row = 10, padx=10, pady=10)

cont_pas.grid(column=0, row=1, padx=10, pady=10)


cont_est=ttk.LabelFrame(tabex, text='Estado Civil')
rb=tk.IntVar()
r5=ttk.Radiobutton(cont_est, text="Union Libre", variable=rb, value=0)
r1=ttk.Radiobutton(cont_est, text="Soltero", variable=rb, value=1)
r2=ttk.Radiobutton(cont_est, text="Viudo", variable=rb, value=2)
r3=ttk.Radiobutton(cont_est, text="Casado", variable=rb, value=3)
r4=ttk.Radiobutton(cont_est, text="Divorciado", variable=rb, value=4)

r1.grid(column=0,row=12, sticky=tk.W, padx=10, pady=10)
r2.grid(column=1,row=12, sticky=tk.W, padx=10, pady=10)
r3.grid(column=2,row=12, sticky=tk.W, padx=10, pady=10)
r4.grid(column=3,row=12, sticky=tk.W, padx=10, pady=10)
r5.grid(column=4,row=12, sticky=tk.W, padx=10, pady=10)

cont_est.grid(column=0, row=2, padx=10, pady=10)

cont_obj=ttk.LabelFrame(tabex, text='Objetivo de la vida')
caja=scrolledtext.ScrolledText(cont_obj, width=50, height=5, wrap=tk.WORD)
caja.grid(column=0, row=0,padx=10, pady=10)
cont_obj.grid(column=0, row=3, padx=10, pady=10)

imprimir = ttk.Button(tabex, text="Imprimir Datos", command=datos)

imprimir.grid(column=0, row=5, sticky=tk.E, padx=20, pady=5)

##########################################################################################################################################
ventana.mainloop()
