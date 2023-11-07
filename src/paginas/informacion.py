from flet import *
from src.clases.PcInfo import PcInfo

#Clase que contiene la pagina de información de la interfaz gráfica
class Info(Container):
    def __init__(self, page:Page):
        self.pc = PcInfo()
        super().__init__()
        self.expand = True
        page.padding = 0
        page.margin = 0
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
                                          controls=[
                                            Container(
                                                expand=True,
                                                margin=0,

                                                content=Column(
                                                    controls=[
                                                        Row(
                                                            expand=True,
                                                            alignment=alignment.center,

                                                            controls=[Container(
                                                                expand=True,
                                                                alignment=alignment.center_right,
                                                                margin=0,
                                                                content=Text(self.pc),
                                                            ),Container(
                                                                expand=True,
                                                                 alignment=alignment.center_left,
                                                                 margin=0,
                                                                 content=Image(
                                                                     src="assets/img/pngwing.com.png",
                                                                      width=300,
                                                                      height=300,
                                                                      fit=ImageFit.CONTAIN,
                                                                      repeat=ImageRepeat.NO_REPEAT,
                                                                      border_radius=border_radius.all(10),
                                                                      
                                                                 )
                                                            )]
                                                        )
                                                    ]
                                                )
                                            )
                                          ]
                                      )
                                      )
                        ]
                    )
                ]
            ))