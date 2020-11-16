# secure_backend
<div>
<h1>Install Dependencies</h1>
Install project dependencies:
<b>$ pip install -r requirements/local.txt</b>

Install postgresql:<b>https://www.postgresql.org/download/</b>
</div>
<div>
<h1>To Start</h1>
Then simply apply the migrations:
<b>$ python manage.py migrate</b>

You can now run the development server:
<b>$ python manage.py runserver</b>

To change the model schema:

<p align="center">
    <img src="./readme_src/model.png"></img>
</p>
</div>


# How to run and test for the testing team
1. Install docker and docker-compose in your machine
2. Extract the postgres-data.zip into the root directory
    - The folder should be named `postgres-data` and the structure shold be like this
    ```
    [root]
    - postgres-data
      - base
      - global
      ...
    ``` 
3. Back to the root folder and run (Use sudo to make sure the data folder gets loaded correctly)
    ```
    sudo docker-compose up -d --build
    ```
4. The site shall be available at http://localhost:8000

5. Here are the credentials
    - `superuser:b+3;njAJg4>Af,7'` (superuser account)
    - `normaluser:b9wDh5mEDVjg3kd` (normal account)

ENJOY! 