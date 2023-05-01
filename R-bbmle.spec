#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bbmle
Version  : 1.0.25
Release  : 42
URL      : https://cran.r-project.org/src/contrib/bbmle_1.0.25.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bbmle_1.0.25.tar.gz
Summary  : Tools for General Maximum Likelihood Estimation
Group    : Development/Tools
License  : GPL-3.0
Requires: R-bdsmatrix
Requires: R-mvtnorm
Requires: R-numDeriv
BuildRequires : R-bdsmatrix
BuildRequires : R-mvtnorm
BuildRequires : R-numDeriv
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n bbmle
cd %{_builddir}/bbmle

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1652282198

%install
export SOURCE_DATE_EPOCH=1652282198
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bbmle
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bbmle
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bbmle
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc bbmle || :


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
/usr/lib64/R/library/bbmle/tests/BIC.R
/usr/lib64/R/library/bbmle/tests/BIC.Rout.save
/usr/lib64/R/library/bbmle/tests/ICtab.R
/usr/lib64/R/library/bbmle/tests/ICtab.Rout.save
/usr/lib64/R/library/bbmle/tests/RUnit-tests.R
/usr/lib64/R/library/bbmle/tests/binomtest1.R
/usr/lib64/R/library/bbmle/tests/binomtest1.Rout
/usr/lib64/R/library/bbmle/tests/binomtest1.Rout.save
/usr/lib64/R/library/bbmle/tests/boundstest.R
/usr/lib64/R/library/bbmle/tests/controleval.R
/usr/lib64/R/library/bbmle/tests/controleval.Rout.save
/usr/lib64/R/library/bbmle/tests/eval.R
/usr/lib64/R/library/bbmle/tests/eval.Rout.save
/usr/lib64/R/library/bbmle/tests/formulatest.R
/usr/lib64/R/library/bbmle/tests/formulatest.Rout.save
/usr/lib64/R/library/bbmle/tests/glmcomp.R
/usr/lib64/R/library/bbmle/tests/glmcomp.Rout.save
/usr/lib64/R/library/bbmle/tests/gradient_vecpar_profile.R
/usr/lib64/R/library/bbmle/tests/gradient_vecpar_profile.Rout.save
/usr/lib64/R/library/bbmle/tests/grtest1.R
/usr/lib64/R/library/bbmle/tests/grtest1.Rout.save
/usr/lib64/R/library/bbmle/tests/impsamp.R
/usr/lib64/R/library/bbmle/tests/makesavefiles
/usr/lib64/R/library/bbmle/tests/methods.R
/usr/lib64/R/library/bbmle/tests/methods.Rout.save
/usr/lib64/R/library/bbmle/tests/mkout
/usr/lib64/R/library/bbmle/tests/mortanal.R
/usr/lib64/R/library/bbmle/tests/mortanal.Rout.save
/usr/lib64/R/library/bbmle/tests/optimize.R
/usr/lib64/R/library/bbmle/tests/optimize.Rout.save
/usr/lib64/R/library/bbmle/tests/optimizers.R
/usr/lib64/R/library/bbmle/tests/optimizers.Rout.save
/usr/lib64/R/library/bbmle/tests/optimx.R
/usr/lib64/R/library/bbmle/tests/optimx.Rout.save
/usr/lib64/R/library/bbmle/tests/order.R
/usr/lib64/R/library/bbmle/tests/order.Rout.save
/usr/lib64/R/library/bbmle/tests/parscale.R
/usr/lib64/R/library/bbmle/tests/parscale.Rout.save
/usr/lib64/R/library/bbmle/tests/predict.R
/usr/lib64/R/library/bbmle/tests/predict.Rout.save
/usr/lib64/R/library/bbmle/tests/prof_newmin.R
/usr/lib64/R/library/bbmle/tests/prof_spec.R
/usr/lib64/R/library/bbmle/tests/profbound.R
/usr/lib64/R/library/bbmle/tests/profbound.Rout.save
/usr/lib64/R/library/bbmle/tests/richards.R
/usr/lib64/R/library/bbmle/tests/richards.Rout.save
/usr/lib64/R/library/bbmle/tests/startvals.R
/usr/lib64/R/library/bbmle/tests/startvals.Rout.save
/usr/lib64/R/library/bbmle/tests/startvals2.R
/usr/lib64/R/library/bbmle/tests/startvals2.Rout.save
/usr/lib64/R/library/bbmle/tests/test-relist1.R
/usr/lib64/R/library/bbmle/tests/test-relist1.Rout.save
/usr/lib64/R/library/bbmle/tests/testbounds.R
/usr/lib64/R/library/bbmle/tests/testbounds.Rout
/usr/lib64/R/library/bbmle/tests/testbounds.Rout.save
/usr/lib64/R/library/bbmle/tests/testderiv.R
/usr/lib64/R/library/bbmle/tests/testderiv.Rout.save
/usr/lib64/R/library/bbmle/tests/testenv.R
/usr/lib64/R/library/bbmle/tests/testenv.Rout.save
/usr/lib64/R/library/bbmle/tests/testparpred.R
/usr/lib64/R/library/bbmle/tests/testparpred.Rout.save
/usr/lib64/R/library/bbmle/tests/tmptest.R
/usr/lib64/R/library/bbmle/tests/tmptest.Rout.save
/usr/lib64/R/library/bbmle/tests/update.R
/usr/lib64/R/library/bbmle/tests/update.Rout.save
/usr/lib64/R/library/bbmle/vignetteData/orob1.rda
