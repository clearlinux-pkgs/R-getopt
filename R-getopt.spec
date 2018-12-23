#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-getopt
Version  : 1.20.2
Release  : 14
URL      : https://cran.r-project.org/src/contrib/getopt_1.20.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/getopt_1.20.2.tar.gz
Summary  : C-Like 'getopt' Behavior
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
BuildRequires : clr-R-helpers
Provides: /path/to/Rscript

%description
``#!'' shebang scripts that accept short and long flags/options.
    Many users will prefer using instead the packages optparse or argparse
    which add extra features like automatically generated help option and usage,
    support for default values, positional argument support, etc.

%prep
%setup -q -c -n getopt

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521202528

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521202528
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library getopt
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library getopt
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library getopt
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library getopt|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/getopt/DESCRIPTION
/usr/lib64/R/library/getopt/INDEX
/usr/lib64/R/library/getopt/Meta/Rd.rds
/usr/lib64/R/library/getopt/Meta/features.rds
/usr/lib64/R/library/getopt/Meta/hsearch.rds
/usr/lib64/R/library/getopt/Meta/links.rds
/usr/lib64/R/library/getopt/Meta/nsInfo.rds
/usr/lib64/R/library/getopt/Meta/package.rds
/usr/lib64/R/library/getopt/NAMESPACE
/usr/lib64/R/library/getopt/NEWS
/usr/lib64/R/library/getopt/R/getopt
/usr/lib64/R/library/getopt/R/getopt.rdb
/usr/lib64/R/library/getopt/R/getopt.rdx
/usr/lib64/R/library/getopt/exec/example.R
/usr/lib64/R/library/getopt/help/AnIndex
/usr/lib64/R/library/getopt/help/aliases.rds
/usr/lib64/R/library/getopt/help/getopt.rdb
/usr/lib64/R/library/getopt/help/getopt.rdx
/usr/lib64/R/library/getopt/help/paths.rds
/usr/lib64/R/library/getopt/html/00Index.html
/usr/lib64/R/library/getopt/html/R.css
