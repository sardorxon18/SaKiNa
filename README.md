# Loyiha Nomi: Sakina

Bu loyiha "Sakina" deb nomlangan va Django veb-ramkasi yordamida yaratilgan. Quyida loyiha katalogining har bir qismi va uning vazifalari keltirilgan.

## Loyiha Strukturasining Tushuntirishi:

### 1. config/
Loyiha konfiguratsiya fayllarini o'z ichiga oladi.
- **\_\_init\_\_.py**: Bu papkani Python moduli sifatida belgilaydi.
- **asgi.py**: Asynchronous Server Gateway Interface konfiguratsiyasi. Bu Django'ni asinxron rejimda ishga tushirish uchun ishlatiladi.
- **settings.py**: Loyiha sozlamalari, ma'lumotlar bazasi sozlamalari, statik fayllar yo'li va boshqa sozlamalar.
- **urls.py**: Loyiha uchun URL yo'nalishlari.
- **wsgi.py**: Web Server Gateway Interface konfiguratsiyasi, loyihani ishlab chiqarish muhiti uchun ishlatiladi.

### 2. pagesapp/
Dastur moduli. Bu yerda loyiha uchun kerakli kodlar mavjud.
- **\_\_init\_\_.py**: Bu papkani Python moduli sifatida belgilaydi.
- **admin.py**: Django admin paneli bilan bog'liq sozlamalar.
- **apps.py**: Dastur konfiguratsiyasi.
- **models.py**: Ma'lumotlar bazasi modellari.
- **tests.py**: Test fayllari.
- **urls.py**: Dastur uchun URL yo'nalishlari.
- **views.py**: Ko'rinishlar. Bu yerda URL yo'nalishlariga javob beruvchi funksiyalar yoziladi.

### 3. static/
Statik fayllar (CSS, JavaScript, rasmlar) saqlanadigan papka.
- **css/**: CSS fayllarini saqlash uchun papka.
    - **style.css**
    - **style1.css**
    - **style2.css**
    - **style3.css**
- **images/**: Rasmlar uchun papka.

### 4. templates/
HTML shablon fayllari saqlanadigan papka.
- **pagesOne/**: `pagesOne` sahifasining shablon fayllari.
    - **basic.html**
- **pagesTwo/**: `pagesTwo` sahifasining shablon fayllari.
    - **HtmlAndCss.html**
    - **salom.html**
    - **simple.html**
- **photo/**: Rasmlar saqlanadigan papka.
- **indexs.html**: Asosiy sahifa shabloni.

### 5. db.sqlite3
SQLite3 ma'lumotlar bazasi fayli. Bu yerda loyiha uchun barcha ma'lumotlar saqlanadi.

### 6. manage.py
Django boshqaruv skripti. Bu skript loyihani boshqarish uchun ishlatiladi (masalan, serverni ishga tushirish, migratsiyalarni qo'llash va boshqalar).

### 7. .idea/
Bu papka PyCharm kabi IDE'lar tomonidan yaratiladi va IDE sozlamalarini o'z ichiga oladi.

## O'rnatish
Loyihani ishga tushirish uchun quyidagi bosqichlarni bajaring:

1. Python 3 va pip o'rnatilganligiga ishonch hosil qiling.
2. Loyihani klonlang:
    ```sh
    git clone <repository-url>
    ```
3. Virtual muhitni yarating va faollashtiring:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate  # Windows
    ```
4. Zaruriy kutubxonalarni o'rnating:
    ```sh
    pip install -r requirements.txt
    ```
5. Ma'lumotlar bazasini migatsiya qiling:
    ```sh
    python manage.py migrate
    ```
6. Serverni ishga tushiring:
    ```sh
    python manage.py runserver
    ```

## Foydalanish
Loyihani ishga tushirgandan so'ng, brauzerda `http://127.0.0.1:8000/` manziliga o'ting.

Agar qo'shimcha savollaringiz yoki muammolar yuzaga kelsa, iltimos, muallif bilan bog'laning yoki loyiha repozitoriyasiga qarang.
