Summary: High performance source code search tool
Name: highway
Version: 1.1.0
Release: 1%{?dist}
Source: https://github.com/tkengo/%{name}/archive/v%{version}.tar.gz
License: MIT License
Vendor: Kengo Tateishi https://github.com/tkengo
Packager: Hiroaki Nakamura https://github.com/hnakamur
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: autoconf, automake, gperftools-devel
Requires: gperftools-libs

%description
High performance source code search tool.

%prep
%setup -q -n highway-%{version}

%build
mkdir -p config
aclocal
autoconf
autoheader
automake --add-missing
./configure --prefix %{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_prefix}/bin/hw

%changelog
