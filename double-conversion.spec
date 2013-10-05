#
# TODO
# - versioning in shared lib

# Conditional build:
%bcond_without	static_libs	# don't build static libraries

Summary:	Library providing binary-decimal and decimal-binary routines for IEEE doubles
Name:		double-conversion
Version:	1.1.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://double-conversion.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	29b533ed4311161267bff1a9a97e2953
URL:		http://code.google.com/p/double-conversion
Source1:	SConstruct
BuildRequires:	libstdc++-devel
BuildRequires:	scons >= 2.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project (double-conversion) provides binary-decimal and
decimal-binary routines for IEEE doubles.

The library consists of efficient conversion routines that have been
extracted from the V8 JavaScript engine. The code has been refactored
and improved so that it can be used more easily in other projects.

%package devel
Summary:	Library providing binary-decimal and decimal-binary routines for IEEE doubles
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Contains header files for developing applications that use the %{name}
library.

There is extensive documentation in src/double-conversion.h. Other
examples can be found in test/cctest/test-conversions.cc.

%package static
Summary:	Static %{name} library
Summary(pl.UTF-8):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%description static -l pl.UTF-8
Statyczna biblioteka %{name}.

%prep
%setup -q -n %{name}
cp -p %{SOURCE1} SConstruct

%build
%scons \
	CXX="%{__cxx}"
	CXXFLAGS="%{__cxx}"

# avoid file exists errors, when entering install
rm -f libdouble_conversion.so libdouble_conversion.so.0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/%{name}}
%scons install \
	DESTDIR=$RPM_BUILD_ROOT \

cp -p src/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README AUTHORS
%attr(755,root,root) %{_libdir}/libdouble_conversion.so.*.*.*
%ghost %{_libdir}/libdouble_conversion.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libdouble_conversion.so
%{_includedir}/%{name}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdouble_conversion.a
%{_libdir}/libdouble_conversion_pic.a
%endif
