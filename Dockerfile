# Build Stage - Development Environment

FROM python:3.9-slim as builder

RUN apt-get update && apt-get install -y \

gcc \

g++ \

make \

curl

WORKDIR /app

COPY requirements.txt .

RUN pip install --user -r requirements.txt

COPY src/ ./src/

RUN python -m compileall src/

# Runtime Stage - Production Environment

FROM python:3.9-slim as runtime

WORKDIR /app

COPY --from=builder /root/.local /root/.local

COPY --from=builder /app/src/ ./src/

ENV PATH=/root/.local/bin:$PATH

CMD ["python", "src/main.py"]







# # Parallel build stages for different components

# FROM maven:3.8-jdk-11 as spark-builder

# # Spark application compilation

# FROM python:3.9 as ml-builder

# # ML model training and serialization

# FROM node:16 as config-builder

# # Configuration processing

# # Runtime combines selective outputs

# FROM openjdk:11-jre-slim as runtime

# COPY --from=spark-builder /app/target/*.jar ./lib/

# COPY --from=ml-builder /app/models/ ./models/

# COPY --from=config-builder /app/config.json ./
