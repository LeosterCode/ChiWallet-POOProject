#---------------LIBRERIAS-----------------------#
import tkinter as tk 
from tkinter import messagebox, simpledialog, Text, Scrollbar
import sqlite3
from tkcalendar import DateEntry
from PIL import Image, ImageTk 
import time
from datetime import datetime, time
#---------------FONTS---------------------------#
font_title = ("Noisy Walk", 18)
font_balance = ("Open Sans", 20, "bold")
font_buttons = ("Open Sans",9, "bold")
font_basic = ("Open Sans",9, "bold")
font_moves = ("Open Sans",10, "bold")




class ChiWallet:
#-------------------------METODO CONSTRUCTOR E INTERFAZ DE INICIO DE SESION--------------------------------
    def __init__(self, root):
     
        self.root = root
        self.root.title("ChiWallet")
        self.root.geometry("280x350")
        self.root.config(bg="#003785") #8aeae5
        self.root.iconbitmap(default="C:\\Users\\soter\\OneDrive\\Universidad\\2DO CUATRIMESTRE\\POO\\ChiCoin\\Codigos y BD\\Images\\CW1.ico")
        self.root.resizable(0,0)
    
        #Variables contrasena y usuario 
          
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        
        #nterfaz inicio de sesion
        self.login_lbl = tk.Label(root,text="Bienvenido a ChiWallet!", font=font_title, bg="#003785", fg="#8aeae5")
        self.login_lbl.grid(row=1, column=2, padx=10, pady=10)
        
        self.username_lbl = tk.Label(root, text="Usuario", fg="#FFFFFF", bg="#003785", font=font_basic)
        self.username_lbl.grid(row=2, column=2, padx=10, pady=5)
        
        self.username_entry = tk.Entry(root, textvariable = self.username, bg="#c4dafa", relief="ridge", fg="#000000")
        self.username_entry.grid(row=3, column=2, padx=10, pady=5)
        
        self.password_lbl = tk.Label(root, text="Contraseña", bg="#003785", fg="#FFFFFF", font=font_basic)
        self.password_lbl.grid(row=4, column=2, padx=10, pady=5 )
        
        self.password_entry = tk.Entry(root, textvariable = self.password, bg="#c4dafa", relief="ridge", show="*")
        self.password_entry.grid(row=5, column=2, padx=10, pady=5)
        
        self.login_bttn = tk.Button(root,text="Iniciar Sesion", bg="#c4dafa", relief="groove", fg="#000000",command=self.login)
        self.login_bttn.grid(row=6, column=2, padx=10, pady=5)
        
        self.label_create_account1 = tk.Label(root,text="¿No tienes cuenta? Crea una ", fg="#FFFFFF", bg="#003785", font=font_basic)
        self.label_create_account1.grid(row=7, column=2, padx=10, pady=5) 
        
        self.btn_create_account1 = tk.Button(root, text="Crear cuenta", bg="#c4dafa", relief="groove",fg="#000000", command=self.sign_in)
        self.btn_create_account1.grid(row=8, column=2, padx=10, pady=5)    


#-------------------------METODO PARA MOSTRAR VENTANA DE CREAR CUENTA------------------------------------   
    def sign_in(self):
       
        created_user = tk.StringVar()
        created_pasword = tk.StringVar()
        created_email = tk.StringVar()
       
        self.create_account_wdw = tk.Toplevel(root)
        self.create_account_wdw.title("Crea tu Cuenta")
        self.create_account_wdw.geometry("370x320")
        self.create_account_wdw.config(bg="#003785")
        self.create_account_wdw.resizable(0,0)
        
        
        
        self.label_create_account = tk.Label(self.create_account_wdw, text="Crea tu ChiWallet Cuenta", bg="#003785",fg="#55DFD8" ,font=font_title)
        self.label_create_account.grid(row=0, column=2, padx=10, pady=10)
        
        self.create_username_lbl = tk.Label(self.create_account_wdw, text="Nombre de Usuario",fg="#FFFFFF", bg="#003785", font=font_basic)
        self.create_username_lbl.grid(row=1, column=2, padx=10, pady=5)
        
        self.create_username_entry = tk.Entry(self.create_account_wdw, textvariable=created_user,bg="#c4dafa", relief="ridge", fg="#000000")
        self.create_username_entry.grid(row=2, column=2, padx=10, pady=5)
        
        self.create_email_lbl = tk.Label(self.create_account_wdw, text="E-mail", fg="#FFFFFF", bg="#003785", font=font_basic)
        self.create_email_lbl.grid(row=3, column=2, padx=10, pady=5)
        
        self.create_email_entry = tk.Entry(self.create_account_wdw, textvariable=created_email,bg="#c4dafa", relief="ridge", fg="#000000")
        self.create_email_entry.grid(row=4, column=2, padx=10, pady=5)
        
        self.create_password_lbl = tk.Label(self.create_account_wdw,text="Crea tu contraseña:", fg="#FFFFFF", bg="#003785", font=font_basic)
        self.create_password_lbl.grid(row=5, column=2, padx=10, pady=5)
        
        self.create_password_entry = tk.Entry(self.create_account_wdw, textvariable=created_pasword,bg="#c4dafa", relief="ridge", fg="#000000", show="*")
        self.create_password_entry.grid(row=6, column=2, padx=10, pady=5)
        
        self.create_account_bttn = tk.Button(self.create_account_wdw, state="disabled", text="CREAR CUENTA", bg="#c4dafa", relief="groove", fg="#000000", font=font_buttons,command=self.create_account)
        self.create_account_bttn.grid(row=7, column=2, padx=10, pady=5)
        
        self.terms_button = tk.Button(self.create_account_wdw, text="Terminos y Condiciones",bg="#c4dafa", relief="groove", fg="#000000", font=font_buttons ,command=self.accept_terms_conditions)
        self.terms_button.grid(row=8, column=2, padx=10, pady=10)
        
        self.create_account_wdw.mainloop() 
        

