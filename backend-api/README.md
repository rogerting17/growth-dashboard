
# Render 後端更新服務

## 如何部署

1. 登入 https://render.com
2. 建立 Web Service 並連接本 repo
3. 設定：

- Root directory: `backend-api`
- Build command: `pip install -r requirements.txt`
- Start command: `python app.py`
- Environment Variable:
  - `API_TOKEN=YOUR_SECRET_TOKEN`

4. 成功後你會有網址，如：
   `https://your-api.onrender.com/update?token=YOUR_SECRET_TOKEN`
