#
# Conditional build:
%bcond_without	static_libs	# static library
%bcond_without	tests		# build without tests

Summary:	Library providing binary-decimal and decimal-binary routines for IEEE doubles
Summary(pl.UTF-8):	Biblioteka dostarczająca przejścia binarno-dziesiętne i dziesiętno-binarne dla typów double IEEE
Name:		double-conversion
Version:	3.1.6
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/google/double-conversion/releases
Source0:	https://github.com/google/double-conversion/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	432fa87cc342a5c45ed812cdc1f8c209
URL:		https://github.com/google/double-conversion
BuildRequires:	cmake >= 3.0
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project (double-conversion) provides binary-decimal and
decimal-binary routines for IEEE doubles.

The library consists of efficient conversion routines that have been
extracted from the V8 JavaScript engine. The code has been refactored
and improved so that it can be used more easily in other projects.

%description -l pl.UTF-8
Projekt double-conversion dostarcza funkcje przejścia
binarno-dziesiętne i dziesiętno-binarne dla typów double IEEE.

Biblioteka składa się z wydajnych funkcji konwersji, wyciągniętych z
silnika JavaScriptu V8. Kod został zrefaktorowany i ulepszony, dzięki
czemu może być łatwiej używany w innych projektach.

%package devel
Summary:	Header files for double-conversion library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki double-conversion
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Contains header files for developing applications that use the
double-conversion library.

There is extensive documentation in double-conversion.h.

%description devel -l pl.UTF_8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę double-conversion.

W pliku double-conversion.h zawarta jest obszerna dokumentacja.

%package static
Summary:	Static double-conversion library
Summary(pl.UTF-8):	Statyczna biblioteka double-conversion
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static double-conversion library.

%description static -l pl.UTF-8
Statyczna biblioteka double-conversion.

%prep
%setup -q

%build
%if %{with static_libs}
install -d build-static
cd build-static
%cmake .. \
	-DBUILD_SHARED_LIBS=OFF

%{__make}
cd ..
%endif

install -d build
cd build
%cmake .. \
	%{?with_tests:-DBUILD_TESTING=ON}

%{__make}

%{?with_tests:ctest}

%install
rm -rf $RPM_BUILD_ROOT

%if %{with static_libs}
%{__make} -C build-static install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog LICENSE README.md
%attr(755,root,root) %{_libdir}/libdouble-conversion.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdouble-conversion.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdouble-conversion.so
%{_includedir}/double-conversion
%{_libdir}/cmake/double-conversion

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdouble-conversion.a
%endif
