from flask import Flask, render_template, request, make_response
import pdfkit

app = Flask(__name__)

# Path to wkhtmltopdf
path_wkhtmltopdf = r'C:\Users\praja\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # code to generate resume

    data = request.form.to_dict()
    rendered = render_template('resume_template.html', data=data)
    pdf = pdfkit.from_string(rendered, False, configuration=config)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=resume.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)
