FROM python:3.11-slim

WORKDIR /app

# تثبيت المكاتب
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ ملف السورس
COPY main.py .

# مجلد البيانات (جلسة + إعدادات)
VOLUME /app/data

# متغيرات البيئة (تعبأ من لوحة التحكم)
ENV STRING_SESSION=""
ENV API_ID=""
ENV API_HASH=""

# تشغيل البوت
CMD ["python", "-u", "main.py"]
