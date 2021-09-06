FROM    python:3.8-alpine

WORKDIR /app

COPY    . .

RUN     apk update && apk add ffmpeg \
	&& pip install -r requirements.txt

ENTRYPOINT ["python", "converter.py"]
