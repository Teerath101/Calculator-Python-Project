## Building a Calculator Application using Python

Problem faced-<br/>

The first problem I faced was with Tkinter showing depreciated when I tried to run the simple main window command.<br/>
After some searching, I found out that it this warning means that my Tkinter installed was outdated.<br/>

Solution - <br/>
Update the Tkinter via Homebrew-<br/>
```bash
brew install tcl-tk
```
<br/>
Get into the Nano text editor on the terminal by running-<br/>
```bash
nano ~/.zshrc
```
<br/>
If permission is denied, it uses sudo <br/>
```bash
sudo nano ~/.zshrc
```
Add the Environmental Variable -<br/>
```bash
export PATH="/usr/local/opt/tcl-tk/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/tcl-tk/lib"
export CPPFLAGS="-I/usr/local/opt/tcl-tk/include"
export PKG_CONFIG_PATH="/usr/local/opt/tcl-tk/lib/pkgconfig"
export TK_SILENCE_DEPRECATION=1
```
<br/>
Save the Changes using Ctrl + O and Enter to Confirm. and Press Ctrl + X to exit the Nano Editor




