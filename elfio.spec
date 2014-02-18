%define oname ELFIO
%define sdevname %mklibname %{name} -d -s

Summary:	ELF (Executable and Linkable Format) reader and producer
Name:		elfio
Version:	1.0.3
Release:	6
License:	LGPLv2.1+
Group:		System/Libraries
Url:		http://elfio.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{oname}-%{version}.tar.bz2

%description
ELFIO is a C++ library for reading and generating files in the ELF
binary format. This library is unique and not based on any other
product. It is also platform independent. The library uses standard
ANSI C++ constructions and runs on a wide variety of architectures.

%files
%doc README AUTHORS doc/tutorial.pdf
%{_bindir}/ELFDump

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
%{_includedir}/ELF*.h
%{_libdir}/lib%{oname}.a

#----------------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

