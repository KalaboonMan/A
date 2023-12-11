
python -m venv <ชื่อenv>
.\<ชื่อenv>\Scripts\activate
pip install Flask
pip freeze

gh auth login
gh repo clone KanjanaPS/dstoolbox-A

cd .\dstoolbox-test\

git checkout -b <ชื่อ branch>
 กดเพิ่มไฟล์ app.py ได้เลย
เขียนฟังก์ชันที่ต้องการ ต้องเอา index เข้ามาด้วย 
หลังจากเขียนเสร็จกดเพิ่มโฟลเดอร์ templates
และสร้างไฟล์ index.html + สร้างไฟล์ฟังก์ชันที่ต้องการ 
git add .
git push .

##app.py##
from flask import Flask , render_template, request, redirect , url_for

app = Flask(__name__)

courses = [
    {'code' : 'TH001', 'name': 'Thai'},
    {'code' : 'Eng002', 'name': 'English'},
    {'code' : 'IR003', 'name': 'IR'},
]

@app.route('/')
def index():
    return render_template('index.html', courses = courses)

@app.route('/search', methods=['GET','POST'])
def search():
    result = None
    
    if request.method == 'POST':
        course_code = request.form.get('course_code')
        result = next((course for course in courses if course['code'] == course_code), None)
        
    return render_template('search.html', result=result)

@app.route('/search_by_name', methods=['GET','POST'])
def search_by_name():
    result = None
    
    if request.method == 'POST':
        course_name = request.form.get('course_name')
        result = next((course for course in courses if course['name'] == course_name), None)
        
    return render_template('search_by_name.html', result=result)

@app.route('/edit_course/<code>', methods=['GET','POST'])
def edit_course(code):
    result = next((course for course in courses if course['code'] == code), None)
    
    if result is None:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        result['name'] = request.form.get('course_name')
        
        return redirect(url_for('index'))
    
    return render_template('edit_course.html', result=result)

@app.route('/delete_course/<code>', methods=['GET','POST'])
def delete_course(code):
    result = next((course for course in courses if course['code'] == code), None)
    
    if result is None:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        courses.remove(result)
        
        return redirect(url_for('index'))
    
    return render_template('delete_course.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)


####index.html
<title>รายการวิชา</title>
<div id="course-list">
    <ul>
        {% for course in courses %}
            <li>{{ course['name'] }}</li>
        {% endfor %}
    </ul>
</div>


search.html
<title>ค้นหารายวิชา</title>
<h1>ค้นหารายวิชา</h1>
<form action="{{ url_for('search') }}" method="post">
    <label for="course_code">รหัสวิชา</label>
    <input type="text" id="course_code" name="course_code" requried>
    <button type="submit">ค้นหา</button>
</form>
{% if result %}
    <div id="search-result">
        <h2>ผลลัพธ์การค้นหา</h2>
        <p>รหัสวิชา: {{ result['code'] }}</p>
        <p>ชื่อวิชา:{{ result['name'] }}</p>
    </div>
{% endif %}



search_by_name.html
<title>ค้นหารายวิชา</title>
<h1>ค้นหารายวิชา</h1>
<form action="{{ url_for('search_by_name') }}" method="post">
    <label for="course_name">ชื่อวิชา</label>
    <input type="text" id="course_name" name="course_name" requried>
    <button type="submit">ค้นหา</button>
</form>
{% if result %}
    <div id="search-result">
        <h2>ผลลัพธ์การค้นหา</h2>
        <p>รหัสวิชา: {{ result['code'] }}</p>
        <p>ชื่อวิชา:{{ result['name'] }}</p>
    </div>
{% endif %}


edit_course.html
<title>แก้ไขข้อมูลรายวิชา</title>
<h1>แก้ไขข้อมูลรายวิชา</h1>
<form action="{{ url_for('edit_course'), code=result['code'] }}" method="post">
    <label for="course_name">ชื่อวิชา</label>
    <input type="text" id="course_name" name="course_name" value="{{ result['name'] }}" requried>
    <button type="submit">บันทึก</button>
</form>



delete_course.html
<title>ลบรายวิชา</title>
<h1>ลบรายวิชา</h1>
<p>คุณแน่ใจหรือไม่ที่ต้องการลบรายวิชา "{{ result['name'] }}" (รหัสวิชา: {{ result['code']  }})?</p>
<form action="{{ url_for('delete_course'), code=result['code'] }}" method="post">
    <button type="submit">ลบ</button>
    <a href="{{ url_for('index') }}">ยกเลิก</a>
</form>
