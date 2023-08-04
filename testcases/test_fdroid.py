import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

"""
Desired Capabilities
"""

capabilities = {
    "appium:appPackage": "org.tasks",
    "appium:appActivity": "com.todoroo.astrid.activity.TaskListActivity",
    "platformName": "Android",
    "appium:deviceName": "Galaxy S10+",
    "appium:udid": "RR8M3026JMJ",
    "appium:automationName": "UiAutomator2",
    "appium:ensureWebviewsHavePages": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
}

# 1. Task
def test_membuat_task():
    appium_server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(appium_server_url, capabilities)
    driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Create new task"]').click()
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText').click()
    tasktitle = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText')
    tasktitle.send_keys("Membuat Task")
    driver.find_element(By.ID, 'org.tasks:id/task_edit_start_date').click()
    driver.find_element(By.XPATH, '//android.view.View[@content-desc="04 August 2023"]').click()
    driver.find_element(By.ID, 'org.tasks:id/ok_button').click()
    driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Save"]').click()
    actual_taskname = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView').text
    expected_taskname = 'Membuat Task'
    # Verify
    assert actual_taskname == expected_taskname, "Task name isn't match"

# 2 Task
def test_mengedit_task():
    appium_server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(appium_server_url, capabilities)
    driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Create new task"]').click()
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText').click()
    tasktitle = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText')
    tasktitle.send_keys("Besok ada meeting")
    driver.find_element(By.ID, 'org.tasks:id/task_edit_start_date').click()
    driver.find_element(By.XPATH, '//android.view.View[@content-desc="04 August 2023"]').click()
    driver.find_element(By.ID, 'org.tasks:id/ok_button').click()
    driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Save"]').click()

    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView').click()
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText').click()
    tasktitle_new = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText')
    tasktitle_new.send_keys("Reschedule Meeting")
    driver.find_element(By.ID, 'org.tasks:id/task_edit_start_date').click()
    driver.find_element(By.XPATH, '//android.view.View[@content-desc="05 August 2023"]').click()
    driver.find_element(By.ID, 'org.tasks:id/ok_button').click()
    driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Save"]').click()
    actual_taskname = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView').text
    expected_taskname = 'Reschedule Meeting'
    # Verify
    assert actual_taskname == expected_taskname, "Task name isn't match"
    driver.quit()

# 3
def test_menyelesaikan_task():
    appium_server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(appium_server_url, capabilities)
    driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Create new task"]').click()
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText').click()
    tasktitle = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText')
    tasktitle.send_keys("Besok ada meeting")
    driver.find_element(By.ID, 'org.tasks:id/task_edit_start_date').click()
    driver.find_element(By.XPATH, '//android.view.View[@content-desc="04 August 2023"]').click()
    driver.find_element(By.ID, 'org.tasks:id/ok_button').click()
    driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Save"]').click()
    # ---
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageView').click()
    actual_taskdone = driver.find_element(By.ID, 'org.tasks:id/snackbar_text').text
    expected_taskdone = 'Task completed'
    # Verify
    assert actual_taskdone == expected_taskdone, "Alert isn't match"
    driver.quit()

# 4
def menghapus_task():
    appium_server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(appium_server_url, capabilities)
    driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Create new task"]').click()
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText').click()
    tasktitle = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText')
    tasktitle.send_keys("Besok ada meeting")
    driver.find_element(By.ID, 'org.tasks:id/task_edit_start_date').click()
    driver.find_element(By.XPATH, '//android.view.View[@content-desc="04 August 2023"]').click()
    driver.find_element(By.ID, 'org.tasks:id/ok_button').click()
    driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Save"]').click()
    # ----
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView').click()
    driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Delete task"]').click()
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]').click()
    actual_delete = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView').text
    expected_delete = 'There are no tasks here.'
    # Verify
    assert actual_delete == expected_delete, "Alert isn't match"
    driver.quit()

