# Flask App Pipeline
This repository contains a Flask web application enhanced with database interaction, authentication, rate limiting, and integrated with a CI/CD pipeline using GitHub Actions.

### Features
- Database Integration: Uses SQLite for storing user data.
- Authentication: Basic HTTP authentication for protecting routes.
- Rate Limiting: Limits the number of requests to prevent abuse.
- CI/CD Pipeline: Integrated with GitHub Actions for continuous integration and deployment.

### Setup Instructions
Prerequisites
- Python 3.8 or higher
- Docker and Docker Compose
- Git

### Local Development
Clone the repository:
```
git clone https://github.com/talitz/flask-app-prod-pipeline.git
cd flask-app-prod-pipeline
```

#### Create a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

#### Install dependencies:
```pip install -r requirements.txt``` 

#### Set up environment variables:
Copy the example environment file and adjust the variables as needed.

#### Run the application:
```python3 -m flask --app src/app run --port 5000 --debug```

The application will be available at http://127.0.0.1:5000.

#### Local Development using Docker

To build the Docker image for the Flask application, navigate to the root directory of the project where the Dockerfile is located and run the following command:

```docker build -t flask-app:latest .```

This command will build a Docker image named flask-app based on the instructions in the Dockerfile.

Once the image is built, you can run the container using the following command:

```docker run -p 5001:5000 flask-app```

This command starts the container and maps port 5000 inside the container to port 5001 on your local machine.

You can access the Flask application by navigating to the following URL in your web browser: http://127.0.0.1:5001/
