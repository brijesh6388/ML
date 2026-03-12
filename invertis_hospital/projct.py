from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Data storage
doctors = []
patients = []
appointments = []

# Default Diseases (10 already added)
diseases = [
    {"name": "Fever"},
    {"name": "Cold"},
    {"name": "Cough"},
    {"name": "Diabetes"},
    {"name": "Blood Pressure"},
    {"name": "Headache"},
    {"name": "Stomach Pain"},
    {"name": "Skin Allergy"},
    {"name": "Asthma"},
    {"name": "Typhoid"}
]


# Dashboard
@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        patientCount=len(patients),
        doctorCount=len(doctors),
        diseaseCount=len(diseases),
        appointmentCount=len(appointments),
        appointments=appointments
    )


# Doctor Page
@app.route("/doctor", methods=["GET", "POST"])
def doctor_page():

    if request.method == "POST":

        name = request.form.get("name")
        speciality = request.form.get("speciality")

        if name and speciality:
            doctors.append({
                "name": name,
                "speciality": speciality
            })

        return redirect("/doctor")

    return render_template("doctor.html", doctors=doctors)


# Patient Page
@app.route("/patient", methods=["GET", "POST"])
def patient_page():

    if request.method == "POST":

        name = request.form.get("name")
        disease = request.form.get("disease")

        if name and disease:
            patients.append({
                "name": name,
                "disease": disease
            })

        return redirect("/patient")

    return render_template(
        "patient.html",
        patients=patients,
        diseases=diseases
    )


# Disease Page
@app.route("/disease", methods=["GET", "POST"])
def disease_page():

    if request.method == "POST":

        name = request.form.get("name")

        if name:
            diseases.append({
                "name": name
            })

        return redirect("/disease")

    return render_template(
        "disease.html",
        diseases=diseases
    )


# Book Appointment
@app.route("/book", methods=["GET", "POST"])
def book_page():

    if request.method == "POST":

        patient = request.form.get("patient")
        doctor = request.form.get("doctor")
        disease = request.form.get("disease")
        date = request.form.get("date")

        if patient and doctor and disease and date:
            appointments.append({
                "patient": patient,
                "doctor": doctor,
                "disease": disease,
                "date": date
            })

        return redirect("/appointments")

    return render_template(
        "book.html",
        patients=patients,
        doctors=doctors,
        diseases=diseases
    )


# Appointment List
@app.route("/appointments")
def appointments_page():

    return render_template(
        "appointments.html",
        appointments=appointments
    )
# Delete All History
@app.route("/delete_all")
def delete_all():

    doctors.clear()
    patients.clear()
    appointments.clear()

    return redirect("/")


# Run Server
if __name__ == "__main__":
    app.run(debug=True)