Summary: A collection of small tools based on Qt development
Name: jqtools
Version: 20.6.9
Release: 1%{?dist}
License: MIT
URL: https://github.com/188080501/JQTools
Source0: https://github.com/188080501/JQTools/archive/%{version}.tar.gz

# Add build dependencies
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtquickcontrols2-devel
BuildRequires: qt5-qtquickcontrols-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-qtgraphicaleffects-devel

%description
This package provides a collection of small tools based on Qt development.

%prep
%autosetup -p1

%build
qmake-qt5
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/JQTools

%changelog
Sat Jun 9 2020 shijie.chen xingwozhonghua@126.com - 20.6.9-1
Initial package for jqtools.
