# Scalable Food Ordering REST API 🍴

A backend REST API for a food ordering system, built with **Flask** and **MySQL**.  
It supports user management, menu management, and order placement.  
The project is containerized using Docker for easy deployment.

## 🚀 Features
- User signup and profile management  
- Add and view menu items  
- Place and track customer orders  
- MySQL database with normalized schema  
- RESTful JSON APIs  
- Dockerized for deployment on Linux environments  

## 🛠️ Tech Stack
- **Backend:** Python (Flask)  
- **Database:** MySQL, SQLAlchemy ORM  
- **Containerization:** Docker, Docker Compose  
- **Testing Tools:** Postman, Curl  

## ⚡ Installation & Setup

1. Clone the repository  
```bash
git clone https://github.com/your-username/food-ordering-api.git
cd food-ordering-api

python -m venv venv
source venv\Scripts\activate

pip install -r requirements.txt

CREATE DATABASE food_ordering;

python app.py


---

### 5. **API Endpoints**
```markdown
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

## 🐳 Docker Deployment

1. Build the Docker image  
```bash
docker build -t food-ordering-api .

docker run -p 5000:5000 food-ordering-api

http://localhost:5000


---

### 7. **Contributing**
```markdown
## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

## 📄 License
This project is licensed under the MIT License.
