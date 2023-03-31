# disable these for bootstrapping nose and sphinx
%bcond_with tests

Summary:	This package provides 16 stemmer algorithms

Name:		python-snowballstemmer
Version:	2.2.0
Release:	3
Source0:	https://files.pythonhosted.org/packages/44/7b/af302bebf22c749c56c9c3e8ae13190b5b5db37a33d9068652e8f73b7089/snowballstemmer-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://pypi.python.org/pypi/snowballstemmer
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
BuildRequires:	python3-distribute

%description
This package provides 16 stemmer algorithms (15 + Poerter English stemmer)
generated from Snowball algorithms.

%prep
%autosetup -n snowballstemmer-%{version}

%build
%py_build

%install
%py_install

%check
%if %{with tests}
make test
%endif

%files
%{py_puresitedir}/*
