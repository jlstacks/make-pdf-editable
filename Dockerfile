FROM debian:trixie-slim
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        ocrmypdf poppler-utils tesseract-ocr qpdf \
    && rm -rf /var/lib/apt/lists/*
ENV HOME=/tmp
WORKDIR /tmp
ENTRYPOINT ["ocrmypdf"]
