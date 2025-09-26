FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir poetry
RUN poetry install --no-root
CMD ["poetry", "run", "python", "main.py"]
