# 📝 Resume Builder for Tier-2/Tier-3 Students

A full-stack resume builder web application designed to help students from Tier-2/Tier-3 colleges easily create professional-looking resumes for jobs, internships, and hackathons.

---

## 🔧 Features

- 📄 Generate professional resume PDFs automatically
- ✅ User-friendly form-based input system
- 📚 Sections included:
  - Personal Details
  - Career Objective
  - Educational Qualifications
  - Technical Skills
  - Projects
  - Certifications
  - Achievements
  - Languages Known
  - GitHub and LinkedIn Profiles
- 💡 Real-time preview of resume fields
- 🎨 Clean and printable PDF format using HTML/CSS

---

## 🛠️ Tech Stack

| Layer     | Tech Used          |
|-----------|--------------------|
| Frontend  | HTML, CSS, JavaScript |
| Backend   | Python (Flask)     |
| Templating| Jinja2 (Flask default) |
| PDF Tool  | pdfkit + wkhtmltopdf |

---

## 📁 Project Structure

resume-builder/
│
├── app.py # Flask backend
├── requirements.txt # Python dependencies
│
├── static/
│ ├── style.css # Custom styling
│ └── script.js # Optional JavaScript
│
├── templates/
│ ├── index.html # Main form page
│ └── resume_template.html # Resume template for PDF
│
└── README.md # Project readme

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/<your-username>/resume-builder.git
cd resume-builder
2. Install Required Python Packages
pip install -r requirements.txt
3. Install wkhtmltopdf
Download from: https://wkhtmltopdf.org/downloads.html
Make sure it's added to your system PATH, or update the path in app.py:
config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
4. Run the Flask App
python app.py
Visit in browser: http://127.0.0.1:5000

💻 Usage
Fill out all the fields on the home page form.

Click Generate Resume.

Your resume will be automatically downloaded as a PDF.


✅ Future Enhancements
User login and dashboard to save resumes

Multiple template designs to choose from

Export to .docx format

Drag-and-drop section ordering

Dark mode support

👨‍💻 Contributor
Hariprasad R

📄 License
This project is licensed under the MIT License.

🙌 Acknowledgements
Inspired by the needs of students seeking internships and placements.

Thanks to Flask, wkhtmltopdf, and Open Source libraries.

⭐ Star this repository if you find it helpful!

---
