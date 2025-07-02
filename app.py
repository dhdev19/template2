from flask import Flask, render_template, request, redirect, url_for, send_file, after_this_request
import os
from werkzeug.utils import secure_filename
import zipfile
import io

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Store last submitted project data
global_project_data = {}

@app.route('/', methods=['GET', 'POST'])
def project_form():
    global global_project_data
    if request.method == 'POST':
        project = {
            'title': request.form['project_title'],
            'description': request.form['project_description'],
            'keywords': request.form['keywords'],
            'whatsappNumber': request.form['whatsapp_number'],
            'name': request.form['project_name'],
            'formSubHeading': request.form['project_form_subheading'],
            'address': request.form['project_address'],
            'startingfPrice': request.form['project_starting_price'],
            'paragraph': request.form['project_form_description'],
            'owner': request.form['owner_name'],
            'companyName': request.form['company_name'],
            'maharera': request.form['maharera_number'],
            'projectMaharera': request.form['project_maharera_number'],
            'mahareraWebsite': request.form['maharera_website']
        }

        # File handling
        def save_file(file):
            if file:
                filename = secure_filename(file.filename)
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(path)
                return os.path.join('uploads', filename).replace("\\", "/")
            return None

        # Images
        project['qrCode'] = save_file(request.files.get('qr_code_image'))
        project['favicon'] = save_file(request.files.get('favicon'))
        project['logo'] = save_file(request.files.get('logo'))
        project['aboutUsImage'] = save_file(request.files.get('about_us_image'))
        project['sliderImages'] = [save_file(file) for file in request.files.getlist('slider_images') if file.filename]
        project['gallery'] = [save_file(file) for file in request.files.getlist('project_gallery') if file.filename]
        project['floorPlans'] = [{'image': save_file(file)} for file in request.files.getlist('floor_plan_images') if file.filename]
        project['mapImage'] = save_file(request.files.get('map_image'))

        # Amenities, location, configuration
        project['amenities'] = request.form.getlist('amenities[]')
        project['locationBenefits'] = request.form.getlist('location_benefits[]')
        configurations = []
        for config, area, value in zip(
            request.form.getlist('configuration[]'),
            request.form.getlist('rera_carpet_area[]'),
            request.form.getlist('agreement_val[]')
        ):
            configurations.append({
                'type': config,
                'carpetArea': area,
                'agreementValue': value
            })
        project['configurations'] = configurations
        global_project_data = project
        return render_template('index.html', project=project)

    return render_template('form.html')

@app.route('/download_project', methods=['GET'])
def download_project():
    global global_project_data
    # Use last submitted data or default
    project = global_project_data if global_project_data else {
        'title': 'Sample Project',
        'description': 'Sample description',
        'keywords': 'sample,project',
        'whatsappNumber': '9999999999',
        'name': 'Sample Name',
        'formSubHeading': 'Sample Subheading',
        'address': 'Sample Address',
        'startingfPrice': '1,00,000',
        'paragraph': 'Sample overview',
        'owner': 'Sample Owner',
        'companyName': 'Sample Company',
        'maharera': 'RERA123',
        'projectMaharera': 'PRJ123',
        'mahareraWebsite': 'https://maharera.mahaonline.gov.in',
        'qrCode': 'uploads/qr-code.webp',
        'favicon': 'uploads/favicon.webp',
        'logo': 'uploads/logo.webp',
        'aboutUsImage': 'uploads/about-us.webp',
        'sliderImages': ['uploads/slider-1.webp', 'uploads/slider-2.webp', 'uploads/slider-3.webp'],
        'gallery': ['uploads/gallery-1.webp', 'uploads/gallery-2.webp'],
        'floorPlans': [{'image': 'uploads/floor-plan-1.webp'}, {'image': 'uploads/floor-plan-2.webp'}],
        'mapImage': 'uploads/map.jpg',
        'amenities': ['Amenity 1', 'Amenity 2'],
        'locationBenefits': ['Location 1', 'Location 2'],
        'configurations': [
            {'type': '1 BHK', 'carpetArea': '500', 'agreementValue': '50L'},
            {'type': '2 BHK', 'carpetArea': '800', 'agreementValue': '80L'}
        ]
    }
    # Render index.html to a string
    rendered_index = render_template('index.html', project=project)
    # Create zip in memory
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add static folder
        for folder, _, files in os.walk('static'):
            for file in files:
                file_path = os.path.join(folder, file)
                arcname = os.path.relpath(file_path, '.')
                zipf.write(file_path, arcname)
        # Add PHP files
        for php_file in [
            'privacy-policy.php', 'thank-you-brochure.php', 'include-frm-action.php', 'class.smtp.php', 'class.phpmailer.php']:
            if os.path.exists(php_file):
                zipf.write(php_file, php_file)
        # Add rendered index.html
        zipf.writestr('index.html', rendered_index)
    zip_buffer.seek(0)
    return send_file(zip_buffer, mimetype='application/zip', as_attachment=True, download_name='project_package.zip')

if __name__ == '__main__':
    app.run()
