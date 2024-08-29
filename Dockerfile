FROM python:3.10-slim

# Install curl and sqlite3
RUN apt-get update && apt-get install -y \
    curl \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

COPY src/ /app/src/

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/src/db \
    && sqlite3 /app/src/db/flask_app.db "" \
    && chown -R 100000:100000 /app/src/db

USER 100000

EXPOSE 5000

# Command to run the application
CMD ["python3", "-m", "flask", "--app", "src/app", "run", "--host=0.0.0.0"]
