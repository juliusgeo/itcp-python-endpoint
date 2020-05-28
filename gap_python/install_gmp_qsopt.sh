CATPIT_DIR=/catpit
cd $CATPIT_DIR
rm -r gmp_install
rm -r qsopt_install/
rm -r bzip2_install/
rm -r zlib_install/
mkdir lib include
mkdir gmp_install
mkdir qsopt_install bzip2_install zlib_install
mkdir bzip2_install/lib
mkdir bzip2_install/include

cd gmp-6.1.0
./configure --prefix=$CATPIT_DIR/gmp_install --disable-assembly
make
make install
make check
cd $CATPIT_DIR
cp gmp_install/lib/* lib/
cp gmp_install/include/* include/
cd gap-valgrind
./configure  --with-gmp=$CATPIT_DIR/gmp_install
make
cd ../
export C_INCLUDE_PATH=$CATPIT_DIR/include
cd bzip2-1.0.6
make clean
make -f Makefile-libbz2_so
make
make install
if ( test ! -d $CATPIT_DIR/bzip2_install/lib ) ; then mkdir -p  $CATPIT_DIR/bzip2_install/lib ; fi
if ( test ! -d $CATPIT_DIR/bzip2_install/include ) ; then mkdir -p  $CATPIT_DIR/bzip2_install/include ; fi
cp libbz2.so.1.0.6 $CATPIT_DIR/bzip2_install/lib/
cp *.h $CATPIT_DIR/bzip2_install/include/
cd $CATPIT_DIR
cd zlib-1.2.8
./configure --prefix=$CATPIT_DIR/zlib_install
make
make install
cd $CATPIT_DIR
cp gmp_install/include/* include/
cp zlib_install/include/* include/
cp bzip2_install/include/* include/

cd qsopt-ex-2.5.10.3
rm -r build
mkdir build
cd build
../configure --enable-shared --prefix=$CATPIT_DIR/qsopt_install LDFLAGS="-L$CATPIT_DIR/gmp_install/lib -L$CATPIT_DIR/zlib_install/lib -L$CATPIT_DIR/bzip2_install/lib" CFLAGS="-g -fPIC"
make
make install
cd $CATPIT_DIR
cp qsopt_install/include/qsopt_ex/* include/
cp qsopt_install/lib/* lib/
