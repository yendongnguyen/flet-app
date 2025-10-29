import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text, TextField, RadioGroup, Radio, Dropdown, dropdown, Card, ListTile, Divider
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
from datetime import datetime

def main(page: Page) -> None:
    page.title = 'Flet App'
    page.theme_mode = ft.ThemeMode.LIGHT
    
    user_data = {}

    email_error = Text(value="", color="red", size=12)
    password_error = Text(value="", color="red", size=12)
    
    # Login page
    email_field = TextField(
        label="Email",
        width=300,
        border_color=ft.Colors.GREY_400
    )
    
    password_field = TextField(
        label="Password",
        password=True,
        can_reveal_password=True,
        width=300,
        border_color=ft.Colors.GREY_400
    )
    
    # Form page fields
    name_field = TextField(label="Name", width=400)
    
    
    # Date picker
    def handle_date_change(e):
        dob_field.value = e.control.value.strftime("%Y-%m-%d")
        page.update()

    def open_date_picker(e):
        date_picker.open = True
        page.update()
    
    date_picker = ft.DatePicker(
        on_change=handle_date_change,
        first_date=datetime(1900, 1, 1),
        last_date=datetime.now(),
        help_text="Choose your date of birth",
    )
    
    page.overlay.append(date_picker)
    
    dob_field = TextField(
        label="Date of Birth",
        width=400,
        hint_text="Click to select date",
        read_only=True,
        on_click=open_date_picker,
    )

    gender_group = RadioGroup(
        content=ft.Column([
            Radio(value="Male", label="Male"),
            Radio(value="Female", label="Female"),
            Radio(value="Other", label="Other"),
        ])
    )
    
    address_field = TextField(label="Address", width=400)
    
    country_dropdown = Dropdown(
        label="Country",
        width=400,
        options=[
            dropdown.Option("Finland"),
            dropdown.Option("USA"),
            dropdown.Option("UK"),
            dropdown.Option("Germany"),
            dropdown.Option("France"),
            dropdown.Option("Other"),
        ]
    )
    
    def validate_login(e):
        email_error.value = ""
        password_error.value = ""
        
        is_valid = True
        
        if not email_field.value or email_field.value.strip() == "":
            email_error.value = "Email is required"
            is_valid = False
            
        if not password_field.value or password_field.value.strip() == "":
            password_error.value = "Password is required"
            is_valid = False
        
        page.update()
        
        if is_valid:
            page.go('/home')
    
    def submit_form(e):
        user_data["name"] = name_field.value or "Osman"
        user_data["dob"] = dob_field.value or "2006-12-25 06:00:00"
        user_data["gender"] = gender_group.value or "Male"
        user_data["address"] = address_field.value or "Savonia UAS"
        user_data["country"] = country_dropdown.value or "Finland"
        page.go('/details')
    
    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        # Login view
        page.views.append(
            View(
                route='/',
                controls=[
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Container(
                                    content=Text("flet app", size=24, weight=ft.FontWeight.BOLD, color="white"),
                                    bgcolor=ft.Colors.GREY_800,
                                    padding=20,
                                    width=350,
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(height=30),
                                email_field,
                                email_error,
                                ft.Container(height=10),
                                password_field,
                                password_error,
                                ft.Container(height=30),
                                ElevatedButton(
                                    text="Log in",
                                    width=300,
                                    on_click=validate_login,
                                    bgcolor=ft.Colors.BLUE,
                                    color="white"
                                ),
                            ],
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                        ),
                        padding=40,
                        alignment=ft.alignment.center,
                        expand=True
                    )
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )

        # Home view
        if page.route == '/home':
            page.views.append(
                View(
                    route='/home',
                    controls=[
                        AppBar(
                            title=Text('Home', color="white"),
                            bgcolor=ft.Colors.GREY_800,
                            leading=ft.IconButton(
                                icon=ft.Icons.ARROW_BACK,
                                icon_color="white",
                                on_click=lambda _: page.go('/')
                            )
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    Text(value='Welcome!', size=32, weight=ft.FontWeight.BOLD),
                                    ft.Container(height=20),
                                    ElevatedButton(
                                        text='Go to Form',
                                        on_click=lambda _: page.go('/form'),
                                        width=200,
                                        bgcolor=ft.Colors.BLUE,
                                        color="white"
                                    )
                                ],
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                            ),
                            alignment=ft.alignment.center,
                            expand=True
                        )
                    ],
                    vertical_alignment=MainAxisAlignment.START,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        
        # Form view
        if page.route == '/form':
            page.views.append(
                View(
                    route='/form',
                    controls=[
                        AppBar(
                            title=Text('Form', color="white"),
                            bgcolor=ft.Colors.GREY_800,
                            leading=ft.IconButton(
                                icon=ft.Icons.ARROW_BACK,
                                icon_color="white",
                                on_click=lambda _: page.go('/home')
                            )
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Container(height=20),
                                    name_field,
                                    ft.Container(height=10),
                                    dob_field,
                                    ft.Container(height=10),
                                    Text("Gender:", size=16, weight=ft.FontWeight.BOLD),
                                    gender_group,
                                    ft.Container(height=10),
                                    address_field,
                                    ft.Container(height=10),
                                    country_dropdown,
                                    ft.Container(height=20),
                                    ElevatedButton(
                                        text="Submit",
                                        width=400,
                                        on_click=submit_form,
                                        bgcolor=ft.Colors.BLUE,
                                        color="white"
                                    ),
                                ],
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                scroll=ft.ScrollMode.AUTO,
                            ),
                            padding=20,
                            expand=True
                        )
                    ],
                    vertical_alignment=MainAxisAlignment.START,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        
        # Details view
        if page.route == '/details':
            page.views.append(
                View(
                    route='/details',
                    controls=[
                        AppBar(
                            title=Text('Result', color="white"),
                            bgcolor=ft.Colors.GREY_800,
                            leading=ft.IconButton(
                                icon=ft.Icons.ARROW_BACK,
                                icon_color="white",
                                on_click=lambda _: page.go('/form')
                            )
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Container(height=20),
                                    Card(
                                        content=ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.Container(
                                                        content=Text(user_data.get("name", ""), size=18, weight=ft.FontWeight.BOLD),
                                                        padding=ft.padding.only(left=16, top=16, right=16, bottom=8)
                                                    ),
                                                    Divider(height=1),
                                                    ft.Container(
                                                        content=ft.Row(
                                                            [
                                                                ft.Column(
                                                                    [
                                                                        Text("Date of Birth:", weight=ft.FontWeight.BOLD),
                                                                        Text(user_data.get("dob", "")),
                                                                    ],
                                                                    spacing=2
                                                                ),
                                                            ],
                                                            alignment=MainAxisAlignment.START
                                                        ),
                                                        padding=16
                                                    ),
                                                    ft.Container(
                                                        content=ft.Row(
                                                            [
                                                                ft.Column(
                                                                    [
                                                                        Text("Gender:", weight=ft.FontWeight.BOLD),
                                                                        Text(user_data.get("gender", "")),
                                                                    ],
                                                                    spacing=2
                                                                ),
                                                                ft.Container(width=40),
                                                                ft.Column(
                                                                    [
                                                                        Text("Address:", weight=ft.FontWeight.BOLD),
                                                                        Text(user_data.get("address", "")),
                                                                    ],
                                                                    spacing=2
                                                                ),
                                                            ],
                                                            alignment=MainAxisAlignment.START
                                                        ),
                                                        padding=ft.padding.only(left=16, right=16, bottom=8)
                                                    ),
                                                    ft.Container(
                                                        content=ft.Row(
                                                            [
                                                                ft.Column(
                                                                    [
                                                                        Text("Country:", weight=ft.FontWeight.BOLD),
                                                                        Text(user_data.get("country", "")),
                                                                    ],
                                                                    spacing=2
                                                                ),
                                                            ],
                                                            alignment=MainAxisAlignment.START
                                                        ),
                                                        padding=ft.padding.only(left=16, right=16, bottom=16)
                                                    ),
                                                ],
                                                spacing=0
                                            ),
                                            padding=0,
                                        ),
                                        width=500,
                                        elevation=2
                                    ),
                                    ft.Container(height=20),
                                    ft.TextButton(
                                        text="Go back",
                                        on_click=lambda _: page.go('/Login page')
                                    ),
                                ],
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                            ),
                            alignment=ft.alignment.top_center,
                            expand=True
                        )
                    ],
                    vertical_alignment=MainAxisAlignment.START,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
   
        page.update()
   
    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
   

if __name__ == "__main__":
    ft.app(target=main)