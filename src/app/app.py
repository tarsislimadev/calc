import flet as ft

def main(page: ft.Page):
  page.title = "Calc app"
  page.bgcolor = ft.colors.BLUE_50
  text_field = ft.Text("")

  def write(str):
    print("write: " + str)

    match str.replace("Numpad ", ""):
      case ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        text_field.value = text_field.value + str
      case "Backspace":
        print("backspace: " + text_field.value)
      case "Enter":
        print("enter: " + text_field.value)
    page.update()

  page.on_keyboard_event = lambda e: write(e.key)

  page.add(ft.Row([text_field]))
  page.add(ft.Row([text_button("7", write), text_button("8", write), text_button("9", write)]))
  page.add(ft.Row([text_button("4", write), text_button("5", write), text_button("6", write)]))
  page.add(ft.Row([text_button("1", write), text_button("2", write), text_button("3", write)]))
  page.add(ft.Row([text_button("<", write), text_button("0", write), text_button(">", write)]))

def text_button(str, callback):
  def on_click(e):
    if (str == "<"):
      callback("Backspace")
    elif (str == ">"):
      callback("Enter")
    else:
      callback(str)

  return ft.TextButton(str, on_click=on_click)

ft.app(target=main)
