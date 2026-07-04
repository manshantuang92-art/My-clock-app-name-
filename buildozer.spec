[app]
title = My Clock App
package.name = clockapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# ဗားရှင်းကို အသေမသတ်မှတ်ဘဲ Buildozer အလိုအလျောက် ချိန်ညှိခိုင်းခြင်း
requirements = python3,kivy,pillow

orientation = portrait
fullscreen = 1

android.archs = arm64-v8a
android.accept_sdk_license = True
android.api = 33

[buildozer]
log_level = 2
warn_on_root = 0
