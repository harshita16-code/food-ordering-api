# Scalable Food Ordering REST API 🍴

A backend REST API for a food ordering system, built with **Flask** and **MySQL**.  
It supports user management, menu management, and order placement.  
The project is containerized using Docker for easy deployment.

---

## 🚀 Features
- User signup and profile management  
- Add and view menu items  
- Place and track customer orders  
- MySQL database with normalized schema  
- RESTful JSON APIs  
- Dockerized for deployment on Linux environments  

---

## 🛠️ Tech Stack
- **Backend:** Python (Flask)  
- **Database:** MySQL, SQLAlchemy ORM  
- **Containerization:** Docker, Docker Compose  
- **Testing Tools:** Postman, Curl  

---

## ⚡ Installation & Setup

```bash
# 1. Clone the repo
git clone https://github.com/your-username/food-ordering-api.git
cd food-ordering-api

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create database in MySQL
CREATE DATABASE food_ordering;

# 5. Run the app
python app.py

---

## 📌 API Endpoints

### 👤 Users
- `POST /users` → Register new user  
- `GET /users/<id>` → Fetch user details  

### 🍔 Menu
- `POST /menu` → Add new food item  
- `GET /menu` → Get all menu items  

### 🛒 Orders
- `POST /orders` → Place an order  
- `GET /orders/<id>` → Get order details  

---

## 🐳 Docker Deployment

```bash
# Build Docker image
docker build -t food-ordering-api .

# Run container
docker run -p 5000:5000 food-ordering-api


---

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss improvements.

---

## 📄 License
This project is licensed under the MIT License.
