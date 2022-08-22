FROM python:3

WORKDIR /src

COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# тут нужно перейти в src
CMD [ "sh", "-c", "cd src && python main.py"]