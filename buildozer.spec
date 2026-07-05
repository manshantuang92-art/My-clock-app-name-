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
presplash.filename = %(source.dir)s/blank.png
android.presplash_color = #1A1A1A
[buildozer]
log_level = 2
warn_on_root = 0
