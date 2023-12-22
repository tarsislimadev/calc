import flet as ft

def main(page: ft.Page):
  page.title = "Calc app"
  page.bgcolor = ft.colors.WHITE
  text_field = ft.Text("", color = ft.colors.BLACK)

  def write(text):
    match(text):
      case ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        text_field.value = text_field.value + text
      case ["Backspace", "Enter"]:
        text_field.value = ""

    page.update()

  def text_button(text):
    def on_click(e):
      if (text == "<"):
        write("Backspace")
      elif (text == ">"):
        write("Enter")
      else:
        write(text.replace("Numpad ", ""))

    return ft.TextButton(text, on_click=on_click)

  page.on_keyboard_event = lambda e: write(e.key)
  page.add(ft.Row([text_field]))
  page.add(ft.Row([text_button("7"), text_button("8"), text_button("9")]))
  page.add(ft.Row([text_button("4"), text_button("5"), text_button("6")]))
  page.add(ft.Row([text_button("1"), text_button("2"), text_button("3")]))
  page.add(ft.Row([text_button("<"), text_button("0"), text_button(">")]))

ft.app(target=main)
