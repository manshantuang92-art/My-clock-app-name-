[app]
title = My Clock App
package.name = clockapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.11,kivy==2.3.0,pillow
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a
android.accept_sdk_license = True
android.api = 33
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 0
