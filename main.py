from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Line
from kivy.uix.widget import Widget
import time
import math

class AnimatedClockWidget(Widget):
    """ အသက်ဝင်ပြီး တရွေ့ရွေ့ လှည့်ပတ်နေမယ့် နာရီစနစ် """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.angle = 0
        Clock.schedule_interval(self.update_clock, 0.05)  # အရမ်းချောမွေ့အောင် ခပ်မြန်မြန်လှည့်ခြင်း

    def update_clock(self, *args):
        # နာရီလက်တံကို တရွေ့ရွေ့ လှည့်ပတ်စေခြင်း
        self.angle -= 5  
        self.canvas.clear()
        
        with self.canvas:
            # နာရီဝိုင်းပုံ ဆွဲခြင်း
            Color(1, 1, 1, 1)  
            Line(circle=(self.center_x, self.center_y, 150), width=3)
            
            # စက္ကန့်တံ (တရွေ့ရွေ့ လှည့်နေသော အဝါရောင်လက်တံ)
            Color(1, 0.8, 0.2, 1)
            rad = math.radians(self.angle)
            x = self.center_x + 130 * math.sin(rad)
            y = self.center_y + 130 * math.cos(rad)
            Line(points=[self.center_x, self.center_y, x, y], width=2)

class ClockApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        self.main_layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        # === ပထမအဆင့်- Loading စာသားနှင့် လှည့်နေသောနာရီကို ပြသခြင်း ===
        self.loading_label = Label(text="LOADING...", font_size='24sp', bold=True, color=(0.2, 0.6, 1, 1))
        self.animated_clock = AnimatedClockWidget()
        
        self.main_layout.add_widget(self.loading_label)
        self.main_layout.add_widget(self.animated_clock)

        # ၃ စက္ကန့်ပြည့်ရင် တကယ့် ဒီဂျစ်တယ်နာရီမျက်နှာပြင်ဆီ ကူးပြောင်းရန် ညွှန်ကြားခြင်း
        Clock.schedule_once(self.switch_to_digital_clock, 3)

        return self.main_layout

    def switch_to_digital_clock(self, *args):
        # Loading မျက်နှာပြင်ကို ဖျက်ပစ်ခြင်း
        self.main_layout.clear_widgets()

        # === ဒုတိယအဆင့်- တကယ့် ဒီဂျစ်တယ်နာရီ မျက်နှာပြင်ကို ပြသခြင်း ===
        self.title_label = Label(text="MY DIGITAL CLOCK", font_size='24sp', bold=True, color=(0.2, 0.6, 1, 1))
        self.time_label = Label(text="00:00:00 AM", font_size='48sp', bold=True, color=(1, 0.8, 0.2, 1))

        self.main_layout.add_widget(self.title_label)
        self.main_layout.add_widget(self.time_label)

        # ပုံမှန် တစ်စက္ကန့်ချင်း အချိန် Update လုပ်ခြင်းစနစ်ကို စတင်ခြင်း
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, *args):
        current_time = time.strftime("%I:%M:%S %p")
        self.time_label.text = current_time

if __name__ == "__main__":
    ClockApp().run()
