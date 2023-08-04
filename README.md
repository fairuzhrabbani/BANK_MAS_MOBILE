# Automation Mobile
Automation Mobile [FDroid] Version 13.3.2 with Python

## What will the test do?
- Create Task
- Edit Task
- Completed Task
- Delete Task

## Tech

- [Python] - Python is used successfully in thousands of real-world business applications around the world
- [Vysor] - For Emulator Real Device
- [Pytest] - The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries
- [PyCharm] - The Python IDE for Professional Developers
- [NodeJs] - Node.js® is an open-source, cross-platform JavaScript runtime environment.
- [Appium Desktop] - Appium is used mostly in the field of software test automation
- [Appium Command-Line]
- [Appium Inspector] - A GUI inspector for mobile apps and more, powered by a (separately installed) Appium server
- [Java] - Java is a programming language and computing platform first released by Sun Microsystems in 1995
- [Android Studio] -Get the official Integrated Development Environment (IDE) for Android app development.
## Installation

Download & Install [Python](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe) 3.11.4.
Check Python version in cmd
```sh
python --version
Python 3.11.4
```
Download & Install [PyCharm]
Install Python [Pytest] di cmd
```sh
pip install pytest
```
Install Python [Appium-Python-Client] di cmd
```sh
pip install Appium-Python-Client==0.38
```
Check Packages in cmd has been done 
```sh
pip list
```
Create ANDROID_HOME and JAVA_HOME in Environment variables - System variables
Click Path -> Edit -> New -> path folder 'platform-tools' android sdk

## Development
1. Open Android Studio and install SDK Version
2. Open Appium desktop -> edit configuration and input path ANDROID_HOME and JAVA_HOME
3. Connect your smartphone - USB
4. Open cmd and input adb device
```sh
adb devices
```
List of devices attached is connected
5. Input appium
```sh
appium 
```
Appium server is running
6. Open Appium Inspector and create Desired Capabilites
```sh
{
  "appium:appPackage": "org.tasks",
  "appium:appActivity": "com.todoroo.astrid.activity.TaskListActivity",
  "platformName": "Android",
  "appium:deviceName": "Galaxy S10+",
  "appium:udid": "RR8M3026JMJ",
  "automationName": "UiAutomator2"
}
```
7. Click Start Session and smartphone will be open application FDroid
8. Inspect Element
9. Open PyCharm
10. Run Script in terminal
```sh
pytest -v testcases\test_fdroid.py  
```


   [Python]: <https://www.python.org/>
   [Request]: <https://pypi.org/project/requests/>
   [Pytest]: <https://pypi.org/project/pytest/>
   [PyCharm]: <https://www.jetbrains.com/pycharm/>
   [ToDoList]: <https://todomvc.com/examples/knockoutjs/>
   [Allure]: <https://pypi.org/project/allure-pytest/>
   [FDroid]: <https://f-droid.org/en/packages/org.tasks/>
   [Vysor]: <https://www.vysor.io/>
   [Appium Desktop]: <https://github.com/appium/appium-desktop/releases>
   [Appium Inspector]: <https://github.com/appium/appium-inspector>
   [NodeJs]: <https://nodejs.org/en>
   [Java]: <https://www.java.com/en/>
   [Android Studio]: <https://developer.android.com/studio?gclid=CjwKCAjww7KmBhAyEiwA5-PUSpvyumHKHmlYYArPjTx4-nI1la5m1TEADPsxsSYXxObFbi8J-NtLNRoCLfgQAvD_BwE&gclsrc=aw.ds>
   [Appium-Python-Client]: <https://pypi.org/project/Appium-Python-Client/0.38/>
