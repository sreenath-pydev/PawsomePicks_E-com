<img src="https://github.com/user-attachments/assets/fcb0d2ba-3af0-47a3-8a89-ff85ba92ce52" alt="PawsomePicks" width="200" height="200"> </br>
# Pawsome Picks - E-commerce Pets Product Purchasing Website 



Pawsome Picks is an e-commerce website dedicated to pet products, allowing users to browse, purchase, and manage their pet-related purchases conveniently. The website is built using Python and Django framework, with front-end development using HTML, CSS, and JavaScript (Bootstrap for responsive design). It includes various features such as user authentication, payment integration with Razorpay, PostgreSQL database for data management, and several user-centric functionalities like wishlists, cart management, order status tracking, and more.

## Features

- **User Authentication:** Secure user registration, login, logout, and authentication using Django's built-in authentication system.
  
- **Password Management:** Users can reset and change passwords securely.

- **Wishlist Management:** Authenticated users can add and remove products from their wishlist for future reference.

- **Shopping Cart:** Fully functional shopping cart with plus and minus buttons to adjust quantities, calculating total amounts dynamically.

- **Order Management:** Users can view their order status and history, providing transparency and tracking.

- **Search Functionality:** Dedicated search bar to find specific products and related items based on user queries.

- **Admin Features:** Only authenticated admin users can add products, manage inventory, and view site analytics.

- **Static Pages:** About and Contact pages provide information about the website and facilitate communication with users.

- **Footer:** Detailed footer with links to important pages, social media, and contact information for enhanced user experience.

## Technologies Used

- **Backend:** Python, Django, PostgreSQL
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Payment Integration:** Razorpay for secure and seamless payment processing

## Installation

1. Clone the repository:
   ```bash
    git clone https://github.com/Sreenathkk00/Ecommerce_project01.git
3. Install dependencies:
   ```bash
    pip install -r requirements.txt
4. Configure PostgreSQL database settings in `settings.py`.

5. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
7. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
9. Run the development server:
    ```bash
   python manage.py runserver
11. Access the application at `http://localhost:8000/`.

## Usage

- Register as a new user or login with existing credentials.
- Browse categories (e.g., Dog, Cat) and products, add them to the cart.
- Adjust quantities in the cart and proceed to checkout.
- Complete payment securely using Razorpay integration.
- Track order status and manage wishlists.
- Explore additional features such as About Us and Contact pages for more information.

## Contributing

Contributions are welcome! Please follow GitHub's guidelines for pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
