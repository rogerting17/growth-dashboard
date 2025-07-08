
def run():
    try:
        with open("frontend-cloudflare/data/growth.csv", "w", encoding="utf-8") as f:
            f.write("代號,名稱,24M06 年增率,24M07 年增率\n")
            f.write("2330,台積電,22.3,24.1\n")
            f.write("2317,鴻海,15.1,16.8\n")
        return True
    except Exception as e:
        print("更新失敗:", e)
        return False
