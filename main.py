# import flet as ft


# def main(page: ft.Page):
#     page.title = "Цветное приложение 😎"
#     page.theme_mode = ft.ThemeMode.LIGHT

#     text_hello = ft.Text("Hello world", size=20)

#     name_input = ft.TextField(label="Введите имя")

#     def send_name(_):
#         name = name_input.value.strip()
#         if name:
#             text_hello.value = f"Hello {name}"
#             text_hello.color = None
#             name_input.value = ""
#         else:
#             text_hello.value = "Введите имя!"
#             text_hello.color = ft.Colors.RED

#         page.update()

#     send_button = ft.ElevatedButton("Send", on_click=send_name)

#     colors = [
#         ft.Colors.BLUE,
#         ft.Colors.GREEN,
#         ft.Colors.ORANGE,
#         ft.Colors.PURPLE,
#         ft.Colors.PINK,
#         ft.Colors.TEAL,
#     ]

#     color_index = 0

#     def change_color(_):
#         nonlocal color_index
#         page.bgcolor = colors[color_index]
#         color_index = (color_index + 1) % len(colors)
#         page.update()

#     color_button = ft.IconButton(
#         icon=ft.Icons.COLOR_LENS,
#         tooltip="Сменить цвет",
#         on_click=change_color
#     )

#     page.add(
#         text_hello,
#         name_input,
#         send_button,
#         color_button
#     )

# ft.app(target=main)







import flet as ft
import datetime

def main(page: ft.Page):
    page.title = 'My first Flet app'
    page.theme_mode = ft.ThemeMode.LIGHT
    text_hello = ft.Text(value="HELLO WORLD", color=ft.Colors.BLUE)

    text_hello.value = 'Привет!'

    def on_button_click(e):
        name = name_input.value.strip()
        current_time = datetime.datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
        print(f"Пользователь ввел: {name}")
        print(f"Время ввода: {current_time}")
        if name:
            current_time = datetime.datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
            text_hello.value = f'{current_time} - Здравствуйте, {name}!'
            text_hello.color = ft.Colors.GREEN
            name_input.value = None
        else:
            text_hello.value = "Пожалуйста, введите имя!"
            text_hello.color = ft.Colors.RED
            name_input.value = None
        page.update()


    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            theme_button.icon = ft.Icons.LIGHT_MODE
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            theme_button.icon = ft.Icons.DARK_MODE
        page.update()

    elevated_button = ft.ElevatedButton("ОТПРАВИТЬ", icon=ft.Icons.SEND, on_click=on_button_click)
    name_input = ft.TextField(label='Введите ваше имя', on_submit=on_button_click)

    theme_button = ft.IconButton(
        icon=ft.Icons.DARK_MODE,
        tooltip="День / Ночь",
        on_click=toggle_theme
    )

    page.add(theme_button, text_hello, name_input, elevated_button)


ft.app(target=main)


    