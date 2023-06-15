# Governor's Bowl Fantasy Football League - Web Application

This project is a Flask-based web application for the Governor's Bowl Fantasy Football League. It's designed to provide all-time, yearly, and seasonal stats about the league owners and teams.

## Table of Contents

- [Project Overview](#project-overview)
- [Pages](#pages)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Contributing](#contributing)
- [Contact](#contact)

## Project Overview

This web application is a comprehensive platform for all Governor's Bowl Fantasy Football League data. It presents users with data about all-time stats, detailed yearly stats, and in-depth season recaps. It also provides visualizations of various statistical data.

The back-end of the application is powered by Flask, while the front-end uses HTML and CSS (using Bootstrap framework) for structuring and styling, respectively. Data is read from CSV files, processed using Pandas library, and then displayed on the web pages.

## Pages

The application consists of several HTML pages, each serving a specific purpose:

- `index.html` : The Home page, which provides all-time stats about the league.
- `owner.html` : Page for each owner that showcases their all-time stats and yearly results.
- `season_recaps.html` : A dedicated page for each season. Here, you can view the recap of that year, showing details like the Champion, Sacko, and other relevant statistics.

## Technologies Used

This application has been built using various technologies, frameworks, and libraries:

- **Python**: A powerful, flexible, and easy-to-learn programming language that serves as the backbone of this project.
- **Flask**: A micro web framework written in Python. It's minimalistic and easy to use, and it's what powers the back-end of this application.
- **SQLite**: A C library that provides a lightweight disk-based database. It allows accessing the database using a nonstandard variant of the SQL query language. In this project, it's used to store and retrieve data needed for the application.
- **Flask-SQLAlchemy**: An extension for Flask that adds support for SQLAlchemy to your application. It simplifies the application's interaction with databases by providing helpful defaults and extra helpers that make it easier to accomplish common tasks.
- **Pandas**: A software library for data manipulation and analysis. In this project, it's used to process the CSV data files.
- **HTML/CSS**: Used for structuring and styling the front-end of the application. HTML provides the basic structure of pages, which is enhanced and styled by CSS.
- **Bootstrap**: A popular HTML, CSS, and JavaScript framework for developing responsive, mobile-first websites. It's used in this project for efficient and attractive front-end design.

## Installation

- Clone the repo to your local machine.
- Make sure you have Python 3.6+ and Pip installed.
- Install the required Python libraries by running `pip install -r requirements.txt`.
- Start the Flask server by running `python app.py`.

## Usage

Open your browser and go to `http://localhost:5000`. This will open the Home page of the application.

- `/` : Home page that shows all-time statistics.
- `/owner/<owner_name>` : Page for each owner that shows their all-time stats and yearly results.
- `/season_recaps/<year>` : Season recap page for each year showing the Champion, Sacko, and other stats.

## Development

To work on the project:

1. Clone the repository to your local machine.
2. Create a new branch.
3. Make your changes.
4. Push your changes to the branch.
5. Create a pull request.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## Contact

For any questions or contributions, please don't hesitate to reach out. Unless its Bernie, keep it to yourself Bernie. 
