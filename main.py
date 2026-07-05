from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
import time

class ClockApp(App):
    def build(self):
        # နောက်ခံအရောင်ကို မီးခိုးရင့်ရောင် သတ်မှတ်ခြင်း
        Window.clearcolor = (0.1, 0.1, 0.1, 1)

        # အပြင်အဆင် Layout ဆောက်ခြင်း
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        # ခေါင်းစဉ်စာသား
        self.title_label = Label(
            text="MY DIGITAL CLOCK",
            font_size='24sp',
            bold=True,
            color=(0.2, 0.6, 1, 1)  # အပြာနုရောင်
        )

        # အချိန်ပြမည့် စာသား
        self.time_label = Label(
            text="00:00:00 AM",
            font_size='48sp',
            bold=True,
            color=(1, 0.8, 0.2, 1)  # အဝါရောင်
        )

        layout.add_widget(self.title_label)
        layout.add_widget(self.time_label)

        # တစ်စက္ကန့်တိုင်း အချိန်ကို Update လုပ်ပေးရန် ညွှန်ကြားခြင်း
        Clock.schedule_interval(self.update_time, 1)

        return layout

    def update_time(self, *args):
        # လက်ရှိအချိန်ကို ရယူပြီး ပုံစံဖော်ခြင်း (ဥပမာ - 11:26:19 PM)
        current_time = time.strftime("%I:%M:%S %p")
        self.time_label.text = current_time

if __name__ == "__main__":
    ClockApp().run()
