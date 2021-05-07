#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : toml
Version  : 0.10.2
Release  : 19
URL      : https://files.pythonhosted.org/packages/be/ba/1f744cdc819428fc6b5084ec34d9b30660f6f9daaf70eead706e3203ec3c/toml-0.10.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/be/ba/1f744cdc819428fc6b5084ec34d9b30660f6f9daaf70eead706e3203ec3c/toml-0.10.2.tar.gz
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

%description
TOML
        ****

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
Provides: pypi(toml)

%description python3
python3 components for the toml package.


%prep
%setup -q -n toml-0.10.2
cd %{_builddir}/toml-0.10.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604343631
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/toml
cp %{_builddir}/toml-0.10.2/LICENSE %{buildroot}/usr/share/package-licenses/toml/5e02fc6e946419e35c2f97512cee7fd1a2fe1952
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/toml/5e02fc6e946419e35c2f97512cee7fd1a2fe1952

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