#-------------------------METODO PARA ACEPTAR TERMINOS Y CONDICIONES-------------------------------------    
    def accept_terms_conditions(self):
        self.terms_wdw=tk.Toplevel(root)
        self.terms_wdw.title("Términos y Condiciones")
        self.terms_wdw.geometry("200x200")
        self.terms_wdw.resizable(False, False)
        
        self.terms_frame = tk.Frame(self.terms_wdw, width=400, height=100)
        self.terms_frame.pack(fill=tk.BOTH) #el frame se expande horizontal y verticalmente
        self.terms_frame.pack_propagate(False) 
        
        #Frame de botones
        self.button_frame =tk.Frame(self.terms_wdw, width=400, height=100)
        self.button_frame.pack()
        self.button_frame.pack_propagate(False) 
     
     
        #Scrollbar en el lado derecho de la ventana
        self.scrollbar = Scrollbar(self.terms_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        #Widget para mostrar terminos y condiciones
        self.terms_text = Text(self.terms_frame, wrap=tk.WORD, yscrollcommand=self.scrollbar.set)
        self.terms_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)    # Expande el widget para que llene la ventana
        self.scrollbar.config(command=self.terms_text.yview)  # Configura el scrollbar para controlar el desplazamiento vertical

        self.load_terms_and_conditions()
        
        self.accept_terms = tk.BooleanVar()
        self.accept_terms.set(False)  # No se han aceptado los términos(por defecto)
        
        self.accept_checkbutton = tk.Checkbutton(self.button_frame, text="Acepto los términos y condiciones", variable=self.accept_terms)
        self.accept_checkbutton.grid(row=3)
        
        self.accept_button=tk.Button(self.button_frame, text="ACEPTAR", bg="Green", command=self.check_accept)
        self.accept_button.grid(row=1, padx=10, pady=2)
        
        self.rechace_button=tk.Button(self.button_frame, text="RECHAZAR", bg="red", command=self.reject_terms)
        self.rechace_button.grid(row=2, padx=10, pady=2)


#-------------------------METODO PARA VERIFICAR SI SE ACEPTARON LOS TERMINOS Y CONDICIONES---------------------------
    def check_accept(self):
         if self.accept_terms.get():
            self.create_account_bttn.config(state=tk.NORMAL)
            self.terms_wdw.destroy()  # Cierra la ventana después de aceptar los términos            


#-------------------------METODO PARA MOSTRAR UN MSJ SI SE RECHAZAN LOS TERMINOS Y CONDICIONES---------------------
    def reject_terms(self):
        if not self.accept_terms.get():
            self.create_account_bttn.config(state=tk.DISABLED)
            messagebox.showwarning("Advertencia", "Debes aceptar los términos y condiciones para continuar")
            self.create_account_wdw.lift()
            self.terms_wdw.destroy()  # Cierra la ventana            


