#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bbmle
Version  : 1.0.20
Release  : 7
URL      : https://cran.r-project.org/src/contrib/bbmle_1.0.20.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bbmle_1.0.20.tar.gz
Summary  : Tools for General Maximum Likelihood Estimation
Group    : Development/Tools
License  : GPL-2.0
Requires: R-numDeriv
Requires: R-optimx
Requires: R-stringi
BuildRequires : R-numDeriv
BuildRequires : R-optimx
BuildRequires : R-stringi
BuildRequires : clr-R-helpers
BuildRequires : texlive

%description
This package modifies and extends the 'mle' classes in the 'stats4' package.

%prep
%setup -q -c -n bbmle

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530503284

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530503284
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bbmle
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bbmle
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bbmle
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library bbmle|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bbmle/DESCRIPTION
/usr/lib64/R/library/bbmle/INDEX
/usr/lib64/R/library/bbmle/Meta/Rd.rds
/usr/lib64/R/library/bbmle/Meta/features.rds
/usr/lib64/R/library/bbmle/Meta/hsearch.rds
/usr/lib64/R/library/bbmle/Meta/links.rds
/usr/lib64/R/library/bbmle/Meta/nsInfo.rds
/usr/lib64/R/library/bbmle/Meta/package.rds
/usr/lib64/R/library/bbmle/Meta/vignette.rds
/usr/lib64/R/library/bbmle/NAMESPACE
/usr/lib64/R/library/bbmle/NEWS.Rd
/usr/lib64/R/library/bbmle/R/bbmle
/usr/lib64/R/library/bbmle/R/bbmle.rdb
/usr/lib64/R/library/bbmle/R/bbmle.rdx
/usr/lib64/R/library/bbmle/doc/index.html
/usr/lib64/R/library/bbmle/doc/mle2.R
/usr/lib64/R/library/bbmle/doc/mle2.Rnw
/usr/lib64/R/library/bbmle/doc/mle2.pdf
/usr/lib64/R/library/bbmle/doc/quasi.R
/usr/lib64/R/library/bbmle/doc/quasi.Rnw
/usr/lib64/R/library/bbmle/doc/quasi.pdf
/usr/lib64/R/library/bbmle/help/AnIndex
/usr/lib64/R/library/bbmle/help/aliases.rds
/usr/lib64/R/library/bbmle/help/bbmle.rdb
/usr/lib64/R/library/bbmle/help/bbmle.rdx
/usr/lib64/R/library/bbmle/help/paths.rds
/usr/lib64/R/library/bbmle/html/00Index.html
/usr/lib64/R/library/bbmle/html/R.css
/usr/lib64/R/library/bbmle/vignetteData/orob1.rda
