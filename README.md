# Movie App
This app gives details about movies and also users can use this for making their movie collections.
## Quickstart

Create VirtualEnv:
   ```bash
   $ python3 -m venv env
   ```
  
1. Clone and install dependencies

    ```bash
    $ git clone https://github.com/swatisom1612/Movie-API.git
    $ cd Movie-API
    $ pip install -r requirements.txt
    ```
2. Install and run Redis and Celery

I used here custom middleware where through celery task I am incrementing request counter in redis database.

   To install Redis-Celery for this project, follow these steps- https://stackabuse.com/asynchronous-tasks-in-django-with-redis-and-celery/.
   
   
3. Exporting environment variables
 ```bash
   $ export MOVIE_LIST_API_CLIENT_SECRET='Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1'
   $ export MOVIE_LIST_API_CLIENT_ID='iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0'
   ``` 

4. Running app

   ```bash
   $ manage.py makemigrations movie 
   $ manage.py makemigrations user 
   $ python manage.py migrate
   $ python manage.py runserver
   ```  

## API Documentation 

### `This Endpoint takes username and password and registers and gives the access token` 

1. `POST /user/register/` 

```bash
 application/json - {
    "username": "username:,
    "password": "password",
}
```
##### `response`

```bash
{
   "access_token": "access token"
}   
```
2. `POST /user/login/` 

```bash
 application/json - {
    "username": "username:,
    "password": "password",
}
```
##### `response`

```bash
{
   "access_token": "access token"
}
    
```
##### `For all the requests we would use this access token for authentication and permission in headers request`
```bash
   Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9
    
```
    

### `This Endpoint gives the list of movies from third party API with pagination support ` 

1. `GET /movies/` 

##### `response`

```bash
 application/json - {
 “count”: <total number of movies>,
 “next”: <link for next page, if present>,
 “previous”: <link for previous page>,
 “data”: [
 {
 “title”: <title of the movie>,
 “description”: <a description of the movie>,
 “genres”: <a comma separated list of genres, if
present>,
 “uuid”: <a unique uuid for the movie>
 },
 ...
 ]
}
```

### `This Endpoint takes movie collection and stores them and also returns top 3 genres` 

1. `POST /collection/` 

```bash
 application/json - {
 “title”: <Title of the collection>,
 “description”: <Description of the collection>,
 “movies”: [
 {
 “title”: <title of the movie>,
 “description”: <description of the movie>,
 “genres”: <generes>,
 “uuid”: <uuid>
 }, ...
 ]
}
```
##### `response`

```bash
{
 “collection_uuid”: <uuid of the collection item>
}   
```
2. `PUT /collection/<collection_uuid>/` 

```bash
 application/json - {
 “title”: <Optional updated title>,
 “description”: <Optional updated description>,
 “movies”: <Optional movie list to be updated>,
}
```
##### `response`

```bash
{
 “title”: <Title of the collection>,
 “description”: <Description of the collection>,
 “movies”: <Details of movies in my collection>
5
}
    
```
3. `DELETE /collection/<collection_uuid>/` 


##### `response`

```bash
{"message": "Collection deleted successfully!"}
    
```
4. `GET /collection` 

##### `response`

```bash
 application/json - {
 “is_success”: True,
 “data”: {
 “collections”: [
 {
 “title”: “<Title of my collection>”,
 “uuid”: “<uuid of the collection name>”
 “description”: “My description of the collection.”
 },
 ...
 ],
 “favourite_genres”: “<My top 3 favorite genres based on the
movies I have added in my collections>.”
 }
}
```
### `This Endpoint return the number of requests which have been served by the server and resets it` 

1. `GET /request-count/` 

```bash
 application/json - {
 “requests”: <number of requests served by this server till now>.
}
```
##### `response`

```bash
{
   "request_count": "request_count"
}   
```
2. `POST /request-count/reset/` 

##### `response`

```bash
{
 “message”: “request count reset successfully”
}
    
```
