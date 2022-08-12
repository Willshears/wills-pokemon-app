# Pokemon Crawler

Project started from https://docs.docker.com/compose/django/

Some useful commands:

* `docker-compose up`
* `docker-compose exec web bash`
* `docker-compose exec web python -m pip install -r requirements.txt`
* `python manage.py migrate`
* `python manage.py makemigrations`

Design:
With the design, I kept it relatively simple and planned to create a schema with the pokemon name, height, weight, health, attack, defense, sprite, moves and types.
I realised afterwards this is more than suggested but since they are in the same API request and make sense together (height/weight, attack/defense) I left them in there for now.
Due to the large amount of data being processed, I opted to use normalisation to reduce redundant data. There are many abilities and types for each Pokemon, but the only relationship is the Pokemon itself.
Therefore, I divided the data into 3 tables: Pokemon(name, height, weight, health, attack, defense, sprite), Type(pokemon_name, type), Ability(pokemon_name, ability). 


Implementation:
I created a function based view and kept the scraper logic seperate from the view function. There are two API requests being made within the function - the first one returns the pokemon names and URLS, and the second one utilises the pokemon URLS gathered and
queries them for the specified attributes. Using the get_or_update function on the database ensures that both new pokemon are added and existing values are updated. Furthermore, several checks are in place to make sure the expected response is received and no duplicates are being entered.
To display the Pokemon relations, I used prefetch_related with the tags provided in the models.py. I used a TDD approach, with 2 methods. When developing, I often create and run isolated functions in a seperate .py file to manually check for issues and to ensure everything is working correctly, this 
allows for quickly finding the key issues along the way. In addition to this, some unit tests have been demonstrated, which ensure the server responds correctly, and to ensure the relationships are correct between the tables.

Scaling:
When running in development mode, more complex features would likely make it unusable due to the scraper function. However, I have a few ideas on how it could be improved if it was being developed into a production app. The scraper function could run asyncronously, perhaps as part of a microservice or serverless function. Ideally, this 
would return all of the values in a single dictionary, which could then be cross-referenced with the previous one. If there have been no changes in Pokemon attributes, there would be no need to run the get_or_create function with the data. In addition to this, bulk create or update could be implemented to save resources, at the expense of being able to rapidly update the newly caught pokemon.