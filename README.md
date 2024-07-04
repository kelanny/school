# School Management System

## Description

The School Management System is a comprehensive application designed to manage school records efficiently. This system allows for the management of student and teacher information, class schedules, subjects, and financial records, including invoices, payments, and balances. The application ensures that school administrators can keep track of student attendance, grades, and overall academic performance.

## Features

- **Student Management**: Add, update, and delete student records.
- **Teacher Management**: Manage teacher information and their assigned subjects.
- **Class Management**: Create and manage classes, and assign students and teachers to classes.
- **Subject Management**: Define subjects and assign teachers to subjects.
- **Financial Management**: Generate and manage student invoices, record payments, and track balances.
- **Attendance Tracking**: Record and monitor student attendance.
- **Grade Management**: Record and manage student grades.

## Command Interpreter

The command interpreter is a CLI (Command Line Interface) tool that allows users to interact with the School Management System. Users can perform various operations such as adding new students, generating invoices, and recording payments.

### How to Start the Command Interpreter

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/school-management-system.git
    ```
2. **Navigate to the Project Directory**:
    ```bash
    cd school-management-system
    ```
3. **Install Dependencies**:
    Make sure you have Python and pip installed. Then, install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the Command Interpreter**:
    ```bash
    python manage.py
    ```

### How to Use the Command Interpreter

Once the command interpreter is running, you can use the following commands to interact with the system:

- **Add a New Student**:
    ```bash
    add_student --first_name John --last_name Doe --dob 2005-05-15 --gender M --address "123 Main St" --email john.doe@example.com --phone 555-1234 --class Grade1
    ```
- **Add a New Teacher**:
    ```bash
    add_teacher --first_name Jane --last_name Smith --dob 1980-08-20 --gender F --address "456 Elm St" --email jane.smith@example.com --phone 555-5678 --subjects "Mathematics,Science"
    ```
- **Generate an Invoice**:
    ```bash
    generate_invoice --student_id 1 --amount 500 --due_date 2024-08-01
    ```
- **Record a Payment**:
    ```bash
    record_payment --invoice_id 1 --amount 250 --payment_date 2024-07-15 --method "credit card"
    ```
- **View Student Balance**:
    ```bash
    view_balance --student_id 1
    ```
- **Record Attendance**:
    ```bash
    record_attendance --student_id 1 --date 2024-07-04 --status present
    ```
- **Add a Grade**:
    ```bash
    add_grade --student_id 1 --subject_id 1 --marks 95 --grade A --date 2024-06-30
    ```

### Examples

- **Adding a New Student**:
    ```bash
    $ python manage.py
    > add_student --first_name John --last_name Doe --dob 2005-05-15 --gender M --address "123 Main St" --email john.doe@example.com --phone 555-1234 --class Grade1
    Student John Doe added successfully.
    ```

- **Generating an Invoice**:
    ```bash
    $ python manage.py
    > generate_invoice --student_id 1 --amount 500 --due_date 2024-08-01
    Invoice generated successfully.
    ```

- **Recording a Payment**:
    ```bash
    $ python manage.py
    > record_payment --invoice_id 1 --amount 250 --payment_date 2024-07-15 --method "credit card"
    Payment recorded successfully.
    ```

Feel free to explore other commands and functionalities. This README provides a basic overview to get you started with the School Management System.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
