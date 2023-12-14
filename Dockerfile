# otherShipAIS.py
FROM python:3.11.0

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ais20171001_top5 /app/ais20171001_top5
COPY otherShipAIS.py .

CMD ["python", "otherShipAIS.py"]

# TCPA_server.py
# FROM python:3.11.0

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY TCPA_server.py .

# CMD ["python", "TCPA_server.py"]
