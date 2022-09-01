from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        self.window.add_widget(Image(source=('logo.jpg')))

        self.greeting = Label(
                    text = 'What is your name?',
                    font_size = 20,
                    color = '#00F366')
        self.window.add_widget(self.greeting)
        self.user = TextInput(
                    multiline=False,
                    size_hint = (0.5, 0.4),
                    padding_y = (20, 20),
                    padding_x = (5, 20))
        self.window.add_widget(self.user)
        self.button = Button(
                    text='GREET',
                    size_hint = (0.5, 0.3),
                    bold = True,
                    background_color = '#00F366'
                    )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window
    
    def callback(self, event):
        self.greeting.text = f'Hey, {self.user.text}! Welcome.'


if __name__ == '__main__':
    SayHello().run()