class Phone():
    def __init__(self,brand,ram,memory):
        self.brand = brand
        self.ram = ram
        self.memory = memory
        self.is_on = False
        self.apps = []
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def download_app(self,app):
        self.apps.append(app)

phone = Phone("samsung", "8gb", "128gb")
phone.download_app("facebook")
phone.download_app("Tik tok")
phone.turn_on()

print(phone.apps)
print(phone.is_on)
