# 🛒 Django Ecommerce Project

A fully functional ecommerce website built with Django, featuring product catalog, shopping cart, wishlist, user authentication, and order management.

## ✨ Features

- **Product Catalog**: Browse products by categories (Milk, Curd, Ghee, Lassi, etc.)
- **Search Functionality**: Search products by name, description, or category
- **Shopping Cart**: Add, remove, and manage cart items with quantity controls
- **Wishlist**: Save favorite products for later
- **User Authentication**: Registration, login, logout, and profile management
- **Order Management**: Complete checkout process with order history
- **Admin Panel**: Full admin interface for managing products, users, and orders
- **Responsive Design**: Mobile-friendly interface with Bootstrap
- **Payment Integration**: Basic payment system (ready for Razorpay integration)

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-ecommerce.git
   cd django-ecommerce
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv env
   .\env\Scripts\activate

   # macOS/Linux
   python -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create sample data**
   ```bash
   python manage.py populate_products
   python manage.py create_sample_customer
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Website: http://localhost:8000
   - Admin: http://localhost:8000/admin/

### 🎯 One-Click Setup (Windows)

Simply double-click `start_project.bat` to automatically:
- Activate virtual environment
- Install all dependencies
- Run migrations
- Create sample data
- Start the server

## 📱 Usage

### For Users
1. **Browse Products**: Navigate through different product categories
2. **Search**: Use the search bar to find specific products
3. **Add to Cart**: Click "Add to Cart" on any product
4. **Manage Cart**: View cart, update quantities, or remove items
5. **Wishlist**: Add products to wishlist for later purchase
6. **Checkout**: Complete the purchase process
7. **Track Orders**: View order history and status

### For Administrators
1. **Access Admin**: Go to http://localhost:8000/admin/
2. **Manage Products**: Add, edit, or delete products
3. **User Management**: Manage user accounts and profiles
4. **Order Management**: View and update order status
5. **Analytics**: Monitor sales and user activity

## 🏗️ Project Structure

```
django-ecommerce/
├── ec/                          # Django project directory
│   ├── app/                     # Main application
│   │   ├── templates/           # HTML templates
│   │   ├── static/             # CSS, JS, images
│   │   ├── models.py           # Database models
│   │   ├── views.py            # View functions
│   │   ├── urls.py             # URL patterns
│   │   └── management/         # Custom management commands
│   ├── ec/                     # Project settings
│   │   ├── settings.py         # Django settings
│   │   └── urls.py             # Main URL configuration
│   └── manage.py               # Django management script
├── env/                        # Virtual environment (not in git)
├── media/                      # User uploaded files
├── requirements.txt            # Python dependencies
├── start_project.bat           # Quick start script (Windows)
├── .gitignore                  # Git ignore file
└── README.md                   # This file
```

## 🛠️ Technologies Used

- **Backend**: Django 5.0.2
- **Database**: SQLite (development)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Image Processing**: Pillow
- **Authentication**: Django's built-in auth system
- **Payment**: Razorpay (ready for integration)

## 📊 Database Models

- **Product**: Product information and images
- **Customer**: User profile and shipping addresses
- **Cart**: Shopping cart items
- **Wishlist**: User wishlist items
- **OrderPlaced**: Order information
- **Payment**: Payment records

## 🔧 Custom Management Commands

- `python manage.py populate_products`: Add sample products
- `python manage.py create_sample_customer`: Create test user with address

## 🎨 Features in Detail

### Product Management
- Product categories (Milk, Curd, Ghee, Lassi, Milkshake, Paneer, Cheese, Ice Cream)
- Product images with Pillow integration
- Price management (selling price vs discounted price)
- Product descriptions and specifications

### Shopping Experience
- Real-time cart updates
- Quantity management (+/- buttons)
- Remove items from cart
- Wishlist functionality
- Search across products

### User Experience
- User registration and authentication
- Profile management
- Address management
- Order history
- Responsive design

## 🚀 Deployment

This project is ready for deployment on platforms like:
- Heroku
- DigitalOcean
- AWS
- Google Cloud Platform

For production deployment, make sure to:
1. Set `DEBUG = False` in settings
2. Configure a production database (PostgreSQL recommended)
3. Set up static file serving
4. Configure email settings
5. Set up proper security settings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

- GitHub: [MadhavKhera1](https://github.com/MadhavKhera1)
- Email: madhavkhera868@gmail.com

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap for the responsive UI components
- All contributors who helped improve this project

---

**Happy Shopping! 🛒✨**