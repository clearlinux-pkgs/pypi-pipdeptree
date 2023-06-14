#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-pipdeptree
Version  : 2.9.1
Release  : 8
URL      : https://files.pythonhosted.org/packages/2b/e9/b36dc85d572a1e732f2e4505afe5ec49a1b1385ba4ebca9eddc625fc8424/pipdeptree-2.9.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/2b/e9/b36dc85d572a1e732f2e4505afe5ec49a1b1385ba4ebca9eddc625fc8424/pipdeptree-2.9.1.tar.gz
Summary  : Command line utility to show dependency tree of packages.
Group    : Development/Tools
License  : MIT
Requires: pypi-pipdeptree-bin = %{version}-%{release}
Requires: pypi-pipdeptree-license = %{version}-%{release}
Requires: pypi-pipdeptree-python = %{version}-%{release}
Requires: pypi-pipdeptree-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatch_vcs)
BuildRequires : pypi(hatchling)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# pipdeptree
[![check](https://github.com/tox-dev/pipdeptree/actions/workflows/check.yml/badge.svg)](https://github.com/tox-dev/pipdeptree/actions/workflows/check.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/tox-dev/pipdeptree/main.svg)](https://results.pre-commit.ci/latest/github/tox-dev/pipdeptree/main)

%package bin
Summary: bin components for the pypi-pipdeptree package.
Group: Binaries
Requires: pypi-pipdeptree-license = %{version}-%{release}

%description bin
bin components for the pypi-pipdeptree package.


%package license
Summary: license components for the pypi-pipdeptree package.
Group: Default

%description license
license components for the pypi-pipdeptree package.


%package python
Summary: python components for the pypi-pipdeptree package.
Group: Default
Requires: pypi-pipdeptree-python3 = %{version}-%{release}

%description python
python components for the pypi-pipdeptree package.


%package python3
Summary: python3 components for the pypi-pipdeptree package.
Group: Default
Requires: python3-core
Provides: pypi(pipdeptree)

%description python3
python3 components for the pypi-pipdeptree package.


%prep
%setup -q -n pipdeptree-2.9.1
cd %{_builddir}/pipdeptree-2.9.1
pushd ..
cp -a pipdeptree-2.9.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686786394
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pipdeptree
cp %{_builddir}/pipdeptree-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pipdeptree/8b057ea7643ea9c2e7936855e2ad67916f884e31 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pipdeptree

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pipdeptree/8b057ea7643ea9c2e7936855e2ad67916f884e31

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
