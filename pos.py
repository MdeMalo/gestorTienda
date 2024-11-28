from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty


class POSApp(BoxLayout):
    cart = ListProperty()  # Lista para almacenar el carrito de compras
    total = StringProperty("0.00")  # Total en formato string

    def add_to_cart(self, product, quantity, price):
        if not product or not quantity.isdigit() or not price.replace('.', '', 1).isdigit():
            return  # Validar datos antes de agregar
        quantity = int(quantity)
        price = float(price)
        total_price = quantity * price
        self.cart.append(f"{product} x{quantity} - ${total_price:.2f}")
        self.calculate_total()

    def calculate_total(self):
        self.total = "{:.2f}".format(sum(
            float(item.split('- $')[-1]) for item in self.cart
        ))

    def clear_cart(self):
        self.cart.clear()
        self.total = "0.00"


class POSAppMain(App):
    def build(self):
        # Asegurar que el archivo KV se cargue correctamente
        self.load_kv('pos.kv')
        return POSApp()


if __name__ == '__main__':
    POSAppMain().run()
