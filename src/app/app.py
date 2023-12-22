import flet as ft

def text_button(str, callback):
  def on_click(e):
    if (str == '<'):
      callback('Backspace')
    elif (str == '>'):
      callback('Enter')
    else:
      callback(str)

  return ft.TextButton(str, on_click=on_click)

def main(page: ft.Page):
  page.title = 'Calc app'
  text_field = ft.TextField(value='', text_align=ft.TextAlign.RIGHT)

  def write(str):
    text_field.value = text_field.value + str
    page.update()

  def on_keyboard(e: ft.KeyboardEvent):
    write(e.key)

  page.on_keyboard_event = on_keyboard

  page.add(ft.Row([text_field]))
  page.add(ft.Row([text_button('7', write), text_button('8', write), text_button('9', write)]))
  page.add(ft.Row([text_button('4', write), text_button('5', write), text_button('6', write)]))
  page.add(ft.Row([text_button('1', write), text_button('2', write), text_button('3', write)]))
  page.add(ft.Row([text_button('<', write), text_button('0', write), text_button('>', write)]))

ft.app(target=main)
