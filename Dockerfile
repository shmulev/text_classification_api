# Use an official Python runtime as a parent image
FROM python:3.6

# Create working directory
RUN mkdir -p /opt/mlnlmk
WORKDIR /opt/mlnlmk

# RUN \
#  apt-get update && \
#  apt-get install -y build-essential \
#  python-dev python-setuptools \
#  python-numpy python-scipy \
#  libatlas-dev libatlas3gf-base \
#  libopenblas-dev gfortran

# RUN update-alternatives --set libblas.so.3 \
#  /usr/lib/atlas-base/atlas/libblas.so.3
# RUN update-alternatives --set liblapack.so.3 \
#  /usr/lib/atlas-base/atlas/liblapack.so.3


# Copy required files
COPY . /opt/mlnlmk

# Install dependencies specified in requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Open port
EXPOSE 5000

# Run command
CMD ["python", "app.py"]