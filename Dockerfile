# 使用 Python 3.10.12 Alpine 作為基礎映像
FROM python:3.10.12-alpine as build

# 設置工作目錄
WORKDIR /app

# 複製需求文件到容器中
COPY requirements.txt .

# 設置時區
ENV TZ=Asia/Taipei

# 安裝依賴項
RUN pip install --no-cache-dir -r requirements.txt

# 開port
EXPOSE 5001

# # 複製應用程式代碼到容器中 由 docker-compose volume 進來就不用複製進來
# COPY . .

# 指定容器啟動命令
CMD ["python", "main.py"]
