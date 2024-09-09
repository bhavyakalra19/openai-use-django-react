Overview:
As passionate travelers, managing our favorite places across different cities has become a tedious and manual task. This application aims to streamline this process by developing a web application that leverages OpenAI to curate and manage a list of must-see locations in any given city. This user-friendly platform will enhance trip planning by offering efficient access to a city's top destinations.

Your main goals to accomplish are,
Backend Development
Construct a server using Node.js and Express (or a similar framework) to interact with OpenAI's API. This server will retrieve a curated list of popular places to visit in a specified city.
Store the retrieved data within a local database solution like sqlite or MongoDB.
Frontend Development
Develop a user interface using React (with TypeScript) that allows users to input new places and display the list of favorite places fetched from the server.
Implement functionalities to view details of existing places, and delete entries(Use any React Router for navigation)

  Note:
Leverage Best Practices and Modular Components.
Ensure secure handling of API keys and interactions with the OpenAI API.
Clear instructions and commands should be provided for setting up and running both the backend server and the frontend application.

For Django installation:-
Create virtual env and run
1. pip install openai
2. pip install djangorestframework
3. pip install python-dotenv
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py runserver
7. Add your open ai key in  .env file

For ReactjS
1. npm install
2. npm start
