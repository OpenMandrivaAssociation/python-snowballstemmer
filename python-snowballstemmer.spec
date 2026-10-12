# disable these for bootstrapping nose and sphinx
%bcond_with tests

Summary:	36 stemmers for 34 languages, generated from Snowball algorithms

Name:		python-snowballstemmer
Version:	3.1.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/snowballstemmer/snowballstemmer-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://pypi.python.org/pypi/snowballstemmer
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	make
BuildRequires:	python%{pyver}dist(setuptools)

%description
This package provides 36 stemmers for 34 languages, generated from
Snowball algorithms.

%check
%if %{with tests}
make test
%endif

%files
%{py_puresitedir}/*
