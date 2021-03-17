FROM python:3.8.5-buster as base
FROM base as builder
WORKDIR /build
COPY requirements.txt .
RUN apt-get update && apt-get install -y python3-dev python3-rpi.gpio && pip3 wheel -r requirements.txt

FROM python:3.8.5-slim-buster as prod
COPY --from=builder /build /wheels
RUN pip install -U pip \
    && pip install --no-cache-dir \
    -r /wheels/requirements.txt \
    -f /wheels \
    && rm -rf /wheels
WORKDIR /app
COPY . .
CMD ["python3", "pifan.py"]