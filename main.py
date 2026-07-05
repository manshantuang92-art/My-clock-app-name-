from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Line, Rectangle
from kivy.core.text import Label as CoreLabel
import time
import math

class PerfectAnimatedClock(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.angle = 0
        self.show_clock = False
        self.bind(pos=self.draw_clock, size=self.draw_clock)
        
        # App စပွင့်ချင်း ၁.၅ စက္ကန့်အထိ အမည်းရောင်မျက်နှာပြင်ပဲ ပြထားပြီး၊ ပြီးမှ နာရီဝိုင်းကို ဖော်ပြရန်
        Clock.schedule_once(self.activate_clock, 1.5)
        Clock.schedule_interval(self.update_angle, 0.05)

    def activate_clock(self, *args):
        self.show_clock = True
        self.draw_clock()

    def update_angle(self, *args):
        if self.show_clock:
            self.angle -= 3
            self.draw_clock()

    def draw_clock(self, *args):
        self.canvas.clear()
        
        # Layout ရဲ့ ဗဟိုချက်ကို တွက်ချက်ခြင်း
        cx = self.center_x
        cy = self.center_y - 50
        radius = 220
        
        with self.canvas:
            # နောက်ခံကို အမည်းရောင်အပြည့် အမြဲဖုံးအုပ်ထားခြင်း (Kivy Logo ပေါ်လာပါက ဖျောက်ရန်)
            Color(0.1, 0.1, 0.1, 1)
            Rectangle(pos=self.pos, size=self.size)
            
            # ၁.၅ စက္ကန့်ပြည့်မှ နာရီဝိုင်းနှင့် နံပါတ်များကို ဆွဲခြင်း
            if self.show_clock:
                # အပြင်ဘက် နာရီအဝိုင်းကြီး
                Color(1, 1, 1, 1)
                Line(circle=(cx, cy, radius), width=4)
                
                # ဗဟိုချက် အစက်
                Line(circle=(cx, cy, 5), width=5)
                
                # နာရီနံပါတ် (၁ မှ ၁၂) ဆွဲခြင်း
                for i in range(1, 13):
                    angle_rad = math.radians(i * 30)
                    nx = cx + (radius - 40) * math.sin(angle_rad)
                    ny = cy + (radius - 40) * math.cos(angle_rad)
                    
                    core_label = CoreLabel(text=str(i), font_size=24, bold=True)
                    core_label.refresh()
                    texture = core_label.texture
                    texture_size = texture.size
                    
                    Color(1, 1, 1, 1)
                    Rectangle(texture=texture, pos=(nx - texture_size[0]/2, ny - texture_size[1]/2), size=texture_size)
                
                # တရွေ့ရွေ့ လှည့်ပတ်နေမယ့် စက္ကန့်တံ (အဝါရောင်)
                Color(1, 0.8, 0.2, 1)
                rad_hand = math.radians(self.angle)
                hand_x = cx + (radius - 20) * math.sin(rad_hand)
                hand_y = cy + (radius - 20) * math.cos(rad_hand)
                Line(points=[cx, cy, hand_x, hand_y], width=3)

class ClockApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        
        self.main_layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        # Loading စာသား (နာရီဝိုင်းပေါ်လာမှ အတူတူပြရန် ကနဦးတွင် စာသားမထည့်ထားပါ)
        self.loading_label = Label(
            text="", 
            font_size='30sp', 
            bold=True, 
            color=(0.2, 0.6, 1, 1),
            size_hint_y=0.15
        )
        
        self.animated_clock = PerfectAnimatedClock(size_hint_y=0.85)
        
        self.main_layout.add_widget(self.loading_label)
        self.main_layout.add_widget(self.animated_clock)

        # ၁.၅ စက္ကန့်ပြည့်ရင် LOADING... စာသား ဖော်ပြရန်
        Clock.schedule_once(self.show_loading_text, 1.5)
        
        # ၄.၅ စက္ကန့်ပြည့်လျှင် တကယ့် ဒီဂျစ်တယ်နာရီဆီ ကူးပြောင်းရန်
        Clock.schedule_once(self.switch_to_digital_clock, 4.5)

        return self.main_layout

    def show_loading_text(self, *args):
        self.loading_label.text = "LOADING..."

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