#-------------------------METODO DONDE SE GUARDAN LOS TERMINOS Y CONDICIONES ---------------------------- 
    def load_terms_and_conditions(self):
        #Texto de terminos y condiciones
        terms_and_conditions = '''
        Bienvenido a ChiWallet. 
        Al usar nuestra aplicación, aceptas los siguientes términos y condiciones:
        
        0. A ver denle run
        1. Uso de la Aplicación: Los usuarios deben aceptar que el uso de la aplicación está sujeto a estos términos y condiciones.
        2. Privacidad de los Datos: Se detalla cómo se recopilan, almacenan y utilizan los datos personales de los usuarios, así como las medidas de seguridad implementadas para proteger dicha información.
        3. Responsabilidad del Usuario: Se establece que los usuarios son responsables de mantener segura su información de inicio de sesión y notificar de inmediato cualquier actividad sospechosa en su cuenta.
        4. Propiedad Intelectual: Se aclara que la aplicación y todo su contenido (diseño, logotipos, texto, etc.) son propiedad de la empresa y están protegidos por las leyes de propiedad intelectual.
        5. Limitación de Responsabilidad: Se especifica que la empresa no será responsable de ningún daño directo, indirecto, incidental, especial, emergente o punitivo que surja del uso o la imposibilidad de usar la aplicación.
        6.Actualizaciones y Cambios: Se reserva el derecho de realizar cambios en la aplicación, incluidas actualizaciones, modificaciones o discontinuación del servicio, en cualquier momento y sin previo aviso.
        7.Terminación de la Cuenta: Se establecen las circunstancias bajo las cuales la empresa puede suspender o cancelar la cuenta de un usuario, así como el proceso para resolver disputas relacionadas.
        8.Legislación Aplicable: Se indica la legislación que regirá estos términos y condiciones, así como la jurisdicción para resolver cualquier disputa legal.
        9.Renuncia de Garantías: Se aclara que la aplicación se proporciona "tal cual" y "según disponibilidad", sin garantías de ningún tipo, ya sean expresas o implícitas.
        10.Consentimiento para Comunicaciones: Se obtiene el consentimiento del usuario para recibir comunicaciones relacionadas con la aplicación, como notificaciones de transacciones, actualizaciones de la aplicación, etc.
        11.Prohibición de Uso Comercial no Autorizado: Se prohíbe el uso comercial no autorizado de la aplicación y se detallan las consecuencias de dicho uso.
        12.Política de Reembolso: Se establecen las políticas y procedimientos para solicitar reembolsos en caso de transacciones no autorizadas o problemas técnicos.
        13.Límites de Responsabilidad Financiera: Se especifican los límites de responsabilidad financiera de la empresa en caso de pérdida de fondos o errores de transacción.
        14.Requisitos de Edad: Se establece la edad mínima requerida para utilizar la aplicación y se informa que los menores de edad deben obtener el consentimiento de sus padres o tutores.
        15.Uso Adecuado de la Aplicación: Se establecen las pautas para el uso adecuado de la aplicación, incluido el cumplimiento de las leyes y regulaciones aplicables.
        16.Notificación de Cambios en los Términos y Condiciones: Se informa a los usuarios que serán notificados de cualquier cambio en los términos y condiciones de la aplicación.
        17.Resolución de Disputas: Se detallan los procedimientos para resolver disputas, incluida la posibilidad de recurrir a la mediación o arbitraje.
        18.Restricciones de Uso: Se enumeran las actividades o comportamientos que están prohibidos en la aplicación, como el fraude, la falsificación de identidad o el uso indebido de fondos.
        19.Seguridad de la Cuenta: Se proporcionan recomendaciones de seguridad para proteger la cuenta del usuario, como el uso de contraseñas seguras y la activación de la autenticación de dos factores.
        20.Acuerdo Completo: Se establece que estos términos y condiciones constituyen el acuerdo completo entre el usuario y la empresa con respecto al uso de la aplicación, y que reemplazan cualquier acuerdo previo o contemporáneo.
        21.Robaremos tus datos bbsite.
        Al hacer clic en "Aceptar", aceptas estos términos y condiciones.
        '''
        
        self.terms_text.insert(tk.END, terms_and_conditions)
        

#-------------------------METODO PARA CREAR LA CUENTA---------------------------------------------------
    def create_account(self):
        
        username = self.create_username_entry.get()
        email = self.create_email_entry.get()
        password= self.create_password_entry.get()
        balance = float()
        
        try:
            #Insertar el nuevo usuario en la BD
            self.connection = sqlite3.connect("ChiWallet.db")
            self.cursor = self.connection.cursor()
            self.cursor.execute('''
                           
                            CREATE TABLE IF NOT EXISTS UserChiWallet(
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            USUARIO TEXT UNIQUE,  
                            CORREO TEXT NOT NULL,  
                            PASSWORD TEXT NOT NULL,
                            BALANCE REAL
                            )
                            ''')
            
            self.cursor.execute('''
                                SELECT USUARIO 
                                FROM UserChiWallet
                                WHERE USUARIO = ?
                                ''', (username,))
            existing_user = self.cursor.fetchone()
            if existing_user:
                messagebox.showwarning("Advertencia","El Usuario ya existe")
            else:
            
                self.cursor.execute('''
                            INSERT INTO UserChiWallet 
                            VALUES (NULL,?,?,?,?) 
                            ''',(username, email, password, balance))
                           
                self.connection.commit()
                
                messagebox.showinfo("Conexion con BD con exito","Usuario Registrado con exito")
                self.create_account_wdw.destroy()
        except sqlite3.Error:
            messagebox.showinfo("Error","Error en la BD")
        
         
        
        self.connection.close()


