# <div align="center">CRM System</div>

Utilized for creating quotes, storing clients and calls record. This app was 
specifically designed for a pool repairment company. All different quotations 
can be printed into a template Word file.

This app is more Object Oriented than my other ones since I wanted to further 
develop this particular way of programming.

## Tech Stack

* Python
* PostgreSQL
* Tkinter

## Quickview

![Screenshot of the site](https://marcosnapolitano.github.io/Assets/todo-aqua.webp)

## Quickstart

*Make sure Python, PostgreSQL and Venv are installed on your OS.*

1. Fork the project.
2. Clone project using `git clone git@github.com:<YOUR-USERNAME>/sistema_todoaqua.git`.
3. Navigate into the project using `cd sistema_todoaqua`.
4. Create a new Virtual Enviroment in this directory 
5. Run `source bin/activate`.
6. Run `pip3 install -r requirements.txt`.
7. These next step run a template database for the App. Log into PSQL and run:

    ```SQL
    CREATE DATABASE aqua;
    CREATE USER 'my_user' WITH ENCRYPTED PASSWORD 'my_password';
    GRANT ALL PRIVILEGES ON DATABASE aqua to aqua
    DROP SCHEMA public CASCADE;
    CREATE SCHEMA public;
    GRANT ALL ON SCHEMA public TO aqua;
    CREATE EXTENSION IF NOT EXISTS adminpack;
    ```
8. Finally run `pg_restore -U aqua -d aqua -W -v --no-owner --role=aqua "./BBDD/aqua_with_samples.sql"`

*Disclaimer: you need to generate your own env password variable.*

## Docs

All logic contained in the `src/app` folder.

* **BBDD**: Database templates and connection logic. 
* **Gui**: All gui elements made with **Modern Tkinter**.
* **Models**: This is where all main classes live, client, call, quotes, etc.
* **Output**: Path used for saving quotes.
* **Services**: Utilities functions, quotes generators and database queries.
* **Templates**: Template docx files for the app.

### App Main Idea

This particular company required a CRM to gather client's info and, according 
to said info, generate a quote. This quotes were very specific as this was a
pool repairment company, which derived in the idea of creating a quote 
generating system which focused only on gathering the client's and pool's details. 
The remaining info present on the quotes stays always the same hence the use of
templates.

This system gave way to an important increase in office productivity since it 
eliminated the need of constantly formatting quotes and manually keep track of them.
