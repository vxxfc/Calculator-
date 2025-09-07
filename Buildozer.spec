[app]

# (str) Title of your application
title = Calculator

# (str) Package name
package.name = calculator

# (str) Package domain (must be unique)
package.domain = org.yourname

# (str) Source code where main.py lives
source.dir = .

# (str) The main .py file
source.main = calculator.py

# (list) Permissions your app needs (empty for calculator)
android.permissions = INTERNET

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Application requirements
# Kivy is required to run the UI
requirements = python3,kivy

# (str) Application versioning
version = 1.0.0

# (str) Application entry point
entrypoint = calculator.py

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Package format: apk or aab (Google Play requires aab)
package.format = apk

# (list) Presplash image (optional)
# presplash.filename = %(source.dir)s/data/presplash.png

# (list) Icon image (optional)
# icon.filename = %(source.dir)s/data/icon.png


[buildozer]

# (int) log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (bool) use the same build directory across builds
use_current_build = 0

# (str) Path to build output
build_dir = .buildozer

# (bool) Copy .apk to bin directory after build
copy_to_bin = 1
