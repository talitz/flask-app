FROM python:3.10-slim

# Install curl and sqlite3
RUN apt-get update && apt-get install -y \
    curl \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /src

COPY requirements.txt .

COPY src/ src/

RUN pip install --no-cache-dir -r requirements.txt \
    && mkdir -p /src/db \
    && sqlite3 /src/db/flask_app.db "" \
    && chown -R 100000:100000 /src/db

USER 100000

EXPOSE 5000

CMD ["python3", "-m", "flask", "--app", "src", "run", "--host=0.0.0.0"]
