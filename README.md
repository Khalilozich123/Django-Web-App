⚽ Football Statistics Django Web App
Une application web moderne développée avec Django, permettant d'afficher en temps réel les statistiques des principaux championnats de football à travers le monde. Suivez les classements, les résultats, les matchs à venir, et les meilleurs buteurs de vos compétitions favorites.

🌟 Fonctionnalités
📊 Classements en direct : Affichage des tableaux de ligue avec les positions, points, buts et autres statistiques clés.

⚽ Résultats & Calendrier : Consultation des résultats passés et des matchs à venir avec des détails complets.

🏆 Meilleurs Buteurs : Suivi des meilleurs buteurs par compétition.

🔄 Données en temps réel : Récupération automatique des données via l'API football-data.org, avec système de cache intégré.

📱 Design Responsive : Interface mobile-friendly conçue avec Bootstrap.

🎯 Filtrage par compétition : Filtrage des matchs par journée et compétition.

⚡ Performance optimisée : Système de cache pour réduire les appels API et accélérer le chargement.


🧪 Installation
1. Cloner le dépôt
        git clone https://github.com/Khalilozich123/Django-Web-App.git
        cd Django-Web-App
2. Créer un environnement virtuel
        python -m venv venv
        source venv/bin/activate
3. Installer les dépendances
        pip install django requests
4. Configurer la base de données
        cd Statistics
        python manage.py makemigrations
        python manage.py migrate
5. Lancer le serveur
        python manage.py runserver
6. Accéder à l'application
        Ouvrez votre navigateur à l'adresse :
        👉 http://localhost:8000
        Cliquez sur "Refresh All" pour initialiser les données via l'API.


🛠️ Structure du projet
football-stats-django/
├── Statistics/
│   ├── StatApp/
│   │   ├── models.py             # Modèles de base de données
│   │   ├── views.py              # Contrôleurs de vues
│   │   ├── services.py           # Intégration avec l'API football-data
│   │   ├── urls.py               # Routage de l'application
│   │   ├── admin.py              # Configuration de l’interface d’admin Django
│   │   ├── templates/
│   │   │   └── statapp/
│   │   │       ├── base.html
│   │   │       ├── home.html
│   │   │       ├── competition_detail.html
│   │   │       ├── matches.html
│   │   │       └── scorers.html
│   │   └── management/
│   │       └── commands/
│   │           └── update_football_data.py  # Commande personnalisée pour maj API
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
   
