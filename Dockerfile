FROM mcr.microsoft.com/playwright/python:v1.47.0-noble

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps

CMD ["pytest"]
