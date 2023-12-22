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

def backspace(str):
  filtered = [s for s, ix in list(str) if ix != len(str) - 1]

  return filtered.join('')

def enter(str):
  return str

def main(page: ft.Page):
  page.title = 'Calc app'
  text_field = ft.TextField()
  text_field.read_only = True

  def write(str):
    match str.replace('Numpad ', ''):
      case ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        text_field.value = text_field.value + str
      case 'Backspace':
        text_field.value = backspace(text_field.value)
      case 'Enter':
        text_field.value = enter(text_field.value)
    page.update()

  page.on_keyboard_event = lambda e: write(e.key)

  page.add(ft.Row([text_field]))
  page.add(ft.Row([text_button('7', write), text_button('8', write), text_button('9', write)]))
  page.add(ft.Row([text_button('4', write), text_button('5', write), text_button('6', write)]))
  page.add(ft.Row([text_button('1', write), text_button('2', write), text_button('3', write)]))
  page.add(ft.Row([text_button('<', write), text_button('0', write), text_button('>', write)]))

ft.app(target=main)
