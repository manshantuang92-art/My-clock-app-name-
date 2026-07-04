import time
import os

# အရောင် Code များ သတ်မှတ်ခြင်း
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def display_clock():
    # Screen ကို အမြဲရှင်းလင်းနေစေရန်
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{YELLOW}================================={RESET}")
    print(f"{BLUE}        MY DIGITAL CLOCK         {RESET}")
    print(f"{YELLOW}================================={RESET}")
    print("\n")

    while True:
        try:
            # လက်ရှိအချိန်ကို ရယူခြင်း
            current_time = time.localtime()
            hour = current_time.tm_hour
            minute = current_time.tm_min
            second = current_time.tm_sec

            # AM / PM ခွဲခြားခြင်း
            am_pm = "AM" if hour < 12 else "PM"
            
            # 12-hour format သို့ ပြောင်းလဲခြင်း
            display_hour = hour % 12
            if display_hour == 0:
                display_hour = 12

            # အချိန်ကို တစ်ကြောင်းတည်းမှာပဲ အမြဲတမ်း Update ဖြစ်နေစေရန် \r သုံးထားပါတယ်
            print(f"\r{YELLOW}လက်ရှိအချိန် - {RESET}{BLUE}{display_hour:02d}:{minute:02d}:{second:02d} {am_pm}{RESET}  (ထွက်ချင်လျှင် Ctrl+C နှိပ်ပါ)", end="", flush=True)
            
            # ၀.၁ စက္ကန့်တိုင်း အချိန်ကို စစ်ဆေးပေးခြင်း
            time.sleep(0.1)
            
        except KeyboardInterrupt:
            # အသုံးပြုသူက ထွက်ချင်တဲ့အခါ
            print(f"\n\n{YELLOW}နာရီပရိုဂရမ်ကို ပိတ်လိုက်ပါပြီ။ သာယာသောနေ့လေးဖြစ်ပါစေဗျာ!{RESET}\n")
            break

if __name__ == "__main__":
    display_clock()