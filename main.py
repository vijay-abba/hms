from exceptions.custom_exceptions import HMSBaseExpection
from modules.department import Department


def safe_run(func, *args, **kwargs):

    try:
        return func(*args, **kwargs)
    except HMSBaseExpection as e:
        print(f"\n[ERROR] {e.message}")
    except KeyboardInterrupt:
        print("\n[Info] Operation cancelled by user.\n")
    except Exception as e:
        print(f"\n [UNEXPECTED ERROR] {e}\n")


def department_menu():
    dept = Department()
    while True:
        print("\n ---- Department Management ----")
        print("1. Add Department")
        print("2. View All Department")
        print("3. Get Department By ID")
        print("4. Update Department")
        print("5. Delete Department")
        print("0. Back")

        dep_choice = input("Enter choice: ").strip()

        if dep_choice == "1":

            def _add():
                dept_name = input("Enter Department name: ")
                dept_code = input("Enter Department code: ")
                dept.add(department_name=dept_name, department_code=dept_code)

            safe_run(_add)

        elif dep_choice == "2":
            print("view all")
        elif dep_choice == "3":
            print("Get dep by id")
        elif dep_choice == "4":
            print("update department")
        elif dep_choice == "5":
            print("delete department")
        elif dep_choice == "0":
            break
        else:
            print("Invalid choice")


def patient_menu():
    while True:
        print("\n ---- Patient Management ----")
        print("1. Add Patient")
        print("2. View All Patient")
        print("3. Get Patient By ID")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("0. Back")

        patient_choice = input("Enter choice: ").strip()

        if patient_choice == "1":
            print("adding")
        elif patient_choice == "2":
            print("view all")
        elif patient_choice == "3":
            print("Get dep by id")
        elif patient_choice == "4":
            print("update patient")
        elif patient_choice == "5":
            print("delete Patient")
        elif patient_choice == "0":
            break
        else:
            print("Invalid choice")


def doctor_menu():
    while True:
        print("\n ---- Doctor Management ----")
        print("1. Add Doctor")
        print("2. View All Doctor")
        print("3. Get Doctor By ID")
        print("4. Update Doctor")
        print("5. Delete Doctor")
        print("0. Back")

        doctor_choice = input("Enter choice: ").strip()

        if doctor_choice == "1":
            print("adding")
        elif doctor_choice == "2":
            print("view all")
        elif doctor_choice == "3":
            print("Get dep by id")
        elif doctor_choice == "4":
            print("update doctor")
        elif doctor_choice == "5":
            print("delete doctor")
        elif doctor_choice == "0":
            break
        else:
            print("Invalid choice")


def appointment_menu():
    while True:
        print("\n ---- Appointment Management ----")
        print("1. Book Appointment")
        print("2. View All Appointment")
        print("3. Get Appointment By ID")
        print("4. Update Appointment")
        print("5. Delete Appointment")
        print("6. Cancel Appointment")
        print("0. Back")

        app_choice = input("Enter choice: ").strip()

        if app_choice == "1":
            print("adding")
        elif app_choice == "2":
            print("view all")
        elif app_choice == "3":
            print("Get dep by id")
        elif app_choice == "4":
            print("update Appointment")
        elif app_choice == "5":
            print("delete Appointment")
        elif app_choice == "6":
            print("Cancel Appointment")
        elif app_choice == "0":
            break
        else:
            print("Invalid choice")


def treatment_menu():
    while True:
        print("\n ---- Treatment Management  ----")
        print("1. Add Treatment")
        print("2. View All Treatment")
        print("3. Get Treatment By ID")
        print("4. Update Treatment")
        print("5. Delete Treatment")
        print("0. Back")

        treatment_choice = input("Enter choice: ").strip()

        if treatment_choice == "1":
            print("adding")
        elif treatment_choice == "2":
            print("view all")
        elif treatment_choice == "3":
            print("Get dep by id")
        elif treatment_choice == "4":
            print("update Treatment")
        elif treatment_choice == "5":
            print("delete Treatment")
        elif treatment_choice == "0":
            break
        else:
            print("Invalid choice")


def billing_menu():
    while True:
        print("\n ---- Billing Management ----")
        print("1. Add Bill (manual)")
        print("2. Auto-Generate Bill from Treatments")
        print("3. Vill All Bills ")
        print("4. Get Bill By ID")
        print("5. Update Bill")
        print("6. Delete Bill")
        print("0. Back")

        bill_choice = input("Enter choice: ").strip()

        if bill_choice == "1":
            print("adding")
        elif bill_choice == "2":
            print("view all")
        elif bill_choice == "3":
            print("Get dep by id")
        elif bill_choice == "4":
            print("update bill")
        elif bill_choice == "5":
            print("delete bill")
        elif bill_choice == "6":
            print("delete bill")
        elif bill_choice == "0":
            break
        else:
            print("Invalid choice")


def dashboard_menu():
    while True:
        print("\n ---- Department Management ----")
        print("1. Summary Numbers")
        print("2. Top Doctors By Revenue")
        print("3. Patients per Department")
        print("4. Monthly Revenue Trend")
        print("5. Pending Payments")
        print("6. Most common Treatments")
        print("0. Back")

        dep_choice = input("Enter choice: ").strip()

        if dep_choice == "1":
            print("Summary Numbers")
        elif dep_choice == "2":
            print("Top Doctors By Revenue")
        elif dep_choice == "3":
            print("Patients per Department")
        elif dep_choice == "4":
            print("Monthly Revenue Trend")
        elif dep_choice == "5":
            print("Pending Payments")
        elif dep_choice == "6":
            print("Most common Treatments")
        elif dep_choice == "0":
            break
        else:
            print("Invalid choice")


def main_menu():

    while True:
        print("=" * 45)
        print(" HOSPITAL MANAGEMENT SYSTEM (HMS)")
        print("=" * 45)
        print("1. Department Management")
        print("2. Patient Management")
        print("3. Doctor Management")
        print("4. Appointment Management")
        print("5. Treatment Management")
        print("6. Billing Management")
        print("7. Dashboard")
        print("0. Exit")
        user_choice = input("Enter choice ").strip()

        if user_choice == "1":
            department_menu()
        elif user_choice == "2":
            patient_menu()
        elif user_choice == "3":
            doctor_menu()
        elif user_choice == "4":
            appointment_menu()
        elif user_choice == "5":
            treatment_menu()
        elif user_choice == "6":
            billing_menu()
        elif user_choice == "7":
            dashboard_menu()
        elif user_choice == "0":
            print("Thank you")
            break
        else:
            print("Invalid Option")


main_menu()
