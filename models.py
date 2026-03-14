# Patient and Queue Management System for Health Clinic
"""
Health Clinic Queue Management System
Using OOP, FIFO Queue, and DateTime Module
"""

from datetime import datetime
from collections import deque

class Patient:
    
# Represents a single patient entity
# This class represents a single patient in the clinic
    """Represents a patient in the clinic queue."""
    
    def __init__(self, patient_id, name, age, reason):
    # Store patient information and registration time
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.reason = reason
        self.timestamp = datetime.now()
        self.seen = False
    
    def mark_as_seen(self):
        """Mark patient as seen by doctor."""
        self.seen = True
    
    def get_wait_time(self):
        """Calculate how long patient has been waiting."""
        wait_duration = datetime.now() - self.timestamp
        minutes = int(wait_duration.total_seconds() / 60)
        return f"{minutes} minutes"
    
    def to_dict(self):
        """Convert patient object to dictionary for display."""
        return {
            'patient_id': self.patient_id,
            'name': self.name,
            'age': self.age,
            'reason': self.reason,
            'timestamp': self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'seen': self.seen,
            'wait_time': self.get_wait_time()
        }


class ClinicQueue:
# This class manages the FIFO queue of patients
    """Manages the queue of patients (FIFO - First In, First Out)."""
    
    def __init__(self):
        self.queue = deque()
        self.patient_counter = 0
        self.patients_seen_today = 0
    
    def add_patient(self, name, age, reason):
    # Add a new patient to the back of the queue
        """Add a new patient to the queue."""
        self.patient_counter += 1
        patient = Patient(self.patient_counter, name, age, reason)
        self.queue.append(patient)
        return patient
    
    def see_next_patient(self):
    # Remove patient from front of queue (FIFO)
        """Remove and mark the next patient as seen (FIFO)."""
        if len(self.queue) > 0:
            patient = self.queue.popleft()
            patient.mark_as_seen()
            self.patients_seen_today += 1
            return patient
        return None
    
    def get_waiting_list(self):
        """Get list of all patients currently waiting."""
        return [patient.to_dict() for patient in self.queue]
    
    def get_queue_size(self):
        """Get number of patients waiting."""
        return len(self.queue)
    
    def get_patients_seen_today(self):
        """Get total number of patients seen today."""
        return self.patients_seen_today