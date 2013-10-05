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
BuildRequires:	scons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library providing binary-decimal and decimal-binary routines for IEEE
doubles.

%package devel
Summary:	Library providing binary-decimal and decimal-binary routines for IEEE doubles
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Contains header files for developing applications that use the %{name} library.

%prep
%setup -q -n %{name}

%build
%scons -f %{SOURCE1}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/%{name}}

cp -p libdouble_conversion.a libdouble_conversion_pic.a $RPM_BUILD_ROOT%{_libdir}

cp -p src/double-conversion.h $RPM_BUILD_ROOT%{_includedir}/%{name}
cp -p src/bignum.h $RPM_BUILD_ROOT%{_includedir}/%{name}
cp -p src/bignum-dtoa.h $RPM_BUILD_ROOT%{_includedir}/%{name}
cp -p src/cached-powers.h $RPM_BUILD_ROOT%{_includedir}/%{name}
cp -p src/diy-fp.h $RPM_BUILD_ROOT%{_includedir}/%{name}
cp -p src/fast-dtoa.h $RPM_BUILD_ROOT%{_includedir}/%{name}
cp -p src/fixed-dtoa.h $RPM_BUILD_ROOT%{_includedir}/%{name}
cp -p src/ieee.h $RPM_BUILD_ROOT%{_includedir}/%{name}
cp -p src/strtod.h $RPM_BUILD_ROOT%{_includedir}/%{name}
cp -p src/utils.h $RPM_BUILD_ROOT%{_includedir}/%{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README AUTHORS

%files devel
%defattr(644,root,root,755)
%{_libdir}/libdouble_conversion.a
%{_libdir}/libdouble_conversion_pic.a
%{_includedir}/%{name}
