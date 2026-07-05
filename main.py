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
    """ ပိုမိုကြီးမားပြီး နံပါတ်များပါဝင်သော အသက်ဝင်နာရီစနစ် """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.angle = 0
        self.bind(pos=self.update_clock, size=self.update_clock)
        Clock.schedule_interval(self.update_clock, 0.05)  # ချောမွေ့စွာ လှည့်ပတ်ရန်

    def update_clock(self, *args):
        self.canvas.clear()
        
        # နာရီအဝိုင်းရဲ့ အချင်းဝက် (Radius) ကို ၂၂၀ အထိ ပိုကြီးအောင် လုပ်ထားပါတယ်
        radius = 220 
        
        with self.canvas:
            # ၁။ အပြင်ဘက် နာရီအဝိုင်းကြီးဆွဲခြင်း (အဖြူရောင်)
            Color(1, 1, 1, 1)  
            Line(circle=(self.center_x, self.center_y, radius), width=4)
            
            # ၂။ နာရီဗဟိုချက် အစက်ကလေးဆွဲခြင်း
            Line(circle=(self.center_x, self.center_y, 5), width=5)
            
            # ၃။ နာရီအကွက်အမှတ်အသားများနှင့် နံပါတ်များနေရာချခြင်း
            for i in range(1, 13):
                # နာရီတစ်ခုချင်းစီရဲ့ တင်ပြမည့် Angle ကိုတွက်ချက်ခြင်း
                angle_deg = i * 30  
                rad_num = math.radians(angle_deg)
                
                # နံပါတ်စာတန်းများအတွက် ကိုဩဒိနိတ်တွက်ချက်ခြင်း
                # နာရီဝိုင်းအတွင်းဘက် အံဝင်ခွင်ကျဖြစ်အောင် အချင်းဝက်ကို ၁၈၀ လောက်ပဲ သုံးထားပါတယ်
                num_x = self.center_x + (radius - 40) * math.sin(rad_num)
                num_y = self.center_y + (radius - 40) * math.cos(rad_num)
                
                # Widget အနေနဲ့ စာသားတွေကို နာရီဝိုင်းထဲ ထည့်သွင်းခြင်း
                # (ပထမအကြိမ်တွင် သို့မဟုတ် တည်နေရာပြောင်းလျှင် Label ဆောက်ပေးရန်)
                # သတိပြုရန် - ကနဦး Canvas ပေါ်တွင် Label တိုက်ရိုက်ဆွဲရန် စာသား Label Widget ကို သုံးပါမည်
                
            # ၄။ တရွေ့ရွေ့လှည့်နေမယ့် စက္ကန့်တံ (အဝါရောင်လက်တံ)
            self.angle -= 3  # လှည့်နှုန်းကို အနည်းငယ် ပိုမှန်အောင် ညှိထားပါတယ်
            Color(1, 0.8, 0.2, 1)
            rad_hand = math.radians(self.angle)
            hand_x = self.center_x + (radius - 20) * math.sin(rad_hand)
            hand_y = self.center_y + (radius - 20) * math.cos(rad_hand)
            Line(points=[self.center_x, self.center_y, hand_x, hand_y], width=3)

class ClockApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        
        # အဓိက Layout အပြင်အဆင်
        self.main_layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

        # === Loading မျက်နှာပြင်ပြသခြင်း ===
        self.loading_label = Label(
            text="LOADING...", 
            font_size='28sp', 
            bold=True, 
            color=(0.2, 0.6, 1, 1),
            size_hint_y=0.2
        )
        
        # နာရီဝိုင်းကြီး ပေါ်လာမည့် နေရာ
        self.animated_clock = AnimatedClockWidget(size_hint_y=0.8)
        
        # နံပါတ်တွေကို နာရီဝိုင်းထဲမှာ စာသား Label တွေအနေနဲ့ ဖြန့်ခင်းပေးခြင်း
        # အလှဆင်ရန်အတွက် နာရီဝိုင်းထဲတွင် နံပါတ်စာသားလေးများ ထည့်သွင်းရန် Layout တစ်ခု သပ်သတ်သုံးခြင်း
        self.clock_box = Widget()
        self.clock_box.add_widget(self.animated_clock)
        
        # နံပါတ် (၁ မှ ၁၂) အထိကို နာရီပတ်ပတ်လည် ပေါ်အောင် စာသားများ ထည့်သွင်းခြင်း
        Clock.schedule_once(self.add_clock_numbers, 0.1)

        self.main_layout.add_widget(self.loading_label)
        self.main_layout.add_widget(self.clock_box)

        # ၄ စက္ကန့်ပြည့်လျှင် တကယ့် ဒီဂျစ်တယ်နာရီဆီ ပြောင်းရန်
        Clock.schedule_once(self.switch_to_digital_clock, 4)

        return self.main_layout

    def add_clock_numbers(self, *args):
        # နာရီဗဟိုချက်ကို ယူခြင်း
        cx = self.animated_clock.center_x
        cy = self.animated_clock.center_y
        radius = 220
        
        for i in range(1, 13):
            angle_rad = math.radians(i * 30)
            # နံပါတ်နေရာများ တွက်ချက်ခြင်း
            nx = cx + (radius - 40) * math.sin(angle_rad) - 15
            ny = cy + (radius - 40) * math.cos(angle_rad) - 15
            
            num_label = Label(
                text=str(i),
                font_size='22sp',
                bold=True,
                color=(1, 1, 1, 1),
                pos=(nx, ny),
                size=(30, 30)
            )
            self.clock_box.add_widget(num_label)

    def switch_to_digital_clock(self, *args):
        # Loading တစ်ခုလုံးကို ရှင်းလင်းပစ်ခြင်း
        self.main_layout.clear_widgets()

        # === တကယ့် ဒီဂျစ်တယ်နာရီ မျက်နှာပြင် ===
        self.title_label = Label(text="MY DIGITAL CLOCK", font_size='26sp', bold=True, color=(0.2, 0.6, 1, 1))
        self.time_label = Label(text="00:00:00 AM", font_size='54sp', bold=True, color=(1, 0.8, 0.2, 1))

        self.main_layout.add_widget(self.title_label)
        self.main_layout.add_widget(self.time_label)

        # အချိန်ပုံမှန် Update လုပ်ခြင်း
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, *args):
        current_time = time.strftime("%I:%M:%S %p")
        self.time_label.text = current_time

if __name__ == "__main__":
    ClockApp().run()
