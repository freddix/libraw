Summary:	Librarized dcraw
Name:		libraw
Version:	0.16.0
Release:	1
License:	GPL v3
Group:		Libraries
Source0:	http://www.libraw.org/data/LibRaw-%{version}.tar.gz
# Source0-md5:	21f569be043057b754d87e3062e2345a
Source1:	http://www.libraw.org/data/LibRaw-demosaic-pack-GPL3-%{version}.tar.gz
# Source1-md5:	b30018c313e10c96521378efc8d492ff
URL:		http://www.libraw.org
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lcms2-devel
BuildRequires:	libgomp-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Librarized dcraw.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for %{name}

%prep
%setup -qn LibRaw-%{version} -a1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-static		\
	--enable-demosaic-pack-gpl3	\
	--enable-examples=no		\
	--enable-lcms			\
	--enable-openmp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changelog.txt
%attr(755,root,root) %ghost %{_libdir}/libraw*.so.10
%attr(755,root,root) %{_libdir}/libraw*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libraw*.so
%{_libdir}/libraw*.la
%{_includedir}/libraw
%{_pkgconfigdir}/*.pc

