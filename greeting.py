# 時刻をお知らせし、挨拶する
def greeting():
    import datetime, time
    # 現在の日付や時刻を変数nowに代入する
    now = datetime.datetime.now()

    # 現在の時間によって違った文章が表示される
    if now.hour <= 9:
        print("おはようございます！いい朝ですね！")
    elif now.hour < 18:
        print("こんにちは！")
    elif now.hour > 18:
        print("こんばんは！お疲れ様です！")
    else:
        print("夜遅くまでお疲れ様です")

    # 現在の時刻を表示する
    print("ただ今の時刻は", now.hour, "時", now.minute, "分", now.second, "秒です！", sep="")
    time.sleep(2)
    print("時刻機能を終了します")
