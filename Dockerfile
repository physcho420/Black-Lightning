FROM python:3.9
RUN mkdir LIGHTNING-UB
COPY . /LIGHTNING-UB

ENV  PYTHONPATH "${PYTHONPATH}:/LIGHTNING-UB"


COPY requirements.txt .

COPY . .


RUN apt -qq update -y

RUN apt -qq install -y --no-install-recommends \
    coreutils \
    bash \
    bzip2 \
    curl \
    tesseract-ocr \
    tesseract-ocr-eng \
    imagemagick \
    figlet \
    gcc \
    g++ \
    git \
    libevent-dev \
    libjpeg-dev \
    libffi-dev \
    libpq-dev \
    libsqlite3-dev \
    libwebp-dev \
    libgl1 \
    musl \
    neofetch \
    libcurl4-openssl-dev \
    postgresql \
    postgresql-client \
    postgresql-server-dev-all \
    openssl \
    mediainfo \
    wget \
    python3-pip \
    libreadline-dev \
    zipalign \
    sqlite3 \
    ffmpeg \
    libsqlite3-dev \
    axel \
    zlib1g-dev \
    recoverjpeg \
    zip \
    megatools \
    libfreetype6-dev \
    procps \
    imagemagick \
    libmagic-dev \
    policykit-1


RUN pip3 install -U tgcrypto
RUN wget http://www.cmake.org/files/v2.8/cmake-2.8.3.tar.gz && tar xzf cmake-2.8.3.tar.gz && cd cmake-2.8.3 && ./configure --prefix=/opt/cmake && make install
RUN axel https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && apt install -y ./google-chrome-stable_current_amd64.deb && rm google-chrome-stable_current_amd64.deb
RUN axel https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && chmod +x chromedriver && mv -f chromedriver /usr/bin/ && rm chromedriver_linux64.zip
RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/master.zip && unzip opencv.zip && mv -f opencv-master /usr/bin/ && rm opencv.zip
RUN  pip3 install --no-cache-dir -r requirements.txt
CMD ["python3", "-m", "system"]
