# Pornim de la o imagine oficiala Python
FROM python:3.12-slim

# Setăm un director de lucru în interiorul containerului
WORKDIR /app

# Copiem mai întâi specificația dependențelor (pentru layer caching — explicat mai jos)
COPY requirements.txt .

# Instalăm dependențele
RUN pip install -r requirements.txt

# Copiem restul codului sursă
COPY . .

# Comanda implicită când containerul pornește
CMD ["python", "main.py"]
