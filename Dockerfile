FROM python:3.9-slim AS builder
ADD . /app
WORKDIR /app
RUN pip install --target=/app -r requirements.txt

FROM python:3.9-slim
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH /app

ENTRYPOINT ["python","/app/main.py"]
