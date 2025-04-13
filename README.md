# ёRadio
<img src="images/yologo.png" width="190" height="142">

#### Youradio fork adopted to platformio instead of arduino ide.

The original project is located here: https://github.com/e2002/yoradio

#### Quick start guide

Prerequesties:

- installed Visual Studio Code
- installed Platformio
- prepared myoptions.h by the simple myoptions generator: https://e2002.github.io/docs/myoptions-generator.html (the codebase will work only on the WROOM module, if you have WVOVER - please adopt the platformio.ini)

How-to:

- Open Workspace from file... yoradio.code-workspace
- Wait until vscode / platformio prepare the workspace (download dependencies)
- Place/replace your myoptions.h under existing yoRadio/src/myoptions.h
- Now build the firmware
- Maybe you need also to build and upload the SPIFFS image (via the platformio menu - Build Filesystem image, Uoload Filesystem image)
- Upload the firmware into the board using platformio

