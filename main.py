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


#-------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------#




import flet as ft
import datetime
import os

HISTORY_FILE = "history.txt"

def main(page: ft.Page):
    page.title = 'My first Flet app'
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text(value="Привет!", color=ft.Colors.BLUE)

    greeting_history = []

    history_text = ft.Text("История приветствий:")

    
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            greeting_history.extend(
                [line.strip() for line in f.readlines() if line.strip()]
            )

        greeting_history[:] = greeting_history[-5:]

        if greeting_history:
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)

   
    def save_history():
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            for item in greeting_history:
                f.write(item + "\n")

   
    def on_button_click(e):
        name = name_input.value.strip()
        current_time = datetime.datetime.now().strftime("%Y:%m:%d - %H:%M:%S")

        if name:
            record = f"{current_time} - Здравствуйте, {name}!"
            text_hello.value = record
            text_hello.color = ft.Colors.GREEN
            name_input.value = ""

            greeting_history.append(record)
            greeting_history[:] = greeting_history[-5:]

            save_history()
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            text_hello.value = "Пожалуйста, введите имя!"
            text_hello.color = ft.Colors.RED

        page.update()

    
    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            theme_button.icon = ft.Icons.LIGHT_MODE
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            theme_button.icon = ft.Icons.DARK_MODE
        page.update()

    
    favorite_names = []
    favorite_text = ft.Text("Любимые имена:")

    def add_to_favorites(e):
        if greeting_history:
            last = greeting_history[-1]
            name = last.split(", ")[1].replace("!", "")

            if name not in favorite_names:
                favorite_names.append(name)
                favorite_text.value = "Любимые имена:\n" + "\n".join(favorite_names)
                page.update()

   
    def delete_last_greeting(e):
        if greeting_history:
            greeting_history.pop()
            save_history()

            if greeting_history:
                history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
            else:
                history_text.value = "История приветствий:"
        else:
            text_hello.value = "История пуста!"
            text_hello.color = ft.Colors.RED

        page.update()

    
    def sort_history(e):
        if greeting_history:
            greeting_history.sort(key=lambda x: x.split(", ")[1])
            save_history()
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            text_hello.value = "История пуста!"
            text_hello.color = ft.Colors.RED

        page.update()


    name_input = ft.TextField(
        label="Введите ваше имя",
        on_submit=on_button_click
    )

    send_button = ft.ElevatedButton(
        "ОТПРАВИТЬ",
        icon=ft.Icons.SEND,
        on_click=on_button_click
    )

    theme_button = ft.IconButton(
        icon=ft.Icons.DARK_MODE,
        tooltip="День / Ночь",
        on_click=toggle_theme
    )

    delete_button = ft.ElevatedButton(
        "Удалить последнее",
        icon=ft.Icons.DELETE,
        on_click=delete_last_greeting
    )

    sort_button = ft.ElevatedButton(
        "Сортировать по алфавиту",
        icon=ft.Icons.SORT_BY_ALPHA,
        on_click=sort_history
    )

    favorite_button = ft.ElevatedButton(
        "Добавить в избранное",
        on_click=add_to_favorites
    )


    main_buttons = ft.Row(
        controls=[send_button, theme_button],
        spacing=10
    )

    history_buttons = ft.Row(
        controls=[delete_button, sort_button],
        spacing=10
    )

    page.add(
        text_hello,
        name_input,
        main_buttons,
        history_text,
        history_buttons,
        favorite_button,
        favorite_text
    )

ft.app(target=main)



    