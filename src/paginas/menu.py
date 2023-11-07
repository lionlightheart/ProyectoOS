from flet import *
from src.clases.Backup import Backup
import asyncio

import os
class Menu(Container):
    def actualizar(self):
        self.robocopy = "alkfsa"
        self.page.update()
        
    def hacer_copia(self,e):
        try:
            self.backup.select_source_folder(self.ruta_carpeta)
            self.backup.select_destination_folder(self.ruta_destino)
            self.robocopy =  self.backup.execute_backup()
            self.container.value = self.robocopy
            
            self.container.update()
            print(f"&&&&&&&&&&6{self.robocopy}&&&&&&&&&&&&")
            
        except:
            print("")
        self.actualizar()
            
    def cambiar_ruta_carpeta(self,e):
        self.ruta_carpeta = e.control.value
    
    def cambiar_ruta_destino(self,e):
        self.ruta_destino = e.control.value


            
    def __init__(self, page:Page):
        super().__init__()
        self.backup = Backup()
        self.backup.load_config()
        self.container = Text()
        self.ruta_carpeta = ""
        self.ruta_destino = ""
        self.robocopy = ""
        self.expand = True
        page.padding = 0
        page.margin = 0

        self.content =Container(
            margin=0,
            padding=-40,
            content=Column(
            spacing=0,

            controls=[
                Container(

                    padding=0,
                    margin=0,
                    alignment = alignment.center,
                    content=
                    Row(
                        expand=True,
                        alignment='center',
                        spacing=0,
                        controls=[
                            Container(
                                alignment = alignment.center_left,
                                padding = padding.only(top=30,left=40),
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
                                                        content=(TextButton("Copias de seguridad", on_click=lambda _:self.page.go("/menu")))
                                                    )
                                                ]))
                                        ]
                                    ),Row(
                                        controls=[Container(
                                            content=Row(
                                                controls=[
                                                    Container(
                                                    content=Icon(icons.COMPUTER_OUTLINED),
                                                    margin=10
                                                    ),
                                                    Container(
                                                        content=(TextButton("Información PC",on_click=lambda _:self.page.go("/info")))
                                                    )
                                                ]))]
                                    ),Row(
                                        controls=[Container(
                                            content=Row(
                                                controls=[
                                                    Container(
                                                    content=Icon(icons.EXPLORE_OUTLINED),
                                                    margin=10
                                                    ),
                                                    Container(
                                                        content=(TextButton("Explorador de archivos",on_click=lambda _:self.page.go("/explorador")))
                                                    )
                                                ]))]
                                    )
                                    ]
                                )
                            ]
                        )

                    ),
                    Container(expand=True,
                              margin=0,
                              content=Column(
                                  expand=True,
                                 
                                  controls=[
                                      Row(
                                          
                                          alignment="center",
                                          vertical_alignment="center",
                                          spacing=0,
                                          controls=[
                                              Row(
                                                  width=700,
                                                  controls=[
                                                      Column(
                                                          expand=True,
                                                          controls=[
                                                              Container(
                                                                  padding=padding.only(top=40),
                                                                  alignment=alignment.center,

                                                                  content=
                                                                  TextField(on_change=self.cambiar_ruta_carpeta,
                                                                      label="Carpeta inicio",
                                                                      hint_text="Ruta de la carpeta a copiar...",
                                                                  
                                                                      
                                                                  )
                                                              )
                                                          ]
                                                      ),
                                                      Column(
                                                          expand=True,

                                                          controls=[
                                                              Container(
                                                                  alignment=alignment.center,
                                                                  padding=padding.only(top=40),
                                                                  content=
                                                                  TextField(on_change=self.cambiar_ruta_destino,
                                                                      label="Carpeta final",
                                                                      hint_text="Ruta de la carpeta destino..."),

                                                              )
                                                          ]
                                                      ),Column(
                                            
                                                  controls=[
                                                      Container(
                                                          alignment=alignment.center,
                                                                  padding=padding.only(top=40),
                                                          

                                                          content=FilledButton(text="Save", on_click= self.hacer_copia)
                                                      )
                                                  ]
                                              )
                                                  ]),

                                          ]
                                      ), Column(expand=True,
                                                     scroll=ScrollMode.ALWAYS,
                                                     
                                                  controls=[
                                                      Container(
                                                          
                                                          padding=padding.only(bottom=500),
                                                          alignment=alignment.top_center,
                                                          content=self.container
                                                      )
                                                  ]
                                              )
                                  ]
                              )
                              )
                    ]
                )
            ]
        ))
        
        