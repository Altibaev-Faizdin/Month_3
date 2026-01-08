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


def main(page: ft.Page):
    page.title = 'Мое первое приложение!'
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text(value='Hello world')

    def text_name(_):
        name = name_input.value.strip()

        if name:
            text_hello.color = None
            text_hello.value = f'Hello {name}'
            name_input.value = ""
        else:
            text_hello.value = "Введите имя!"
            text_hello.color = ft.Colors.RED

        page.update()

    elevated_button = ft.ElevatedButton('send', on_click=text_name)

    name_input = ft.TextField(label='Введите имя')

    
    def change_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            theme_button.icon = ft.Icons.DARK_MODE
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            theme_button.icon = ft.Icons.LIGHT_MODE

        page.update()

    theme_button = ft.IconButton(
        icon=ft.Icons.LIGHT_MODE,
        on_click=change_theme,
        tooltip="Сменить тему"
    )

    page.add(
        text_hello,
        name_input,
        elevated_button,
        theme_button
    )


ft.app(target=main)

    