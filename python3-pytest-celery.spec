Summary:	Shim pytest plugin to enable celery.contrib.pytest
Summary(pl.UTF-8):	Minimalna wtyczka pytesta włączająca celery.contrib.pytest
Name:		python3-pytest-celery
Version:	1.2.0
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-celery/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-celery/pytest_celery-%{version}.tar.gz
# Source0-md5:	d737b3149359b2c7fd516a386389440c
URL:		https://pypi.org/project/pytest-celery/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shim pytest plugin to enable celery.contrib.pytest.

%description -l pl.UTF-8
Minimalna wtyczka pytesta włączająca celery.contrib.pytest.

%prep
%setup -q -n pytest_celery-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{py3_sitescriptdir}/pytest_celery
%{py3_sitescriptdir}/pytest_celery-%{version}.dist-info
