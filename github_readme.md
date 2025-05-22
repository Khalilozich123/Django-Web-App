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
   git clone https://github.com/yourusername/football-stats-django.git
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

## 📸 Screenshots

### Home Page - Competition Selection
![Competition List](https://via.placeholder.com/800x400/0066cc/ffffff?text=Competition+Selection+Page)

### League Standings
![Standings](https://via.placeholder.com/800x400/28a745/ffffff?text=League+Standings+Table)

### Match Results & Fixtures
![Matches](https://via.placeholder.com/800x400/ffc107/000000?text=Match+Results+%26+Fixtures)

### Top Scorers
![Top Scorers](https://via.placeholder.com/800x400/dc3545/ffffff?text=Top+Scorers+Leaderboard)

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

## 🔧 Configuration

### API Setup

The application uses the football-data.org API. The current setup includes a free API key, but for production use:

1. Register at [football-data.org](https://www.football-data.org/client/register)
2. Get your API key
3. Update the `FOOTBALL_API_KEY` in `settings.py`

### Environment Variables (Recommended for Production)

Create a `.env` file in your project root:
```env
FOOTBALL_API_KEY=your_api_key_here
DEBUG=False
SECRET_KEY=your_secret_key_here
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

## 🎨 Customization

The app uses Bootstrap 5 for styling. You can customize the appearance by:
- Modifying the CSS in `templates/statapp/base.html`
- Updating the color scheme and components
- Adding custom JavaScript for enhanced interactions

## 🧪 Testing

Run the Django test suite:
```bash
python manage.py test
```

## 📱 Mobile Support

The application is fully responsive and works seamlessly on:
- Desktop computers
- Tablets
- Mobile phones

## 🔒 Security Notes

- The API key is currently hardcoded for demonstration purposes
- For production deployment, use environment variables
- Enable HTTPS in production
- Configure proper CORS settings if needed

## 🚀 Deployment

### Local Development
Follow the Quick Start guide above.

### Production Deployment
1. Set up environment variables
2. Configure a production database (PostgreSQL recommended)
3. Set `DEBUG = False` in settings
4. Configure static files serving
5. Use a production WSGI server like Gunicorn
6. Set up a reverse proxy with Nginx

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Ensure responsive design compatibility

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [football-data.org](https://www.football-data.org/) for providing the football data API
- [Bootstrap](https://getbootstrap.com/) for the responsive UI framework
- [Font Awesome](https://fontawesome.com/) for the icons
- Django community for the excellent web framework

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the [Django documentation](https://docs.djangoproject.com/)
- Visit the [football-data.org API documentation](https://www.football-data.org/documentation/quickstart)

## 🗺️ Roadmap

Planned features for future releases:
- [ ] Player statistics pages
- [ ] Match prediction system
- [ ] User favorites and notifications
- [ ] Team comparison tools
- [ ] Historical data analysis
- [ ] API endpoint for mobile apps
- [ ] Multi-language support

---

⭐ **If you find this project helpful, please give it a star!** ⭐

Made with ❤️ and ⚽ by [Your Name]