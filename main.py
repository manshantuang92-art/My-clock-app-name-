from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Line
from kivy.uix.widget import Widget
import time
import math

class AnimatedClockWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.angle = 0
        # Layout ဆွဲပြီးမှ ဗဟိုချက်ကို တွက်ချက်ရန် တန်ဖိုးပတ်သက်မှုများကို Bind လုပ်ခြင်း
        self.bind(pos=self.draw_clock, size=self.draw_clock)
        Clock.schedule_interval(self.update_angle, 0.05)

    def update_angle(self, *args):
        self.angle -= 3
        self.draw_clock()

    def draw_clock(self, *args):
        self.canvas.clear()
        
        # နာရီဝိုင်းအရွယ်အစား (Radius)
        radius = 200
        # Widget ရဲ့ ဗဟိုချက်ကို တိတိကျကျ ရယူခြင်း
        cx = self.x + self.width / 2
        cy = self.y + self.height / 2
        
        with self.canvas:
            # ၁။ အပြင်ဘက် နာရီအဝိုင်းကြီး (အဖြူရောင်)
            Color(1, 1, 1, 1)
            Line(circle=(cx, cy, radius), width=4)
            
            # ၂။ နာရီဗဟိုချက် အစက်
            Line(circle=(cx, cy, 5), width=5)
            
            # ၃။ တရွေ့ရွေ့လှည့်နေမယ့် စက္ကန့်တံ (အဝါရောင်လက်တံ)
            Color(1, 0.8, 0.2, 1)
            rad_hand = math.radians(self.angle)
            hand_x = cx + (radius - 20) * math.sin(rad_hand)
            hand_y = cy + (radius - 20) * math.cos(rad_hand)
            Line(points=[cx, cy, hand_x, hand_y], width=3)

class ClockApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        
        # ပင်မ Layout
        self.main_layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

        # Loading စာသား
        self.loading_label = Label(
            text="LOADING...", 
            font_size='28sp', 
            bold=True, 
            color=(0.2, 0.6, 1, 1),
            size_hint_y=0.2
        )
        
        # နာရီဝိုင်းနဲ့ နံပါတ်တွေကို Screen အလယ်မှာ ကွက်တိနေရာချဖို့ RelativeLayout သုံးခြင်း
        self.clock_container = RelativeLayout(size_hint_y=0.8)
        self.animated_clock = AnimatedClockWidget()
        
        self.clock_container.add_widget(self.animated_clock)
        
        # နံပါတ် (၁ မှ ၁၂) ကို အလယ်တည့်တည့်မှာ ဝိုင်းပတ်ပေါ်လာစေရန် ခေါ်ယူခြင်း
        Clock.schedule_once(self.add_clock_numbers, 0.1)

        self.main_layout.add_widget(self.loading_label)
        self.main_layout.add_widget(self.clock_container)

        # ၄ စက္ကန့်ပြည့်လျှင် တကယ့် ဒီဂျစ်တယ်နာရီဆီ ပြောင်းရန်
        Clock.schedule_once(self.switch_to_digital_clock, 4)

        return self.main_layout

    def add_clock_numbers(self, *args):
        # Container ရဲ့ ဗဟိုချက်ကို တွက်ချက်ခြင်း
        cx = self.clock_container.width / 2
        cy = self.clock_container.height / 2
        radius = 200
        
        for i in range(1, 13):
            angle_rad = math.radians(i * 30)
            # စာသား Label ရဲ့ ဗဟိုချက်ကို ညှိရန် -25 နဲ့ -25 နှုတ်ပေးထားပါတယ်
            nx = cx + (radius - 40) * math.sin(angle_rad) - 25
            ny = cy + (radius - 40) * math.cos(angle_rad) - 25
            
            num_label = Label(
                text=str(i),
                font_size='24sp',
                bold=True,
                color=(1, 1, 1, 1),
                pos=(nx, ny),
                size_hint=(None, None),
                size=(50, 50)
            )
            self.clock_container.add_widget(num_label)

    def switch_to_digital_clock(self, *args):
        self.main_layout.clear_widgets()

        # === တကယ့် ဒီဂျစ်တယ်နာရီ မျက်နှာပြင် ===
        self.title_label = Label(text="MY DIGITAL CLOCK", font_size='26sp', bold=True, color=(0.2, 0.6, 1, 1))
        self.time_label = Label(text="00:00:00 AM", font_size='54sp', bold=True, color=(1, 0.8, 0.2, 1))

        self.main_layout.add_widget(self.title_label)
        self.main_layout.add_widget(self.time_label)

        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, *args):
        current_time = time.strftime("%I:%M:%S %p")
        self.time_label.text = current_time

if __name__ == "__main__":
    ClockApp().run()
