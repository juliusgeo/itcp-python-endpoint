from ubuntu:bionic
RUN apt-get update
RUN apt-get install -y python3 python3-pip libgmp3-dev singular zlib1g bzip2 wget git
RUN pip3 install pexpect
RUN pip3 install flask
RUN pip3 install flask-cors
RUN mkdir catpit


WORKDIR catpit
RUN wget http://www.gap-system.org/pub/gap/gap48/tar.gz/gap4r8p4_2016_06_04-12_41.tar.gz
RUN ls -al
RUN tar -xf gap*.tar.gz 
WORKDIR gap4r8 
RUN ./configure --with-gmp=system && make

WORKDIR pkg
RUN git clone https://github.com/jayant91089/itap.git
RUN git clone https://github.com/jayant91089/itcp.git
RUN git clone https://github.com/jayant91089/symchm.git
RUN git clone https://github.com/jayant91089/qsopt_ex-interface.git

WORKDIR ../../
RUN wget https://sites.google.com/site/jayantapteshomepage/home/qsopt.tar.gz
RUN tar -xf qsopt.tar.gz
RUN mkdir qsopt_install
WORKDIR qsopt-ex-2.5.10.3
RUN mkdir build
WORKDIR build
RUN ../configure --prefix=$PWD/../../qsopt_install
RUN make
RUN make install
WORKDIR ../../
RUN mkdir include lib
RUN cp qsopt_install/include/qsopt_ex/* include/
RUN cp qsopt_install/lib/* lib/
WORKDIR gap4r8/pkg/qsopt_ex-interface/
RUN make all
RUN ls -al gap
RUN cd gap && echo "qs_exec:=\"/catpit/gap4r8/pkg/qsopt_ex-interface/qsi\";\n$(cat qsinterface.gi)" > qsinterface.gi && cat qsinterface.gi
WORKDIR /catpit/
RUN export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PWD/lib
COPY ./endpoint.py /
COPY ./gap_python.py /

WORKDIR /
RUN git clone https://github.com/juliusgeo/itcp-python-endpoint.git
RUN ls -la /
ENTRYPOINT ["python3", "itcp-python-endpoint/gap_python/endpoint.py"]