<img src="https://github.com/user-attachments/assets/37c7bad1-d80d-4286-85fc-9d8418cd644a" alt="PawsomePicksome" width="200" height="200"> </br>

# Pawsome Picksome - E-commerce Pets Product Purchasing Website 

Pawsome Picksome is an e-commerce website dedicated to pet products, allowing users to browse, purchase, and manage their pet-related purchases conveniently. The website is built using Python and Django framework, with front-end development using HTML, CSS, and JavaScript (Bootstrap for responsive design). It includes various features such as user authentication, payment integration with Razorpay, PostgreSQL database for data management, and several user-centric functionalities like wishlists, cart management, order status tracking, and more.

## Features

- **User Authentication:** Secure user registration, login, logout, and authentication using Django's built-in authentication system as well as Google OAuth2 via **Google Authentication**.
  
- **Password Management:** Users can reset and change passwords securely, including password manipulation in the **Customer Profile Section**.

- **Wishlist Management:** Authenticated users can add and remove products from their wishlist for future reference.

- **Shopping Cart:** Fully functional shopping cart with plus and minus buttons to adjust quantities, calculating total amounts dynamically.

- **Order Management:** Users can view their order status and history, providing transparency and tracking. Once an order is delivered, an **invoice is generated** for download.

- **Search Functionality:** Dedicated search bar to find specific products and related items based on user queries.

- **Admin Features:** Only authenticated admin users can add products, manage inventory, and view site analytics. The **admin panel** is enhanced with **Jazzmin** for a more customized and feature-rich experience.

- **Static Pages:** About and Contact pages provide information about the website and facilitate communication with users.

- **Footer:** Detailed footer with links to important pages, social media, and contact information for enhanced user experience.

- **Customer Profile Section:** Each user has a profile section where they can upload a **profile photo**, manage their **address**, and handle **password changes**.

## Technologies Used

- **Backend:** Python, Django, PostgreSQL
- **Frontend:** HTML, CSS, JavaScript, Bootstrap, **jQuery**
- **Payment Integration:** Razorpay for secure and seamless payment processing
- **Admin Interface:** Jazzmin for enhanced admin panel functionality and styling
- **Invoice Generation:** Automatic invoice generation for delivered products
- **Authentication:** Google OAuth2 for login via **Google Authentication**


## Installation

1. Create and activate virtual environment

   For windows
   ```cmd
   python -m venv .venv
   .venv\Scripts\activate
   ```

   For linux
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Clone the repository:
   ```bash
    git clone https://github.com/Sreenathkk00/PawsomePicks_E-com.git
3. Install dependencies:
   ```bash
    pip install -r requirements.txt
4. Configure PostgreSQL database settings in `settings.py`.
   ```bash
     DATABASES = {
    'default': {
        'ENGINE': 'Specify the backend',
        'NAME': 'Your database name',
        'USER': 'Your database username',
        'PASSWORD': 'Your database password',
        'HOST': 'Set to empty string for localhost',
        'PORT': 'Default PostgreSQL port',
    }
   }
5. Configure Razorpay credentials in `settings.py`.
   ```bash
   RAZORPAY_KEY_ID = 'Your Razorpay Key ID'
   RAZORPAY_SECRET_KEY = 'Your Razorpay Secret Key'
6. Configure Google Authentication keys in `settings.py`.
   ```bash
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'Your Google Auth Key'
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Your Google Auth Secret'
7. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
8. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
9. Run the development server:
    ```bash
   python manage.py runserver
10. Access the application at `http://localhost:8000/`.

## Usage

- Register as a new user or login with existing credentials (including Google OAuth2 login).
- Browse categories (e.g., Dog, Cat) and products, add them to the cart.
- Adjust quantities in the cart and proceed to checkout.
- Complete payment securely using Razorpay integration.
- Track order status and manage wishlists.
- Explore the Customer Profile section to manage personal information, addresses, and profile picture.
- Explore additional features such as About Us and Contact pages for more information.
- Download invoices for delivered products.

## Contributing

Contributions are welcome! Please follow GitHub's guidelines for pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

## LinkedIn Post

Here's a [LinkedIn post](https://www.linkedin.com/posts/sreenath-k-k-661840247_python-django-ecommerce-activity-7246390843492720640-oxmc?utm_source=share&utm_medium=member_desktop) where I shared more about it!