# Flask Application for Health Clinic Queue Manager
from flask import Flask, render_template, request, redirect, url_for
from models import ClinicQueue

app = Flask(__name__)


# Initialize clinic queue instance
clinic = ClinicQueue()
# Initialize clinic queue for managing patients

# Add sample patients
# Sample patients for testing the queue system
clinic.add_patient("John Doe", 45, "General Checkup")
clinic.add_patient("Jane Smith", 32, "Flu Symptoms")
clinic.add_patient("Ahmed Hassan", 28, "Headache")


# Home route - display queue and statistics
@app.route('/')
def home():
# Home route - display current waiting queue
    """Home page - displays the waiting list."""
    waiting_list = clinic.get_waiting_list()
    queue_size = clinic.get_queue_size()
    patients_seen = clinic.get_patients_seen_today()
    
    return render_template('home.html', 
                         waiting_list=waiting_list,
                         queue_size=queue_size,
                         patients_seen=patients_seen)


@app.route('/register', methods=['GET', 'POST'])
def register():
# Register route - handle patient registration form
    """Register new patient page."""
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        reason = request.form.get('reason')
        
        if name and age and reason:
            clinic.add_patient(name, int(age), reason)
            return redirect(url_for('home'))
    
    return render_template('register.html')


@app.route('/see-patient', methods=['POST'])
def see_patient():
    """Mark the next patient as seen."""
    clinic.see_next_patient()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)