# pip install kivy kivy_garden.clock

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

class SABMUSApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Clock
        clock_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        self.clock_label = Label(text="", font_size=24)
        clock_layout.add_widget(self.clock_label)
        layout.add_widget(clock_layout)

        # Gradient background
        self.gradient_color = Color(0.3, 0.7, 1, 1)  # Adjust colors as needed
        self.gradient_rect = Rectangle(pos=(0, 0), size=(self.root_window.width, self.root_window.height))
        with self.canvas:
            self.gradient_color
            self.gradient_rect

        # Task list
        self.task_list = GridLayout(cols=2, spacing=10)
        layout.add_widget(self.task_list)

        # Add task button
        add_task_button = Button(text="Add Task", size_hint=(1, 0.1))
        add_task_button.bind(on_press=self.add_task)
        layout.add_widget(add_task_button)

        # Update clock every second
        Clock.schedule_interval(self.update_clock, 1)

        return layout

    def update_clock(self, dt):
        self.clock_label.text = self.get_current_time()

    def get_current_time(self):
        # Implement logic to get current time in desired format
        return "12:34 PM"  # Example

    def add_task(self, instance):
        # Implement logic to add a new task to the task list
        pass

if __name__ == '__main__':
    SABMUSApp().run()
