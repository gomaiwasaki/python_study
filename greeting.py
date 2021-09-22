import datetime
now = datetime.datetime.now()

class Greeting:
    if now.hour <= 9:
        print("おはようございます！いい朝ですね！")
    elif now.hour < 18:
        print("こんにちは！")
    elif now.hour > 18:
        print("こんばんは！お疲れ様です！")
    else:
        print("夜遅くまでお疲れ様です")
    print("ただ今の時刻は", now.hour, "時", now.minute, "分", now.second, "秒です！", sep="")