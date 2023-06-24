class Button:
    def paint(self):
        pass

class WindowsButton(Button):
    def paint(self):
        print("Отрисовка кнопки в стиле Windows")

class MacButton(Button):
    def paint(self):
        print("Отрисовка кнопки в стиле macOS")

class Checkbox:
    def paint(self):
        pass

class WindowsCheckbox(Checkbox):
    def paint(self):
        print("Отрисовка флажка в стиле Windows")

class MacCheckbox(Checkbox):
    def paint(self):
        print("Отрисовка флажка в стиле macOS")

class GUIFactory:
    def create_button(self):
        pass

    def create_checkbox(self):
        pass

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

# Использование абстрактной фабрики для создания объектов
def create_gui(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    return button, checkbox

windows_factory = WindowsFactory()
windows_button, windows_checkbox = create_gui(windows_factory)
windows_button.paint()  # Вывод: Отрисовка кнопки в стиле Windows
windows_checkbox.paint()  # Вывод: Отрисовка флажка в стиле Windows

mac_factory = MacFactory()
mac_button, mac_checkbox = create_gui(mac_factory)
mac_button.paint()  # Вывод: Отрисовка кнопки в стиле macOS
mac_checkbox.paint()  # Вывод: Отрисовка флажка в стиле macOS