#-------------------------METODO DE INICIO DE SESION--------------------------------------------------------------
    def login (self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        try:
            self.connection = sqlite3.connect("ChiWallet.db")
            self.cursor = self.connection.cursor()
            self.cursor.execute('''
                           SELECT *
                           FROM UserChiWallet
                           WHERE USUARIO = ?  
                           ''',(username,)) 
            user = self.cursor.fetchone()         
              
        except:
            messagebox.showwarning("Atencion!","El Usuario no esta registrado")
         
        if password == user[3]:  
            messagebox.showinfo("Acceso concedido","Contraseña correcta")
            self.show_principal_window()   
        else:
            messagebox.showwarning("Acceso denegado","Contraseña incorrecta")  


#-------------------------METODO PARA MOSTRAR LA VENTANA PRINCIPAL------------------------------------------ 
    def show_principal_window(self):
    
        root.withdraw()
        
        self.principal_window = tk.Toplevel(root)
        self.principal_window.title("ChiWallet")
        self.principal_window.geometry("375x600")
        
        #Creamos la barra menu
        self.bar_menu = tk.Menu()
        
        #Creamos el primer menu
        self.menu_m = tk.Menu(self.bar_menu, tearoff=False)
        #Agregar a la barra
        self.bar_menu.add_cascade(menu=self.menu_m, label="Menu")
        
        #Añadir comando desplegable
        self.menu_m.add_command(
            label = "Help",
            command = self.help_bm
        )
        self.menu_m.add_command(
            label = "Cerrar Sesion",
            command = self.logout
        )
        self.menu_f = tk.Menu(self.bar_menu, tearoff=False)
        
        self.bar_menu.add_cascade(menu=self.menu_f, label="Funciones")
        self.menu_f.add_command(
            label = "Domiciliar",
            command= self.show_schedule_transfer
            
        )
        self.menu_f.add_command(
            label="Movimientos",
            command=self.show_transactions_list
        )
        self.menu_f.add_command(
            label="Ocultar movimientos",
            command=self.hide_transactions_list
        )
        
        self.principal_window.config(menu=self.bar_menu)
        
        route_image = "C:\\Users\\soter\\OneDrive\\Universidad\\2DO CUATRIMESTRE\\POO\\ChiCoin\\Codigos y BD\\Images\\CHIWALLET.png"
        image = tk.PhotoImage(file=route_image)
        label_img = tk.Label(self.principal_window, image=image)
        label_img.image = image
        label_img.pack()
        
        
        
        self.btn_depositary = tk.Button(self.principal_window, text="DEPOSITAR", cursor="hand2", bg="#005187", 
                                    width=10, relief="flat", font=font_buttons, fg="#FFFFFF", activebackground="#005187", activeforeground="#FFFFFF", command=self.deposit)
        self.btn_depositary.place(x=35, y=175)
        
        self.btn_transfer = tk.Button(self.principal_window, text="TRANSFERIR",cursor="hand2", bg="#005187",
                                 width=10, relief="flat", font=font_buttons, fg="#FFFFFF", activebackground="#005187", activeforeground="#FFFFFF", command=self.transfer)
        self.btn_transfer.place(x=146, y=175)
        
        self.btn_withdraw = tk.Button(self.principal_window, text="RETIRAR", cursor="hand2", bg="#005187", 
                                 width=10, relief="flat", font=font_buttons,fg="#FFFFFF", activebackground="#005178", activeforeground="#FFFFFF", command=self.widthdraw)
        self.btn_withdraw.place(x=260, y=175)
        
        self.balance_lbl = tk.Label(self.principal_window,text="*******", bg="#0069C0", font=font_balance, fg="#FFFFFF")
        self.balance_lbl.place(x=165, y=115)
        
        self.transactions_lbl = tk.Text(self.principal_window, fg="#FFFFFF", width=50, height=10, bg="#0069c0", font=font_moves)
        self.transactions_lbl.configure(state="disabled")
        self.transactions_lbl.place(x=5, y=250,)
        self.scrollbar = tk.Scrollbar(self.principal_window, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.transactions_lbl.yview)
        self.scrollbar.place(x=370, y=250, height=180, anchor="ne")
        self.transactions_lbl.config(yscrollcommand=self.scrollbar.set)
        
         #--Declarar img ojo abierto---#
        self.open_eye = Image.open("C:\\Users\\soter\\OneDrive\\Universidad\\2DO CUATRIMESTRE\\POO\ChiCoin\\Codigos y BD\\Images\\open eye.png")
        img_open_eye = self.open_eye.resize((30,30))
        self.render_open_eye = ImageTk.PhotoImage(img_open_eye)
        
        #--Declarar img cerrar cerrado----#
        self.close_eye = Image.open("C:\\Users\\soter\\OneDrive\\Universidad\\2DO CUATRIMESTRE\\POO\\ChiCoin\\Codigos y BD\\Images\\close eye.png")
        img_close_eye = self.close_eye.resize((30,30))
        self.render_close_eye = ImageTk.PhotoImage(img_close_eye)
        
        
        #--Declarar boton ojo abierto
        self.btn_image_eye = tk.Button(self.principal_window, image=self.render_close_eye, bg="#0069C0", relief="flat", activebackground="#0069C0", command=self.turn_open_eye)
        self.btn_image_eye.place(x=315, y=90)
        
        #llamamos al metodo de realizar la tranferencia programada 
        #self.execute_scheduled_transfers()
        #llamamos al metodo para que se esconda la lista de transacciones
        self.hide_transactions_list()
        
        self.principal_window.mainloop()
        


#-------------------------METODO PARA ABRIR EL OJO Y MOSTRAR SALDO--------------------------#
    def turn_open_eye(self):
            self.btn_image_eye = tk.Button(self.principal_window, image=self.render_open_eye, bg="#0069C0", relief="flat", activebackground="#0069C0", command=self.turn_close_eye)
            self.btn_image_eye.place(x=315, y=90)
            
            self.update_balance()
            

#-------------------------METODO PARA CERRAR EL OJO Y MOSTRAR SALDO---------------------------#       
    def turn_close_eye(self):
            self.balance_lbl.destroy()
            
            self.btn_image_eye = tk.Button(self.principal_window, image=self.render_close_eye, bg="#0069C0", relief="flat", activebackground="#0069C0", command=self.turn_open_eye)
            self.btn_image_eye.place(x=315, y=90)
            self.balance_lbl = tk.Label(self.principal_window,text="******", bg="#0069C0", font=font_balance, fg="#FFFFFF")
            self.balance_lbl.place(x=165, y=115)


#-------------------------METODO PARA ACTUALIZAR EL BALANCE------------------------------------------
    def update_balance(self):
        self.username = self.username_entry.get()
        try:
            self.connection = sqlite3.connect("ChiWallet.db")
            self.cursor = self.connection.cursor()
            self.cursor.execute(
                                '''  
                                SELECT BALANCE
                                FROM UserChiWallet
                                WHERE USUARIO = ?  
                                ''' ,(self.username,)
                                )
            balance_search = self.cursor.fetchone()
            self.balance = balance_search[0]
            self.balance_lbl.config(text=self.balance)
            self.balance_lbl.place(x=140, y=115)
        except sqlite3.Error:
            messagebox.showerror("Error,","Error con la base de datos")
        self.connection.commit()


#-------------------------METODO PARA DEPOSITAR------------------------------------------------------------  
    def deposit(self):
        username = self.username_entry.get()
        amount = float(simpledialog.askfloat("Deposito", "Ingrese la cantidad que desea depositar"))
        chain_amount = (f"${amount}")
        self.cursor.execute('''
                            UPDATE UserChiWallet
                            SET BALANCE = BALANCE + ?
                            WHERE USUARIO = ?
                            ''', (amount, username))
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS Transactions
                            (IDT INTEGER PRIMARY KEY AUTOINCREMENT,
                            CONCEPT TEXT NOT NULL,
                            AMOUNT INTEGER NOT NULL,
                            USUARIO TEXT,
                            FOREIGN KEY (USUARIO) REFERENCES UserChiWallet(USUARIO))
                            ''')
        self.cursor.execute('''
                            INSERT INTO Transactions
                            VALUES (NULL,?,?,?)
                            ''',("Deposito", chain_amount, username))
        self.connection.commit()
        
        messagebox.showinfo("Deposito","Deposito exitoso")
        self.update_balance()
        self.turn_open_eye()


#-------------------------METODO PARA TRANSEFERIR-----------------------------------------------------------   
    def transfer(self):   
        username= self.username_entry.get()
        destination_user = simpledialog.askstring("Tranferencia","Ingrese el Usuario a quien desea transferir")
        amount = simpledialog.askfloat("Transferencia","Ingrese el monto a transferir")
        try:
            if self.enough_balance() >= amount:
                self.connection = sqlite3.connect("ChiWallet.db")
                self.cursor = self.connection.cursor()
                self.cursor.execute('''
                            SELECT *
                            FROM UserChiWallet
                            WHERE USUARIO = ?
                            ''', (destination_user,))
                user_search = self.cursor.fetchone()
        
                if user_search is not None:
                    self.cursor.execute(
                                    '''
                                    UPDATE UserChiWallet 
                                    SET BALANCE = BALANCE + ? 
                                    WHERE USUARIO = ?
                                    ''',(amount, destination_user))
                    self.cursor.execute('''
                                    UPDATE UserChiWallet 
                                    SET BALANCE = BALANCE - ? 
                                    WHERE USUARIO = ?
                                    ''',(amount, username))
                    
                    chain_destiantion = (f"Transferencia a {destination_user}")
                    chain_user = (f"Recibiste de {username}")
                    chain_amount = (f"${amount}")
                
        
                    self.cursor.execute('''
                                    CREATE TABLE IF NOT EXISTS Transactions
                                    (IDT INTEGER PRIMARY KEY AUTOINCREMENT,
                                    CONCEPT TEXT NOT NULL,
                                    AMOUNT INTEGER NOT NULL,
                                    USUARIO TEXT,
                                    FOREIGN KEY (USUARIO) REFERENCES UserChiWallet(USUARIO))
                                    ''')
                    self.cursor.execute('''
                                    INSERT INTO Transactions
                                    VALUES (NULL,?,?,?)
                                    
                                    ''', (chain_destiantion, chain_amount, username))
                    self.cursor.execute('''
                                    INSERT INTO Transactions
                                    VALUES (NULL,?,?,?)
                                    ''', (chain_user, chain_amount, destination_user))
                    self.connection.commit()
                
                    
                    messagebox.showinfo("Tranferencia",f"Tranferencia existosa de: ${amount} a la cuenta: {destination_user}")
                    self.update_balance()
                    self.turn_open_eye()
                    
                else:
                    messagebox.showwarning("Advertencia","El usuario no existe")
            else: 
                messagebox.showwarning("Advertencia","Saldo insuficiente")    
        except sqlite3.Error:
                messagebox.showwarning("Advertencia","El usuario no existe")
              
                
#-------------------------METOOD PARA MOSTRAR LA VENTANA DE TRANFERENCIA PROGRAMADA----------------------------    
    def show_schedule_transfer(self):
        self.window_schedule = tk.Tk()
        self.window_schedule.title("Programar Transferencia")

        self.amount_lbl = tk.Label(self.window_schedule, text = "Monto a transferir:")
        self.amount_lbl.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.amount_entry = tk.Entry(self.window_schedule)
        self.amount_entry.grid(row = 0, column = 1, padx = 5, pady = 5)

        self.destination_user_lbl = tk.Label(self.window_schedule, text = "Cuenta de destino:")
        self.destination_user_lbl.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.destination_user_entry = tk.Entry(self.window_schedule)
        self.destination_user_entry.grid(row = 2, column = 1, padx = 5, pady = 5)

        self.date_transfer = tk.Label(self.window_schedule, text = "Fecha de transferencia")
        self.date_transfer.grid(row = 3, column = 0, padx = 5, pady = 5)
        self.date_entry = DateEntry(self.window_schedule, width = 12, bg = "#F5F5DC", forerguard = "white", borderwith = 2)
        self.date_entry.grid(row = 3, column = 1, padx = 5, pady = 5)

        self.program_button = tk.Button(self.window_schedule, text = "Guardar transferencia", command = self.save_schedule_transfer)
        self.program_button.grid(row = 4, column = 0, padx = 5, pady = 5)

        self.window_schedule.mainloop()


#-------------------------METODO PARA PROGRAMAMR TRANFERENCIA--------------------------------------------#
    def save_schedule_transfer(self):
        
        amount = float(self.amount_entry.get())
        username = self.username_entry.get()
        destination_user = self.destination_user_entry.get()
        self.transfer_date = self.date_entry.get_date()
        done='No'

        #Obtenemos la fecha de hoy y la seleccionada, la convertimos al mismo formato 
        self.current_date=datetime.now().strftime('%Y-%m-%d')
        self.transfer_date_str = self.transfer_date.strftime('%Y-%m-%d')
        
        if self.transfer_date_str < self.current_date:
            messagebox.showwarning("Error", "La fecha seleccionada ya pasó")
        else:
            try:
                self.connection = sqlite3.connect("ChiWallet.db")
                self.cursor = self.connection.cursor()
                self.cursor.execute('''
                                SELECT *
                                FROM UserChiWallet
                                WHERE USUARIO = ?
                                ''', (destination_user,))
                user_search = self.cursor.fetchone()
                #comprueba que el usuario existe
                if user_search is not None:
                
                    #Comprueba que el balance sea suficiente con el metodo enough_balance
                    if self.enough_balance() >=amount:
                        self.connection=sqlite3.connect("ChiWallet.db")
                        self.cursor = self.connection.cursor()
                        self.cursor.execute('''
                                        CREATE TABLE IF NOT EXISTS ScheduleTransfers
                                        (IDST INTEGER PRIMARY KEY AUTOINCREMENT,
                                        DATE DATE NOT NULL,
                                        AMOUNT INTEGER,
                                        DESTINATION TEXT,
                                        USUARIO TEXT,
                                        REALIZADO TEXT,
                                        FOREIGN KEY (USUARIO) REFERENCES UserChiWallet(USUARIO))
                                        ''')
                    
                        self.cursor.execute('''
                                        INSERT INTO ScheduleTransfers
                                        VALUES (NULL,?,?,?,?,?)
                                        ''',(self.transfer_date, amount, destination_user, username, done,))
                    
                        messagebox.showinfo("Tranferencia programada",f"Se guardo una tranferencia a:{destination_user} de ${amount} ") 
                        self.connection.commit()
                    else:
                        messagebox.showwarning("Error", "Su saldo es insuficiente, es imposible realizar el retiro") 
                else:
                    messagebox.showwarning("Advertencia", "El usuario de destino no existe")
            except sqlite3.Error:
                messagebox.showerror("Error","No se logró programar la tranferencia")

            self.window_schedule.destroy()


#-------------------------METODO PARA QUE SE REALICE LA TRANSFERENCIA PROGRAMADA-------------------------------------------    
    def do_schedule_transfer(self, transfer_id, amount, destination_user, username, current_date):
        try:
            # Realizar la transferencia en la base de datos
            self.cursor.execute('''
                UPDATE UserChiWallet 
                SET BALANCE = BALANCE + ? 
                WHERE USUARIO = ? 
            ''',(amount, destination_user))
                
            self.cursor.execute('''
                UPDATE UserChiWallet 
                SET BALANCE = BALANCE - ? 
                WHERE USUARIO = ?
            ''',(amount, username))
        
                
            # Registrar la transferencia en el registro de transacciones
            chain_destination_user = (f"Transferencia Programada a:{destination_user}")
            chain_user = (f"Recibiste Pago Domiciliado de:{username}")
            chain_amount = (f"${amount}")
            
            self.cursor.execute('''
                INSERT INTO Transactions
                VALUES (NULL,?,?,?)
                
            ''', (chain_destination_user, chain_amount, username))
            self.cursor.execute('''
                INSERT INTO Transactions
                VALUES (NULL,?,?,?)
            ''',(chain_user, chain_amount, destination_user))
            
            
            self.transfer_done()

        except sqlite3.Error as error:
            print("Error en la base de datos:", error)
            messagebox.showerror("Error", "Error en la base de datos: " + str(error))
            
            
 #------------------------METODO PARA EJECUTAR LA TRNAFERENCIA PROGRAMADA-----------------------------           
    def execute_scheduled_transfers(self):
        try:
            self.connection = sqlite3.connect("ChiWallet.db")
            self.cursor = self.connection.cursor()
            
            # Obtener las transferencias programadas para la fecha actual
            current_date = datetime.now().strftime('%Y-%m-%d')
            self.cursor.execute('''
                SELECT *
                FROM ScheduleTransfers
                WHERE DATE = ? AND REALIZADO = 'No'
            ''', (current_date,))
            
            scheduled_transfers = self.cursor.fetchall()
            
            for transfer in scheduled_transfers:
                transfer_id, transfer_date, amount, destination_user, username, done = transfer
                
                # Realizar la transferencia
                self.do_schedule_transfer(transfer_id, amount, destination_user, username, current_date)
                
          
            self.connection.commit()
            
    
            
        except sqlite3.Error as error:
            print("Error en la base de datos:", error)
            messagebox.showerror("Error", "Error en la base de datos: " + str(error))


    def transfer_done(self):
        done = "Si"
        try:
            self.cursor.execute('''
                                UPDATE ScheduleTransfers
                                SET REALIZADO = ?
                                WHERE DATE = ?
                                ''',(done, self.current_date))
        except:
            messagebox.showerror("Error","Erro al registrar la transferencia registrada")
#-------------------------METODO PARA RETIRAR------------------------------------------------------------ 
    def widthdraw (self):
        username = self.username_entry.get()
        amount = float(simpledialog.askfloat("Retirar","Ingrese el monto que desea rertirar"))
        chain_amount = (f"${amount}")
        if self.enough_balance()>=amount:
            self.cursor.execute('''
                            UPDATE UserChiWallet 
                            SET BALANCE = BALANCE - ? 
                            WHERE USUARIO = ?
                            ''', (amount, username))
            self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS Transactions
                            (IDT INTEGER PRIMARY KEY AUTOINCREMENT,
                            CONCEPT TEXT NOT NULL,
                            AMOUNT INTEGER NOT NULL,
                            USUARIO TEXT,
                            FOREIGN KEY (USUARIO) REFERENCES UserChiWallet(USUARIO))
                            ''')
            self.cursor.execute('''
                            INSERT INTO Transactions
                            VALUES (NULL,?,?,?)
                            ''',("Retiro", chain_amount, username))
        
            self.connection.commit()
        
            messagebox.showinfo("Retiro","Retiro exitoso!")
            self.update_balance()
            self.turn_open_eye()
        else:
            messagebox.showwarning("Advertencia", "Saldo insuficiente")           


