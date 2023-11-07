from flet import  *
from src.paginas.menu import Menu
from src.paginas.informacion import  Info
from src.paginas.expplorador import Explorador


class Main(UserControl):

    def __init__(self, page:Page):
        super().__init__()
        self.page = page
        self.init_helper()
        page.padding = 0
        page.margin = 0

    def init_helper(self):
        self.page.on_route_change = self.on_route_change
        self.page.go("/menu")


    def on_route_change(self, route):
        new_page = {
            "/menu": Menu,
            "/info": Info,
            "/explorador": Explorador
        }[self.page.route](self.page)
        self.page.views.clear()
        self.page.views.append(
            View(
                route,
                [new_page]
            )
        )
app(target=Main, assets_dir="assets")