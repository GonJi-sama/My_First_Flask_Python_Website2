การสร้างไฟล์แอปพลิเคชัน Flask
สร้างไฟล์ Python ชื่อ app.py (หรือชื่ออื่น ๆ เช่น hello.py) และเพิ่มโค้ด Flask พื้นฐาน:

app.py
Python

from flask import Flask

# สร้างอินสแตนซ์ของ Flask
app = Flask(__name__)

# กำหนด Route สำหรับหน้าแรก (/)
@app.route("/")
def hello_world():
    # ฟังก์ชันนี้จะถูกเรียกเมื่อมีคนเข้าถึง URL หลัก
    return "<p>Hello, World! This is a simple Flask app.</p>"

# หากต้องการให้รันได้โดยตรงเมื่อเรียกใช้ไฟล์
if __name__ == '__main__':
    app.run(debug=True)

การรันแอปพลิเคชัน
เมื่ออยู่ใน Virtual Environment แล้ว ให้รันแอปพลิเคชันด้วยคำสั่ง:

ตั้งค่าตัวแปรสภาพแวดล้อม (สำหรับ Flask CLI):

macOS / Linux:

Bash

export FLASK_APP=app.py
export FLASK_ENV=development # เปิดโหมด debug (แนะนำสำหรับการพัฒนา)
Windows (Command Prompt):

Bash

set FLASK_APP=app.py
set FLASK_ENV=development
รัน Flask:

Bash

flask run
แอปพลิเคชันจะรันที่ URL คล้ายกับ http://127.0.0.1:5000/ หรือ http://localhost:5000/ คุณสามารถเปิด URL นี้ในเบราว์เซอร์เพื่อดูข้อความ "Hello, World! This is a simple Flask app."