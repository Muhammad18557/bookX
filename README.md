## README for the P2P Book Exchange Platform POC
### Introduction
This README outlines the development and features of the Peer-to-Peer (P2P) Book Exchange Platform Proof of Concept (POC). Designed to revolutionize the way book enthusiasts share and discover books, this platform leverages a Tinder-like mechanism to connect users based on shared interests in books. Given a limited timeframe and concurrent academic commitments, the POC demonstrates foundational features with scope for future enhancements.

### Background and Challenges
In the face of academic deadlines, with three university assignments due, the development of this POC was constrained to a single night out of the two days initially allocated. Despite these time constraints, the project was embarked upon with the goal to create a functional, albeit foundational, product that addressed the need for a streamlined book exchange process.

## Core Features
### User Authentication and Profile: 
Register and login capabilities to ensure user data is secured and personalized. Ability to view and edit user profile that also maintains a collection of books.
### Book Listings: 
Users can list books they wish to exchange, including details like title, author, genre, and personal ratings.

### Liking/Unliking a book (AJAX-driven Interactions):
For a seamless user experience, AJAX is used for liking and unliking books, preventing full page reloads on a like/unlike.

### Matchmaking Algorithm: 
A Tinder-inspired mechanism where users 'like' books of interest. Mutual likes between users suggest a potential exchange.

## Technologies Used
### Flask: 
A micro web framework for Python, chosen for its simplicity and flexibility in developing web applications.
### Jinja Templates: 
Used for frontend rendering, allowing dynamic content display based on backend data.
### SQLite3: 
A lightweight database for storing user and book data, coupled with SQLAlchemy for ORM abstraction.
### Bcrypt for Flask: 
Ensures secure storage of user passwords through hashing.

### Setup and Installation
Optional but recommended - Create a virtual environment for the project to manage dependencies.
```
python -m venv venv
```
Install the required dependencies using pip.
```
pip install -r requirements.txt
```
### Running the Application
To run the application, execute the following command in the terminal with some port number e.g. 9000.
```
python runserver.py <port_number>
```
### Database Initialization
I have already created a database with some test records under instance/book_exchange.db. If you wish to start with a fresh database, delete the existing database and run the following command.
```
python models.py
```

### Accessing the Application
Access the application through the following URL in your browser, replacing <port_number> with the port number specified during execution:
```
http://localhost:<port_number>
```
### Testing Credentials (If using the provided database file)
Use the following credentials to test the application:
```
Email: bdllharshad@gmail.com
Password: 123456910
```
```
Email: shaheer@gmail.com
Password: 123456910
```

### Achievements and Future Plans
Given the constrained development period, the project lays a solid foundation with key functionalities implemented. Future enhancements would focus on:

### AI-Generated Summaries:
Enabling users to generate summaries of books using AI, adding value to book listings.

### Enhanced Dashboard and Recommendations: 
Displaying potential matches and recommendations based on user preferences and book collections.

### Advanced Search Features: 
Improving search functionality with AJAX for real-time filtering and results.



Acknowledgments
Special thanks to those who understand the balancing act between academic responsibilities and passion projects. This POC stands as a testament to what can be achieved with dedication and a clear vision, even within tight constraints.

