FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    fonts-liberation \
    libappindicator3-1 \
    xdg-utils \
    libxrandr2 \
    libxss1 \
    libnss3 \
    libgtk-3-0 \
    libgconf-2-4 \
    libasound2 \
    libpangocairo-1.0-0 \
    libpangoft2-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

ENV DISPLAY=:99
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT ["pytest", "--alluredir=reports"]

EXPOSE 4444