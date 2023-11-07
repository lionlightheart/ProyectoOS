from flet import *
from src.clases.Buscador import Buscador

#Clase que contiene la pagina del explorador de la interfaz gráfica
class Explorador(Container):
    
    # Función que se encarga de recibir el evento de cambio de ruta 
    def cambiar_ruta(self,e):
        self.ruta_actual = self.buscador.cambiar_directorio(e.control.value)
        if self.ruta_actual is not None:
            self.ruta_actual = self.ruta_actual[0:-1]
            self.container_archivos = self.mostrar_archivos()
            self.caja_archivos.controls = self.container_archivos
            self.caja_archivos.update()

    # Funcion que devuelve un array con los archivos y ficheros que contiene la ruta 
    def mostrar_archivos(self):
        archivos = []
        ruta = self.ruta_actual
        imagen = ""
        items = self.buscador.listar()
        for i in range(len(items)):
            ruta = self.ruta_actual + "\\" + items[i]
            print(ruta)
            if(self.buscador.es_directorio(ruta)):
                imagen = "assets/img/carpeta.png"
            else:
                imagen = "assets/img/fichero.png"
            archivos.append(
                Container(
                    
                    margin=50,
                    content= Column(
                        controls=[
                            Image(
                            src=imagen,
                            width=50,
                            height=50,
                            fit=ImageFit.CONTAIN),
                            Text(value=items[i], size=13)
                        ]
                        ),
                     width=60,
                    height=60,
                  
                     alignment=alignment.center)
            )
        return archivos
    
    
    def __init__(self, page:Page):
        super().__init__()
        self.expand = True
        self.buscador = Buscador()
        self.ruta_actual = self.buscador.mostar_directorio()

        self.container_archivos = self.mostrar_archivos()
        self.input_ruta_actual = TextField(value= self.ruta_actual, on_change=self.cambiar_ruta)
        self.caja_archivos = Row(scroll=ScrollMode.ALWAYS,
                                 width=page.window_width,
                                 height=500,
                                 wrap=True,
                                 spacing=10,
                                on_scroll_interval=0,
                                run_spacing=100,
                                controls= self.container_archivos)
        
        self.content = Container(
            margin=0,
            padding=-40,
            content=Column(
                spacing=0,
                

                controls=[
                    Container(

                        padding=0,
                        margin=0,
                        alignment=alignment.center,
                        content=
                        Row(
                            expand=True,
                            alignment='center',
                            spacing=0,
                            controls=[
                                Container(
                                    alignment=alignment.center_left,
                                    padding=padding.only(top=30, left=40),
                                    expand=True,
                                    height=100,
                                    bgcolor=colors.INDIGO,
                                    content=Container(

                                        content=Text("Libreria OS", size=20, color=colors.WHITE)
                                    )

                                )
                            ]
                        ),
                    ),

                    Row(
                        spacing=0,
                        expand=True,

                        controls=[Container(
                            padding=40,
                            margin=0,

                            height=page.auto_scroll,
                            width=300,
                            bgcolor=colors.BLUE_50,
                            content=Column(
                                expand=True,

                                controls=[
                                    Column(
                                        height=100,
                                        expand=True,

                                        controls=[Row(
                                            controls=[Container(
                                                content=Row(
                                                    controls=[
                                                        Container(
                                                            content=Icon(icons.SAVE_OUTLINED),
                                                            margin=10
                                                        ),
                                                        Container(
                                                            content=(TextButton("Copias de seguridad",
                                                                                on_click=lambda _: self.page.go(
                                                                                    "/menu")))
                                                        )
                                                    ]))
                                            ]
                                        ), Row(
                                            controls=[Container(
                                                content=Row(
                                                    controls=[
                                                        Container(
                                                            content=Icon(icons.COMPUTER_OUTLINED),
                                                            margin=10
                                                        ),
                                                        Container(
                                                            content=(TextButton("Información PC",
                                                                                on_click=lambda _: self.page.go(
                                                                                    "/info")))
                                                        )
                                                    ]))]
                                        ), Row(
                                            controls=[Container(
                                                content=Row(
                                                    controls=[
                                                        Container(
                                                            content=Icon(icons.EXPLORE_OUTLINED),
                                                            margin=10
                                                        ),
                                                        Container(
                                                            content=(TextButton("Explorador de archivos",
                                                                                on_click=lambda _: self.page.go(
                                                                                    "/explorador")))
                                                        )
                                                    ]))]
                                        )
                                        ]
                                    )
                                ]
                            )

                        ),
                            Container(expand=True,
                                      padding=padding.only(left=10, right=40, top=10, bottom=40),
                                      content=Column(
                                          expand=True,
                                          spacing=0,
                                        alignment= alignment.top_center,

                                          controls=[
                                            Column(
                                                expand=True,
                                                alignment= alignment.top_center,

                                                controls=[
                                                    Container(
                                                        content=self.input_ruta_actual,
                                                        height=50
                                                    ),self.caja_archivos
                                                    
                                                ]
                                            )
                                          ]
                                      )
                                      )
                        ]
                    )
                ]
            ))
        