#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : toml
Version  : 0.10.0
Release  : 6
URL      : https://files.pythonhosted.org/packages/b9/19/5cbd78eac8b1783671c40e34bb0fa83133a06d340a38b55c645076d40094/toml-0.10.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b9/19/5cbd78eac8b1783671c40e34bb0fa83133a06d340a38b55c645076d40094/toml-0.10.0.tar.gz
Summary  : Python Library for Tom's Obvious, Minimal Language
Group    : Development/Tools
License  : MIT
Requires: toml-license = %{version}-%{release}
Requires: toml-python = %{version}-%{release}
Requires: toml-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv
Provides: python-toml
%description
****
TOML
****
.. image:: https://badge.fury.io/py/toml.svg
:target: https://badge.fury.io/py/toml

%package license
Summary: license components for the toml package.
Group: Default

%description license
license components for the toml package.


%package python
Summary: python components for the toml package.
Group: Default
Requires: toml-python3 = %{version}-%{release}

%description python
python components for the toml package.


%package python3
Summary: python3 components for the toml package.
Group: Default
Requires: python3-core

%description python3
python3 components for the toml package.


%prep
%setup -q -n toml-0.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556981803
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/toml
cp LICENSE %{buildroot}/usr/share/package-licenses/toml/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/toml/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
