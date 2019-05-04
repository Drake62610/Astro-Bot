FROM python:3.7.3

RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list
RUN apt-get update 

RUN pip install discord
RUN pip install feedparser
RUN pip install pytumblr
RUN pip install recastai

CMD ["python", "Astro-Bot/main.py"]
