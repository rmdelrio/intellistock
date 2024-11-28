IntelliStock - Restaurant Food Inventory and Ordering System

Project Description
IntelliStock is a comprehensive inventory and ordering system tailored for restaurants, utilizing machine learning for sales forecasting and inventory optimization. The system integrates modern technologies to manage inventory, track daily sales, and streamline ordering processes with vendors.

This project uses Python (Django) for the backend, React.js for the frontend, and PostgreSQL as the database. The system incorporates TensorFlow for machine learning to predict inventory requirements based on historical sales data.

Features
Inventory Management: Track, update, and manage inventory items.
Order Management: Create, update, and track orders with vendors.
Machine Learning Forecasting: Predict suggested order quantities using TensorFlow.
Responsive Frontend: User-friendly UI/UX designed with React.js and Bootstrap.
Role-Based Access: Access control for admins, managers, and staff.
Data Analytics: Weekly sales projection with detailed reports.

Technologies Used
Backend:
Python: Core language for backend logic.
Django: Web framework for API development.
TensorFlow: Machine learning for forecasting inventory needs.

Frontend:
React.js: User interface development.
Bootstrap: Responsive and modern styling.
HTML5/CSS3: Structuring and styling web pages.

Database:
PostgreSQL: Reliable relational database for structured data.


Installation and Setup
Prerequisites:
Python 3.10+
PostgreSQL
Node.js and npm
Virtual Environment (Optional but recommended)

Backend Setup:
Clone the repository:

git clone https://github.com/your-username/intellistock.git
cd intellistock/intellistock_backend
Create a virtual environment and activate it:


python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

Install dependencies:

pip install -r requirements.txt
Configure PostgreSQL:
Create a database named IntelliStockDB.
Update settings.py with your PostgreSQL credentials.

Run migrations:
python manage.py makemigrations
python manage.py migrate

Start the server:
python manage.py runserver

Frontend Setup:
Navigate to the frontend directory:
cd ../intellistock_frontend

Install dependencies:
npm install
Start the development server:
npm start

📋 API Endpoints
Inventory Management APIs:
Get All Items: GET /api/items/
Get Item by ID: GET /api/items/<id>/
Create New Item: POST /api/items/
Update Item: PUT /api/items/<id>/
Delete Item: DELETE /api/items/<id>/

Order Management APIs:
Create Order: POST /api/orders/
Get Order Details: GET /api/orders/<id>/
Update Order: PUT /api/orders/<id>/
Delete Order: DELETE /api/orders/<id>/

Machine Learning APIs:
Forecast Inventory: GET /api/forecast/
📊 Weekly Sales Projection
The system provides a weekly sales projection page where users can:

View projected sales based on historical data.
Analyze gross sales, taxes, and net sales.
Determine optimized inventory levels.
🖥️ Deployment Instructions
Local Deployment:
Ensure all dependencies are installed.
Run backend and frontend servers simultaneously:
Backend: python manage.py runserver
Frontend: npm start


Contributors
Rica Marie Del Rio - Backend API Development
Christian Paul Marco - Database Design
Alvin Merritt - Frontend UI/UX Prototypes
Jose Carlo Dolor - Test Cases and Deployment Diagram
Jose Carlos Dominic Gaa - Project Management