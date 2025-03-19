FROM python:3.13-bookworm

WORKDIR /opt/app

RUN pip install uv

COPY pyproject.toml .
COPY uv.lock .
COPY .python-version .

RUN uv sync

COPY . .

CMD ["uv", "run", "gunicorn", "app.wsgi:application"]