# Minecraft Server Menu
[msm.py](https://github.com/DizzyThermal/minecraft_server_menu/blob/master/msm.py) is a small script to scan worlds in Minecraft Server Directory and hotswap worlds before launch.

**Things to Note:**
* There is no warranty for this - Read the License (15. Disclaimer of Warranty.) - TL;DR: Don't complain if your server.properties file is destroyed or your computer catches on fire (or something else - lawyered).
* [**_GAME_DIR**](https://github.com/DizzyThermal/minecraft_server_menu/blob/master/msm.py#L7) must point to the directory where your Minecraft Server JAR is.
* Worlds must be prefixed with the value of [**_DIR_PREFIX**](https://github.com/DizzyThermal/minecraft_server_menu/blob/master/msm.py#L10) to be detected (go ahead, change this if you want - in the code that is...)
* Out-of-the-Box, this code _also_ assumes the following:
    * Your Minecraft Server JAR File matches this pattern:  **^minecraft_server.\*jar$**
    * server.properties file **exists** and contains a line matching: **^level_name=world-.\*$**
    * **server.properties** file is side-by-side with **^minecraft_server.\*jar$**
    * A world ALREADY exists side-by-side with **^minecraft_server.\*jar$** and **server.properties**
        * This world matches: **^world-.\*$**
    * Python 2.x installed (for msm.py)
    * Java 1.7 or higher is installed (and on PATH) (for Minecraft)
    * A Windows Environment (may work for Linux, but haven't tried)

* This code is **NOT** bullet-proof code. This works for my _current_ setup.

**Back Story:**

I have a few friends that I play Minecraft with, we'll call them John and Sally. When I want to play with John, I would have to edit my server's properties file to point to John's world. When I want to play with Sally, I would have to edit my server's properties file to point to Sally's world. There must be a simpler way... MSM.

MSM edits server.properties with the option I choose and launches the server.

### Ideal World Setup
```
C:\Path\To\Minecraft\Server\Dir
   ...\world-John
   ...\world-Sally
```

### Interface
```
Worlds:
[1] John
[2] Sally

Start which world?:
```

**[pr0tip]:** For Windows, make a Shortcut with the following:

```C:\Windows\System32\cmd.exe /c "python.exe C:\Path\To\msm.py"```

_(assumes python.exe is on your path)_

**Computer on fire? Good.**