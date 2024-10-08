
# Mouse Jiggler

Here is your little buddy *Mouse Jiggler*, which helps to keep your system active like how we coders stay active on caffeine.

![MouseJiggler GIF](https://github.com/user-attachments/assets/9b27860f-d9f0-4254-a591-78be2245c3d3)


- Integrated real-time control through a slider, enabling jiggling interval from 0- 60 seconds.


- Built on __Tkinter__ -> Preferred Python GUI framework for building Desktop application which offers high responsive design with functionality.
    - Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, and is Python's de facto standard GUI.

- Simulating mouse movements -> __PyAutoGUI__ for the duration of the interval set by the user.
    - Python pyautogui library is an automation library that allows mouse and keyboard control. Or we can say that it facilitates us to automate the movement of the mouse and keyboard to establish the interaction with the other application using the Python script.

    - PyAutoGUI has several features:
        - Moving the mouse and clicking in the windows of other applications.
        - Sending keystrokes to applications (for example, to fill out forms).
        - Take screenshots, and given an image (for example, of a button or checkbox), and find it on the screen.
        - Locate an application’s window, and move, resize, maximize, minimize, or close it (Windows-only, currently).
        - Display alert and message boxes.

- __Multi-Threading__ -> The slider automatically runs in a different thread to increase the responsiveness of the application.





## Features

- Can be run as a python script/file for the systems which do not have admin privileges or superuser permissions.
- While executing as a Python program, any system with python installed can run it, making it platform independent or cross platform.
- For quick use of application, without running script, the project also includes a .exe file which runs in Windows machine without privileged access.
- The MouseJiggler.exe file passed the malicious scan test from the Norton Antivirus (which is installed in my local machine) and determined to run without any trouble or issues.






## Authors

- [@Hemanth Kumar A R](https://github.com/arhemanthkumar)


## Badges

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

[![Static Badge](https://img.shields.io/badge/Python-green)](https://www.python.org/)

[![Static Badge](https://img.shields.io/badge/PyAutoGUI-orange)
](https://pyautogui.readthedocs.io/en/latest/#)

[![Static Badge](https://img.shields.io/badge/TKinter-blue)](https://docs.python.org/3/library/tkinter.html)






## Installation

Create a folder to clone the MouseJiggler project repository.

\
Once inside the folder of your choice, you can download the zip folder from the repository or you can clone the repository using:
```bash
git clone https://github.com/arhemanthkumar/Project_MouseJiggler.git
```
Now this will be your working directory, and further commands are valid inside this directory only.

\
Next step is to install the required libraries and dependencies by running:
```bash
pip install -r requirements.txt
```

\
Now you can double click __MouseJiggler.exe__ can directly run it.

\
Or the MouseJiggler can be launched as a python file/script by:
- For Windows Users -->
```bash
python MouseJiggler.py
```
- For Linux / Mac Users -->
```bash
python3 MouseJiggler.py
```

(replace with python2 for older systems.)



## Thank you
