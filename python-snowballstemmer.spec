# disable these for bootstrapping nose and sphinx
%bcond_with tests
%bcond_without python2

Summary:	Theme for the Sphinx documentation generator

Name:		python-snowballstemmer
Version:	1.2.1
Release:	1
Source0:	https://pypi.python.org/packages/20/6b/d2a7cb176d4d664d94a6debf52cd8dbae1f7203c8e42426daa077051d59c/snowballstemmer-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://pypi.python.org/pypi/snowballstemmer
BuildArch:	noarch
Requires:	python-pkg-resources
Requires:	python-docutils
Requires:	python-jinja2
Requires:	python-pygments
BuildRequires:	python-setuptools
%if %{with doc}
BuildRequires:	python-docutils >= 0.7
BuildRequires:	python-jinja2 >= 2.3
%endif
%if %{with tests}
BuildRequires:	python-nose
BuildRequires:	python-pygments
BuildRequires:  python-jinja2
%endif
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3-distribute
%rename python3-sphinx

%description
This package provides 16 stemmer algorithms (15 + Poerter English stemmer)
generated from Snowball algorithms.

%if %{with python2}
%package -n python2-snowballstemmer
Summary:	Theme for the Sphinx documentation generator
Group:		Development/Python
Requires:	python2-docutils >= 0.7
Requires:	python2-pygments >= 1.2
Requires:	python2-jinja2 >= 2.3
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-nose
BuildRequires:	python2-pygments
BuildRequires:  python2-jinja2
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