#-------------------------METODO PARA MOSTRAR LA LISTA DE TRANSACCIONES----------------------------        
    def show_transactions_list(self):
        self.transactions_lbl = tk.Text(self.principal_window, width=50, height=11, fg="#FFFFFF", bg="#0069c0", font=font_moves)
        self.transactions_lbl.place(x=5, y=250,)
        
        self.scrollbar = tk.Scrollbar(self.principal_window, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.transactions_lbl.yview)
        self.scrollbar.place(x=370, y=250, height=180, anchor="ne")
        self.transactions_lbl.config(yscrollcommand=self.scrollbar.set)
        
        username = self.username_entry.get()
        try:
            self.cursor.execute('''
                            SELECT CONCEPT, AMOUNT
                            FROM Transactions
                            WHERE USUARIO = ? 
                            ORDER BY IDT DESC
                            ''', (username,))
        
            self.transactions_list = self.cursor.fetchall()
            self.transactions_text = ""
            for self.concept, self.amount  in (self.transactions_list):
                self.transactions_text += f"{self.concept}: {self.amount}\n"
                
            self.transactions_lbl.insert(tk.END, self.transactions_text)
            
                  
        except sqlite3.Error:
            messagebox.showerror("Error","Falla en el DB")
    

#-------------------------METODO PARA ESCONDER LA LISTA DE TRANSACCIONES----------------------------------------------        
    def hide_transactions_list(self):
        self.transactions_lbl.destroy()
        self.scrollbar.destroy()


