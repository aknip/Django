FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

ARG NODE_MAJOR=18

RUN apt-get update \
  && apt-get install -y ca-certificates curl gnupg \
  && mkdir -p /etc/apt/keyrings \
  && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
  && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list \
  && apt-get update \
  && apt-get install nodejs -y \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && useradd --create-home python \
  && chown python:python -R /app

USER python

COPY --chown=python:python requirements*.txt ./

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV DEBUG="${DEBUG}" \
    PYTHONUNBUFFERED="true" \
    PATH="${PATH}:/home/python/.local/bin" \
    USER="python"

COPY --chown=python:python . .

WORKDIR /app

RUN SECRET_KEY=nothing python manage.py tailwind install --no-input;
RUN SECRET_KEY=nothing python manage.py tailwind build --no-input;
RUN SECRET_KEY=nothing python manage.py collectstatic --no-input;

# running migrations
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver"]
