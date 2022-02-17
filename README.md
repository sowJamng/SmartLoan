# Flask backend API

## Development server 
# Students

# Maodo Laba SOW
# Mehdi Semllami
# Alexis Sidate
# Jouhaina Sahnoun

** Create Pojet **
`mkdir backen`
`python -m venv .\venv`
`.\ven\Scripts\activate`
`pip install flask`
`pip install scikit-learn`

Run `python app.py` to start development server on port `8081` to watch files and restart on update.

## Use from docker container

Clone project on your remote machine (needs to have docker daemon installed), then build image (`docker build -t flask-backend .`) and finally run the image by using `docker run -p 8081:8081 -v /HOST/PATH/TO/BACKEND/FOLDER:/app flask-backend`.