#-------------------------METODO DE SALDO INSUFICIENTE-------------------------------------------------------#
    def enough_balance(self):
        self.connection=sqlite3.connect("ChiWallet.db")
        self.cursor=self.connection.cursor()
        
        self.cursor.execute('''
                            SELECT  BALANCE FROM UserChiWallet
                            WHERE USUARIO = ?
                            ''', (self.username_entry.get(),))             
        balance = self.cursor.fetchone()
        return balance[0] if balance else 0


#-------------------------METODO DE AYUDA-------------------------------------------------------------------#
    def help_bm(self):
            help_wdw = tk.Toplevel(root)
            help_wdw.title("Ayuda")
            help_wdw.geometry("660x500")
            help_txt =  '''
                                                                                                          PREGUNTAS FRECUENTES
        
¿Qué es una wallet digital?
Una wallet digital es un software o servicio en línea que permite almacenar, gestionar y realizar transacciones con diferentes tipos de activos digitales, como monedas fiduciarias, criptomonedas, tokens de blockchain, entre otros.

¿Cómo puedo crear una wallet digital?
Puedes crear una wallet digital registrándote en plataformas en línea que ofrecen este servicio. Generalmente, el proceso implica proporcionar información básica, establecer una contraseña segura y seguir los pasos de verificación necesarios.

¿Qué tipos de wallets digitales existen?
Hay varios tipos de wallets digitales, incluyendo wallets en línea (hot wallets), wallets de escritorio, wallets móviles y wallets de hardware. Cada tipo tiene sus propias características y niveles de seguridad.

¿Cómo puedo proteger mi wallet digital?
Puedes proteger tu wallet digital utilizando medidas de seguridad como contraseñas robustas, autenticación de dos factores (2FA), encriptación de datos y manteniendo actualizado tu software de seguridad.

¿Puedo acceder a mi wallet digital desde múltiples dispositivos?
Sí, dependiendo del tipo de wallet digital que utilices, es posible que puedas acceder a ella desde varios dispositivos. Por ejemplo, muchas wallets en línea y móviles permiten el acceso desde diferentes dispositivos con la misma cuenta.

¿Qué debo hacer si olvido mi contraseña de la wallet digital?
Si olvidas la contraseña de tu wallet digital, algunas plataformas ofrecen opciones de recuperación de contraseña mediante preguntas de seguridad o mediante el envío de un enlace de restablecimiento a tu dirección de correo electrónico.

¿Cuánto cuesta crear y mantener una wallet digital?
La creación y mantenimiento de una wallet digital pueden ser gratuitas o tener un costo asociado, dependiendo del proveedor y del tipo de wallet que elijas. Algunas plataformas pueden cobrar tarifas por transacciones o por servicios adicionales.

¿Qué información debo proporcionar al crear una wallet digital?
Al crear una wallet digital, generalmente se te pedirá que proporciones información básica como nombre, dirección de correo electrónico y contraseña. Además, es posible que necesites completar un proceso de verificación para cumplir con requisitos de seguridad.

¿Es seguro almacenar grandes cantidades de activos en una wallet digital?
La seguridad de almacenar grandes cantidades de activos en una wallet digital depende del tipo de wallet que utilices y de las medidas de seguridad que implementes. Las wallets de hardware suelen considerarse más seguras para almacenar grandes cantidades de activos debido a su aislamiento físico de internet.

¿Qué debo hacer si sospecho que mi wallet digital ha sido comprometida?
Si sospechas que tu wallet digital ha sido comprometida o has detectado actividad no autorizada, es importante actuar rápidamente. Esto puede incluir cambiar tu contraseña, desactivar tu cuenta temporalmente y contactar al servicio de soporte técnico de la plataforma para recibir asistencia.
                        '''
            help_lbl = tk.Text(help_wdw, width=80, height=50)
            help_lbl.place(x=1, y=1)
            help_lbl.insert(tk.END,help_txt)
            help_scroll = tk.Scrollbar(help_wdw, orient=tk.VERTICAL)
            help_scroll.config(command=help_lbl.yview)
            help_scroll.place(x=660, y=1, height=500, anchor="ne")
            help_lbl.config(yscrollcommand=help_scroll.set)
 
            
#-------------------------METODO DE CERRAR SESION-----------------------------------------------------------           
    def logout(self):
        if hasattr(self, "principal_window"):
            self.principal_window.destroy()
        
        self.root.deiconify()
    
            
root=tk.Tk()
app = ChiWallet(root)      
root.mainloop()



