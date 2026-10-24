# 💍 Dream Weddings

**Dream Weddings** is a Django web application designed to help users explore wedding packages, discover professional wedding services, and share their experiences through reviews.

The project was developed as an individual practical assignment for the **SoftUni Python Web – Django Basics** course.

## ✨ Features

### 💒 Wedding Management

- Browse available wedding packages.
- View wedding details, pricing, and included services.
- Create, edit, and delete wedding packages.
- Add wedding images using either an image URL or a file upload.
- Validate wedding forms to ensure an image is provided.
- Read customer reviews and view average ratings.
- Submit reviews for individual wedding packages.
- Select multiple services when creating or editing a wedding package.

### 📸 Service Management

- Explore wedding services across four categories:
  - Photography
  - Videography
  - DJ
  - Decoration
- View service descriptions and contact information.
- Create, edit, and delete services.
- Validate service information through Django forms.

### 🎨 Additional Features

- Custom 404 error page.
- Custom Django template filter for formatting phone numbers.
- Responsive interface with a custom wedding-inspired design.
- Form validation and user-friendly error messages.
- Confirmation pages for deletion.
- Uploaded image handling using Django's media configuration.

## 🛠️ Technologies

- Python
- Django
- PostgreSQL
- Pillow
- HTML5
- CSS3
- Django Template Language (DTL)
- Git & GitHub

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/nikolaygrakow/Dream-Weddings.git
cd Dream-Weddings
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows (Command Prompt):

```cmd
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

This installs Django, PostgreSQL-related dependencies, Pillow, and the other required packages.

### 4. Configure PostgreSQL and environment variables

Make sure PostgreSQL is installed and running, and create a database for the project.

Create a `.env` file in the project root with the following configuration:

```env
# App
SECRET_KEY=your_django_secret_key
DEBUG=True

# Database credentials
DB_NAME=your_database_name
DB_USER=your_postgresql_username
DB_PASSWORD=your_postgresql_password
DB_HOST=localhost
```

Replace the placeholder values with your local configuration.

The `.env` file is excluded from Git version control to protect sensitive credentials. Set `DEBUG=False` when configuring the application for production.

### 5. Apply database migrations

```bash
python manage.py migrate
```

This creates the required database tables.

After applying migrations, you can create wedding services and packages directly through the application's interface.

### 6. Start the development server

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

## 📁 Project Structure

```text
Dream-Weddings/
├── common/
├── services/
├── weddings/
├── weddingProject/
├── templates/
├── static/
│   └── css/
├── media/                 # Uploaded images (local)
├── manage.py
├── requirements.txt
└── README.md
```

The application is organized into three Django apps:

- **common** — shared application functionality.
- **services** — wedding service management.
- **weddings** — wedding packages and customer reviews.

## 🔮 Future Improvements

- **Categorized Service Selection:** Enhance the existing checkbox interface by grouping wedding services into clearly labeled categories (Photography, Videography, DJ, and Decoration), with a scrollable layout for larger service catalogs.
- **Service Filtering:** Allow users to filter available services by category for easier navigation and selection.
- **User Authentication:** Introduce user accounts and permissions for managing wedding packages and submitting reviews.
- **Sample Data:** Provide optional demo data to help new users explore the application immediately after installation.

## 👨‍💻 Author

Developed by **Nikolay Grakov** as part of the **SoftUni Python Web – Django Basics** course.