# 移动端设备 + 包信息
desired_caps = {
    # 被测手机是安卓 + 手机安卓版本
    'platformName': 'Android',
    'platformVersion': '',

    # 设备名，安卓手机可以随意填写 + 启动APP Package名称 + 启动Activity名称
    'deviceName': '当贝家',
    'appPackage': 'com.dangbei.remotecontroller',
    'appActivity': '.ui.splash.SplashActivity',

    # 使用自带输入法，输入中文时填True + 执行完程序恢复原来输入法
    'unicodeKeyboard': True,
    'resetKeyboard': True,

    # 不要重置App + 等待超时时间
    'noReset': True,
    'newCommandTimeout': 6000,
    'automationName': 'UiAutomator2',

    # 账号密码
    'unlockType': 'password',
    'unlockKey': '111111'

}


