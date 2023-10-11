FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime

WORKDIR /tmp

# hadolint ignore=DL3008
# hadolint ignore=DL3013
RUN apt-get update \
    && apt-get install --no-install-recommends -y bash \
    build-essential \
    git \
    curl \
    wget \
    ca-certificates \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists \
    && python3 -m pip install --no-cache-dir --upgrade pip \
    && chmod 1777 /tmp \
    && sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" -- \
    -t https://github.com/denysdovhan/spaceship-prompt \
    -a 'SPACESHIP_PROMPT_ADD_NEWLINE="false"' \
    -a 'SPACESHIP_PROMPT_SEPARATE_LINE="false"' \
    -p git \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-completions \
    && rm -rf /tmp

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=$PYTHONPATH:/app

WORKDIR /app

COPY requirements.txt .
COPY src src

RUN pip install --no-cache-dir -r requirements.txt
