# ⚽ Football Statistics Django Web App

A modern Django web application that displays live football statistics from major leagues around the world. Get real-time standings, match results, fixtures, and top scorer information for your favorite competitions.

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

## 🌟 Features

- **📊 Live League Standings** - View current league tables with team positions, points, goals, and statistics
- **⚽ Match Results & Fixtures** - Browse past results and upcoming matches with detailed information
- **🏆 Top Scorers** - Track leading goalscorers across different competitions
- **🔄 Real-time Data** - Automatic data fetching from football-data.org API with smart caching
- **📱 Responsive Design** - Mobile-friendly interface built with Bootstrap
- **🎯 Competition Filtering** - Filter matches by matchday and competition
- **⚡ Fast Performance** - Built-in caching system to minimize API calls and improve speed

## 🏟️ Supported Competitions

The app supports major football competitions including:
- Premier League (England)
- La Liga (Spain)
- Bundesliga (Germany)
- Serie A (Italy)
- Ligue 1 (France)
- UEFA Champions League
- And many more international competitions

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Django 4.0+
- Internet connection for API data

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Khalilozich123/Django-Web-App.git
   cd football-stats-django
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django requests
   ```

4. **Set up the database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and navigate to `http://localhost:8000`
   - Click "Refresh All" to fetch initial data from the API



## 🛠️ Project Structure

```
DjangoApp/
├── Statistics/
│   ├── StatApp/
│   │   ├── models.py          # Database models
│   │   ├── views.py           # View controllers
│   │   ├── services.py        # API integration service
│   │   ├── urls.py            # URL routing
│   │   ├── admin.py           # Django admin configuration
│   │   ├── templates/         # HTML templates
│   │   │   └── statapp/
│   │   │       ├── base.html
│   │   │       ├── home.html
│   │   │       ├── competition_detail.html
│   │   │       ├── matches.html
│   │   │       └── scorers.html
│   │   └── management/
│   │       └── commands/
│   │           └── update_football_data.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```



## 📊 Data Management

### Manual Data Update
Use the Django admin interface or click "Refresh Data" buttons in the web interface.

### Automated Data Updates
Run the management command:
```bash
# Update all competitions
python manage.py update_football_data --all

# Update specific competition (e.g., Premier League)
python manage.py update_football_data --competition=PL
```

### Scheduling Updates
For production, set up a cron job to update data regularly:
```bash
# Add to crontab for hourly updates
0 * * * * /path/to/venv/bin/python /path/to/project/manage.py update_football_data --all
```

