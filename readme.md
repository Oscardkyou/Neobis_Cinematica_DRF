Cinema Management System
Description

This project is a REST API built with Django Rest Framework for managing cinemas, movies, showtimes, tickets, and user feedback. It allows clients to view available movies, cinemas, showtimes, and purchase tickets, while administrators can manage movies, cinemas, showtimes, and user feedback.
Installation

    Clone the repository: git clone https://github.com/yourusername/yourproject.git
    Install dependencies: pip install -r requirements.txt
    Run migrations: python manage.py migrate

Usage
Movies

    Client: View a list of current and upcoming movies.
    Admin: Create/edit/delete movies. Hide multiple movies at once.

Cinemas

    Client: View all cinemas, their schedules, addresses, and contacts.
    Admin: Create/edit/delete cinemas and their information.

Rooms

    Client: After selecting a cinema and movie, view available rooms.
        Includes time and seat information.

Seats

    Client: Reserve multiple seats.
    Admin: Manage seat availability.

Tickets

    Client: Purchase a limited number of tickets for a showtime.
        Specify ticket prices, selected seats, chosen showtime, and payment method.

Feedback

    Client: Provide feedback or suggestions.
    Admin: Review and respond to feedback.

Discounts

    Client: Utilize a card-based discount system.

Users

    Admins: Create/edit/delete almost any record on the website.
    Clients: Regular users of the service.

Showtimes

    Client: View available movie showtimes at cinemas.
    Admin: Create/edit/delete showtimes.

Purchase History

    Client: View a summary of their expenses.
        Filterable by date range, with aggregated data (e.g., total spent).

Technologies Used

    Django
    Django Rest Framework
    Postgres/SQLite (optional)
    Postman

Contributing

Contributions are welcome! Feel free to suggest new features or report issues.
Authors

    Your Name