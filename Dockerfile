# Stage 1 - Builder

FROM python:3.14-slim AS builder

WORKDIR /app

COPY requirements.txt .
COPY wheelhouse /wheelhouse

RUN pip install \
    --no-index \
    --find-links=/wheelhouse \
    --prefix=/install \
    -r requirements.txt


# Stage 2 - Runtime
FROM python:3.14-slim

WORKDIR /app

COPY --from=builder /install /usr/local

COPY . .

EXPOSE 5000

CMD ["python", "run.py"]
