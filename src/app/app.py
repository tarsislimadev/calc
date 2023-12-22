import flet as ft

class CalcApp(ft.Page):
  def __init__(self):
    self.title = "Calc app"
    self.text_field = ft.Text("", size=100)
    self.on_keyboard_event = lambda e: self.write(e.key)

    self.add(ft.Row([self.text_field]))
    self.add(ft.Row([self.text_button("7"), self.text_button("8"), self.text_button("9")]))
    self.add(ft.Row([self.text_button("4"), self.text_button("5"), self.text_button("6")]))
    self.add(ft.Row([self.text_button("1"), self.text_button("2"), self.text_button("3")]))
    self.add(ft.Row([self.text_button("<"), self.text_button("0"), self.text_button(">")]))

  def text_button(self, str):
    def on_click(e):
      if (str == "<"):
        self.write("Backspace")
      elif (str == ">"):
        self.write("Enter")
      else:
        self.write(str)

    return ft.TextButton(str, on_click=on_click)

  def write(self, str):
    print("write: " + str)
    match str.replace("Numpad ", ""):
      case ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        self.text_field.value = self.text_field.value + str
      case "Backspace":
        print("backspace: " + self.text_field.value)
      case "Enter":
        print("enter: " + self.text_field.value)
    self.update()

ft.app(target=CalcApp)
