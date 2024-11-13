
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Brodie", "Kevin", "Collins", "Chris"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_labels(self):
        main_layout = self.root.ids.main
        for name in self.names:
            temp_label = Label(text=name)
            main_layout.add_widget(temp_label)


DynamicLabelsApp().run()
