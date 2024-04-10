# Download the latest release of SQLite source code and build the source
# amalgamation files (sqlite3.c and sqlite3.h).
$ wget https://www.sqlite.org/src/tarball/sqlite.tar.gz?r=release \
    -O sqlite.tar.gz
$ tar xzf sqlite.tar.gz
$ cd sqlite/
$ ./configure
$ make sqlite3.c

# Copy the sqlite3 amalgamation files into the root of the pysqlite3 checkout
# and run build_static + build:
$ cp sqlite/sqlite3.[ch] pysqlite3/
$ cd pysqlite3
$ python setup.py build_static build