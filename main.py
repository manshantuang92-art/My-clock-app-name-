from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Line
from kivy.graphics.instructions import InstructionGroup
from kivy.core.text import Label as CoreLabel
import time
import math

class PerfectAnimatedClock(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.angle = 0
        self.bind(pos=self.draw_clock, size=self.draw_clock)
        Clock.schedule_interval(self.update_angle, 0.05)

    def update_angle(self, *args):
        self.angle -= 3
        self.draw_clock()

    def draw_clock(self, *args):
        self.canvas.clear()
        
        # နာရီဝိုင်းရဲ့ အရွယ်အစား
        radius = 220
        # Layout ရဲ့ အလယ်ဗဟိုကို တိတိကျကျ ရယူခြင်း
        cx = self.center_x
        cy = self.center_y - 50 # Loading စာသားနဲ့ မညှိအောင် အနည်းငယ် အောက်ချထားခြင်း
        
        with self.canvas:
            # ၁။ အပြင်ဘက် နာရီအဝိုင်းကြီး
            Color(1, 1, 1, 1)
            Line(circle=(cx, cy, radius), width=4)
            
            # ၂။ ဗဟိုချက် အစက်
            Line(circle=(cx, cy, 5), width=5)
            
            # ၃။ နာရီနံပါတ် (၁ မှ ၁၂) ကို Canvas ပေါ်တွင် တိုက်ရိုက်ဆွဲခြင်း (ဘယ်တော့မှ မလွဲစေရန်)
            for i in range(1, 13):
                angle_rad = math.radians(i * 30)
                # နံပါတ်တွေ တည်ရှိမည့်နေရာ တွက်ချက်ခြင်း
                nx = cx + (radius - 40) * math.sin(angle_rad)
                ny = cy + (radius - 40) * math.cos(angle_rad)
                
                # Core Text Render စနစ်ဖြင့် စာသားကို ပုံရိပ်အဖြစ် ပြောင်းလဲခြင်း
                core_label = CoreLabel(text=str(i), font_size=24, bold=True)
                core_label.refresh()
                texture = core_label.texture
                texture_size = texture.size
                
                # စာသားပုံရိပ်ကို အလယ်ဗဟိုတည့်တည့် ရောက်အောင် နေရာချခြင်း
                Color(1, 1, 1, 1)
                from kivy.graphics import Rectangle
                Rectangle(texture=texture, pos=(nx - texture_size[0]/2, ny - texture_size[1]/2), size=texture_size)
            
            # ၄။ တရွေ့ရွေ့ လှည့်ပတ်နေမယ့် စက္ကန့်တံ (အဝါရောင်)
            Color(1, 0.8, 0.2, 1)
            rad_hand = math.radians(self.angle)
            hand_x = cx + (radius - 20) * math.sin(rad_hand)
            hand_y = cy + (radius - 20) * math.cos(rad_hand)
            Line(points=[cx, cy, hand_x, hand_y], width=3)

class ClockApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        
        # ပင်မ Layout
        self.main_layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        # Loading စာသား
        self.loading_label = Label(
            text="LOADING...", 
            font_size='30sp', 
            bold=True, 
            color=(0.2, 0.6, 1, 1),
            size_hint_y=0.15
        )
        
        # အသက်ဝင် နာရီဝိုင်းသစ်ကို Layout ထဲ ထည့်သွင်းခြင်း
        self.animated_clock = PerfectAnimatedClock(size_hint_y=0.85)
        
        self.main_layout.add_widget(self.loading_label)
        self.main_layout.add_widget(self.animated_clock)

        # ၄ စက္ကန့်ပြည့်လျှင် ဒုတိယမျက်နှာပြင်ဆီ ကူးပြောင်းရန်
        Clock.schedule_once(self.switch_to_digital_clock, 4)

        return self.main_layout

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
