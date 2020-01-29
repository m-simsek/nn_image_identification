FROM python:3

RUN pip install --upgrade pip && \
    pip install matplotlib && \
    pip install numpy && \
    pip install scikit-image && \
    pip install torch && \
    pip install pandas && \
    pip install progress && \
    pip install torchvision && \
    pip install Pillow==6.0 && \
    pip install XlsxWriter

WORKDIR '/nn_image_identification'

ADD . /nn_image_identification

CMD [ "python", "/nn_image_identification/main.py" ]

LABEL maintainer="m.simsek"


