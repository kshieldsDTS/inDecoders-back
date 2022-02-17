# inDecoders-back

The Heroku deployed back end for the inDecoders app. Utilizes the Django REST Framework to make navigating and adding posts easier.

### Installation

Fork and clone down this repository. You will need to use `pipenv shell` to start a shell before working with the app. You will need to create a `.env` and add a Django Secret Key to it. You can then run `python3 manage.py runserver` to run the server. Navigate to `localhost:8000` to test out the endpoints and functionality.

### Endpoints

`/users` - Endpoint for POSTing new users.
`/getusers` - Endpoint for GETing all users.
`/getusers/:id` - Endpoint for GETing, PUTing, and DELETEing a specific user by ID.
`/LFWork` - Endpoint for GETing and POSTing seeker posts.
`/LFWork/:id` - Endpoint for GETing, PUTing, and DELETEing a specific seeker post by ID.
`/LFHelp` - Endpoint for GETing and POSTing project posts.
`/LFHelp/:id` - Endpoint for GETing, PUTing, and DELETEing a specific project post by ID.
