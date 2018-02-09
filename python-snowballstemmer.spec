# disable these for bootstrapping nose and sphinx
%bcond_with tests
%bcond_without python2

Summary:	This package provides 16 stemmer algorithms

Name:		python-snowballstemmer
Version:	1.2.1
Release:	4
Source0:	https://pypi.python.org/packages/20/6b/d2a7cb176d4d664d94a6debf52cd8dbae1f7203c8e42426daa077051d59c/snowballstemmer-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://pypi.python.org/pypi/snowballstemmer
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3-distribute

%description
This package provides 16 stemmer algorithms (15 + Poerter English stemmer)
generated from Snowball algorithms.

%if %{with python2}
%package -n python2-snowballstemmer
Summary:	This package provides 16 stemmer algorithms
Group:		Development/Python
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools

%description -n python2-snowballstemmer
This package provides 16 stemmer algorithms (15 + Poerter English stemmer)
generated from Snowball algorithms.
%endif

%prep
%setup -qc -b 0
mv snowballstemmer-%{version} python3

%if %{with python2}
cp -r python3 python2
%endif

%build
%if %{with python2}
cd python2
python2 setup.py build
cd ..
%endif

cd python3
python setup.py build
cd ..

%install
%if %{with python2}
cd python2
python2 setup.py install --skip-build --root %{buildroot}
cd ..
%endif

cd python3
python setup.py install --skip-build --root=%{buildroot} 
cd ..

%check
%if %{with tests}
%if %{with python2}
cd python2/tests
python2 run.py
cd ../..
%endif
cd python3
make test
cd ..
%endif

%files
%{py_puresitedir}/*

%if %{with python2}
%files -n python2-snowballstemmer
%{py2_puresitedir}/*
%endif
