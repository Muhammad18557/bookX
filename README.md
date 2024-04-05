## P2P Book Exchange Platform POC
### Introduction
This README outlines the development and features of the Peer-to-Peer (P2P) Book Exchange Platform Proof of Concept (POC). Designed to revolutionize the way book enthusiasts share and discover books, this platform leverages a Tinder-like mechanism to connect users based on shared interests in books. Given a limited timeframe and concurrent academic commitments, the POC demonstrates foundational features with scope for future enhancements.

### Background and Challenges
In the face of academic deadlines, with three university assignments due, the development of this POC was constrained to a single night out of the two days initially allocated. Despite these time constraints, the project was embarked upon with the goal to create a functional, albeit foundational, product that addressed the need for a streamlined book exchange process.

## Core Features

### User Authentication and Profile: 
Register and login capabilities to ensure user data is secured and personalized. Ability to view and edit user profiles on unique routes that also maintain a collection of their books.
### Book Listings, Search, Book Page: 
Users can list books they wish to exchange, including details like title, author, genre, and personal ratings. These books then go to the market place which is at the home page of the website. Users can search for books in general (e.g. by name) or do an advanced search based on title, author, and/or genre. Each book card can be clicked to view more details speicifically on the dedciated route of the book.


### Dashboard:
A personalized dashboard for each user, displaying the booked they liked, potential matches, and exchnage history. The dashboard is a central hub for user activity, providing a seamless experience for book exchange. This is the point of increasing user engagement and retention. The dashboard is a key feature that will keep users coming back to the platform. There is a lot of room for improvement and achievement in the dashboard. More about the sepcific parts in the following points.

### Liking/Unliking a book (AJAX-driven Interactions):
A user can express interest in a book by liking it on the listing. If no longer intersted or pressed by mistake, they can also unlike it to delete that like. For a seamless user experience, AJAX is used for liking and unliking books, preventing full page reloads on a like/unlike.

### Matchmaking Algorithm: 
A Tinder-inspired mechanism where users 'like' books of interest. Mutual likes between users suggest a potential exchange. This feature is a key differentiator, enhancing user engagement and facilitating book exchanges. Based on the likes, the user is shown a list of all possible matches on the dashboard. However, when we scale up, we can use a more sophisticated algorithm to show only the best matches. For now, if a match is possible, the user is shown a match button which will simulate the exchange of books. However, the way to go would be to notify both users and let them decide if they want to exchange books with a final confirmation.

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

### Enhanced Dashboard and Recommendations: 
Displaying potential matches and recommendations based on user preferences and book collections. Introduce rewards based on user engagement and some metric like exchange rate. Furthermore, exchanges should be rated to make sure users maintain a good reputation when meeting to physically exchange the books.

### Notifications and Messaging:
Implementing notifications for matches and messaging capabilities for users to communicate. This will make the platform more interactive and engaging.

### Introduction of Communities and Forums:
Creating communities and forums for users to discuss books, share recommendations, and engage with like-minded individuals. This can be like a virtual reading club where users can discuss books they have read or are reading. This is essentially an extension of notifications and messaging where we make it more advanced and interactive. E.g. a sart thread feature for a book where users can discuss the book. 

### AI-Generated Summaries:
Enabling users to generate summaries of books using AI, adding value to book listings.

### Advanced Search Features: 
Improving search functionality with AJAX for real-time filtering and results.

### Scalability and Performance:
Optimizing the platform for scalability and performance, ensuring seamless user experience. The match making algorithm can be improved to show only the best matches.

## Acknowledgments
I thank the team at heymax for giving me a chance to work on this project. Despite the clash with school assignments, I enjoyed the challenge and look forward to future collaborations.

