[app]
title = My Clock App
package.name = clockapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,pillow
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
#presplash.filename = "" (Kivy Logo ကြီး ပိတ်ရန်)
android.presplash_color = #1A1A1A (နောက်ခံအမည်းရောင်ထားရန်)
[buildozer]
log_level = 2
warn_on_root = 0
