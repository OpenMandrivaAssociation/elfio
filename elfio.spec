%define oname ELFIO
%define sdevname %mklibname %{name} -d -s

Summary:	ELF (Executable and Linkable Format) reader and producer
Name:		elfio
Version:	3.8
Release:	1
License:	LGPLv2.1+
Group:		System/Libraries
Url:		http://elfio.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{oname}-sources/%{oname}-%{version}/%{name}-%{version}.tar.gz

%description
ELFIO is a C++ library for reading and generating files in the ELF
binary format. This library is unique and not based on any other
product. It is also platform independent. The library uses standard
ANSI C++ constructions and runs on a wide variety of architectures.

%files
%doc README AUTHORS doc/%{name}.pdf
%{_bindir}/*

#----------------------------------------------------------------------------

%package -n %{sdevname}
Summary:	Development tools for programs using the %{oname} library
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{_lib}elfio1-devel < 1.0.3-6

%description -n %{sdevname}
This package contains the header files and libraries needed for
developing programs using the %{oname} library.

%files -n %{sdevname}
%{_includedir}/%{name}/elf*.hpp

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%make_build

%install
%make_install

