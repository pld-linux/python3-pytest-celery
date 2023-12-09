#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Shim pytest plugin to enable celery.contrib.pytest
Summary(pl.UTF-8):	Minimalna wtyczka pytesta włączająca celery.contrib.pytest
Name:		python-pytest-celery
Version:	0.0.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-celery/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-celery/pytest-celery-%{version}.tar.gz
# Source0-md5:	8ef15c46fe2da8ba836cde3ada776a7a
URL:		https://pypi.org/project/pytest-celery/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shim pytest plugin to enable celery.contrib.pytest.

%description -l pl.UTF-8
Minimalna wtyczka pytesta włączająca celery.contrib.pytest.

%package -n python3-pytest-celery
Summary:	Shim pytest plugin to enable celery.contrib.pytest
Summary(pl.UTF-8):	Minimalna wtyczka pytesta włączająca celery.contrib.pytest
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-pytest-celery
Shim pytest plugin to enable celery.contrib.pytest.

%description -n python3-pytest-celery -l pl.UTF-8
Minimalna wtyczka pytesta włączająca celery.contrib.pytest.

%prep
%setup -q -n pytest-celery-%{version}

# change to setuptools to generate egg dependencies
%{__sed} -i -e 's,from distutils\.core,from setuptools,' setup.py

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE
%{py_sitescriptdir}/pytest_celery.py[co]
%{py_sitescriptdir}/pytest_celery-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-celery
%defattr(644,root,root,755)
%doc LICENSE
%{py3_sitescriptdir}/pytest_celery.py
%{py3_sitescriptdir}/__pycache__/pytest_celery.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_celery-%{version}-py*.egg-info
%endif
