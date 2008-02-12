%define name elfio
%define oname ELFIO
%define version 1.0.3
%define release %mkrel 1

%define lib_major 1
%define lib_name %mklibname %{name} %{lib_major}

%define common_description ELFIO is a C++ library for reading and generating files in the ELF\
binary format. This library is unique and not based on any other\
product. It is also platform independent. The library uses standard\
ANSI C++ constructions and runs on a wide variety of architectures.

Summary: ELF (Executable and Linkable Format) reader and producer implemented as a C++ library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://downloads.sourceforge.net/%{name}/%{oname}-%{version}.tar.bz2
License: LGPL
Group: System/Libraries
Url: http://elfio.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
%description
%{common_description}

%package -n %{lib_name}-devel
Summary: Development tools for programs using the %{oname} library
Group: Development/C
Provides: %{name}-devel = %{version}-%{release}

%description -n	%{lib_name}-devel
This package contains the header files and libraries needed for
developing programs using the %{oname} library.

%{common_description}

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS doc/tutorial.pdf
%{_bindir}/ELFDump

%files -n %{lib_name}-devel
%defattr(-,root,root)
%{_includedir}/ELF*.h
%{_libdir}/lib%{oname}.a


