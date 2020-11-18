FROM python:3.8

# Download and extract ifcopenshell
RUN wget --quiet https://s3.amazonaws.com/ifcopenshell-builds/ifcopenshell-python-38-v0.6.0-b08346c-linux64.zip
RUN unzip -q ifcopenshell-python-38-v0.6.0-b08346c-linux64.zip -d /
RUN rm ifcopenshell-python-38-v0.6.0-b08346c-linux64.zip

ADD main.py /
ADD IFC2BOT /IFC2BOT
CMD ["/bin/bash"]