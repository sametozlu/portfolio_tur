from flask import Flask, render_template, request

app = Flask(__name__)

# Dinamik projeler verisi
projects_data = {
    "python": [
        {"name": "Python Proje 1", "description": "Python ile yapılmış bir proje."},
        {"name": "Python Proje 2", "description": "Başka bir Python projesi."}
    ],
    "javascript": [
        {"name": "JavaScript Proje 1", "description": "JavaScript kullanarak yapılmış bir proje."},
        {"name": "JavaScript Proje 2", "description": "Başka bir JavaScript projesi."}
    ],
    "html_css": [
        {"name": "HTML/CSS Proje 1", "description": "HTML ve CSS ile yapılmış bir proje."},
        {"name": "HTML/CSS Proje 2", "description": "Başka bir HTML/CSS projesi."}
    ]
}

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')

# Dinamik beceriler ve projeler
@app.route('/', methods=['POST'])
def process_form():
    selected_skill = request.form.get('button_python') or request.form.get('button_javascript') or request.form.get('button_html_css')

    if selected_skill:
        projects = projects_data.get(selected_skill, [])
        return render_template('projects.html', skill=selected_skill, projects=projects)
    
    return redirect('/')

# Geri bildirim formu verilerini işleme
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        email = request.form['email']
        text = request.form['text']
        
        # Form verilerini terminal ekranına yazdırma
        print(f"\n--- Geri Bildirim ---")
        print(f"E-posta: {email}")
        print(f"Yorum: {text}")
        print("\nTeşekkür ederiz, geri bildiriminiz alınmıştır.")
        
        # Teşekkür mesajı dönüyoruz
        return "Teşekkür ederiz, geri bildiriminiz alınmıştır."
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
