🎬 Cinema Management System

📝 Description

This project is a REST API built with Django Rest Framework for managing cinemas, movies, showtimes, tickets, and user feedback. It provides a comprehensive system for clients to explore available movies, cinemas, showtimes, and purchase tickets, while administrators can efficiently manage movies, cinemas, showtimes, and user feedback.
🚀
## Installation

1) Clone the repository:
```
git clone https://github.com/Oscardkyou/yourproject.git
```
2) Navigate to the project directory:
```
cd yourproject
```
3) Install dependencies:
```
pip install -r requirements.txt
```
4) Start the development server:
```
python manage.py runserver
```
📖 Usage
🎥 Movies

    Client: Browse a list of current and upcoming movies.
    Admin: Create, edit, and delete movies. Hide multiple movies at once.

🏢 Cinemas

    Client: View all cinemas, including their schedules, addresses, and contact information.
    Admin: Create, edit, and delete cinemas and their details.

🏛️ Rooms

    Client: After selecting a cinema and movie, view available rooms with time and seat information.
    Admin: Manage room details and availability.

💺 Seats

    Client: Reserve multiple seats for a showtime.
    Admin: Manage seat availability and configurations.

🎟️ Tickets

    Client: Purchase tickets for a showtime, specifying ticket prices, selected seats, and payment methods.
    Admin: Manage ticket sales and availability.

🗣️ Feedback

    Client: Provide feedback or suggestions about the service.
    Admin: Review and respond to client feedback.

💳 Discounts

    Client: Utilize a card-based discount system for ticket purchases.
    Admin: Manage discount policies and offers.

👥 Users

    Admin: Create, edit, and delete user accounts and records.
    Client: Regular users of the cinema management service.

⏰ Showtimes

    Client: View available movie showtimes at different cinemas.
    Admin: Create, edit, and delete showtime schedules.

📜 Purchase History

    Client: View a summary of their expenses, filterable by date range, with aggregated data (e.g., total spent).
    Admin: Access detailed purchase histories and analytics.

🛠️ Technologies Used

    Django: High-level Python web framework.
    Django Rest Framework: Powerful and flexible toolkit for building Web APIs.
    Postgres/SQLite: Databases for data storage (choose based on your preference).
    Postman: Tool for testing API endpoints.

🤝 Contributing
```
Contributions are welcome! Feel free to fork the repository and submit pull requests. You can also open issues to report bugs or suggest new features.
```
📚 Authors Dk