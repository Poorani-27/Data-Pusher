﻿# Data_Pusher
# Data Pusher Project

## Overview
The Data Pusher Project is a web application built using Django, a high-level Python web framework. It provides functionalities for receiving, processing, and storing data submitted by clients through a RESTful API. The application also includes an administration interface for managing users, data, and other aspects of the system.

## Features
- **API Endpoint**: Provides an endpoint for clients to submit data to the server.
- **Django Admin Interface**: Allows administrators to manage user accounts, view submitted data, and perform other administrative tasks.
- **User Authentication and Authorization**: Implements user authentication and authorization to control access to different parts of the application.
- **Data Processing**: Processes the submitted data according to predefined rules and stores it in the database.
- **Database Storage**: Utilizes a relational database to store the processed data efficiently.

## Installation
Follow these steps to set up the Data Pusher Project locally:

### Prerequisites
- Python (>=3.6)
- pip (Python package manager)
- Git (optional, for cloning the repository)

### Steps
1. **Clone the Repository**: 
    ```bash
    git clone https://github.com/Poorani-27/Data_Pusher.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd Data_Pusher
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Database Migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Configure Secret Key**:
    - Generate a new secret key for your Django project. You can use online generators or Django's `django.core.management.utils.get_random_secret_key()` function to generate one.
    - Replace the value of `SECRET_KEY` in `data_pusher_project/settings.py` with your generated secret key.

6. **Start the Development Server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the Application**:
    Open a web browser and go to `http://127.0.0.1:8000/` to access the application.

## Usage
Here's how you can use the Data Pusher Project:

1. **Admin Interface**:
   - Access the Django admin interface at `http://127.0.0.1:8000/admin/`.
   - Log in with administrator credentials to manage user accounts, view submitted data, and perform administrative tasks.

2. **API Endpoint**:
   - Clients can submit data to the API endpoint at `http://127.0.0.1:8000/api/`.
   - Ensure that the submitted data follows the specified format and includes any required authentication tokens or headers.

## Configuration
The Data Pusher Project can be configured through the following settings:

- **Database Configuration**: Configure the database connection settings in `data_pusher_project/settings.py`.
- **API Endpoint Configuration**: Customize the API endpoint URL and other settings in `data_pusher_app/urls.py`.
- **User Authentication**: Adjust user authentication settings, such as login/logout URLs and authentication backends, in `data_pusher_project/settings.py`.

## Contributing
If you'd like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them to your branch.
5. Push your changes to your forked repository on GitHub.
6. Create a pull request to merge your changes into the main repository.


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

![snapshot](output.png)
