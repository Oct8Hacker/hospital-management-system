# Hospital Appointment Management System

A desktop-based Hospital Appointment Management System built with **Python** and **Tkinter** for managing doctor appointments, patient bookings, and basic patient-doctor messaging. The project uses **CSV files as lightweight storage** and provides separate workflows for **patients**, **doctors**, and **admin**. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}

## Overview

This application allows patients to book appointments with doctors through a GUI, lets doctors manage their appointments, and provides an admin interface to add, remove, or view doctor accounts. The system also includes a simple chat/message feature where patients can send messages to their doctor. :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5}

## Features

### Patient Features
- Book appointments by entering name, age, doctor, and time slot
- Prevent duplicate bookings for the same doctor and time slot
- Send messages to the selected doctor after booking an appointment :contentReference[oaicite:6]{index=6} :contentReference[oaicite:7]{index=7} :contentReference[oaicite:8]{index=8}

### Doctor Features
- Secure login using stored credentials
- View all appointments assigned to the logged-in doctor
- Mark appointments as **Completed**
- Mark appointments as **Cancelled**
- View patient messages for active booked appointments :contentReference[oaicite:9]{index=9} :contentReference[oaicite:10]{index=10} :contentReference[oaicite:11]{index=11}

### Admin Features
- Open admin panel from the login window
- Register a new doctor
- Remove an existing doctor
- View a doctor’s appointment dashboard directly :contentReference[oaicite:12]{index=12} :contentReference[oaicite:13]{index=13} :contentReference[oaicite:14]{index=14}

## Tech Stack

- **Language:** Python
- **GUI Framework:** Tkinter
- **Storage:** CSV files
- **Modules Used:** `csv`, `os`, `tkinter`, `ttk`, `functools` :contentReference[oaicite:15]{index=15} :contentReference[oaicite:16]{index=16}

## Project Structure

```bash
.
├── Main.py                # Entry point of the application
├── UI.py                  # All Tkinter GUI screens
├── Logic.py               # Business logic for appointments, doctors, and admin
├── csvfilereader.py       # CSV handling, login checks, appointment history, chat
├── doctorCredentials.csv  # Stores doctor usernames and passwords
├── patientData.csv        # Stores patient appointments
├── chat_data.csv          # Stores patient-doctor messages
├── GUI.png                # Background GUI image
├── LICENSE
└── README.md
