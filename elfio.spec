%define oname ELFIO
%define sdevname %mklibname %{name} -d -s

Summary:	ELF (Executable and Linkable Format) reader and producer
Name:		elfio
Version:	3.11
Release:	1
License:	LGPLv2.1+
Group:		System/Libraries
Url:		https://elfio.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{oname}-sources/%{oname}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake ninja

%description
ELFIO is a C++ library for reading and generating files in the ELF
binary format. This library is unique and not based on any other
product. It is also platform independent. The library uses standard
ANSI C++ constructions and runs on a wide variety of architectures.

%files
%doc doc/%{name}.pdf
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
%{_includedir}/%{name}
%{_datadir}/cmake/elfio
%doc %{_docdir}/elfio

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
# Install examples
mkdir -p %{buildroot}%{_bindir}
for i in add_section anonymizer elfdump proc_mem write_obj; do
	install -m 755 build/examples/$i/$i %{buildroot}%{_bindir}/
done
# Move cmake files where cmake can find then
mkdir -p %{buildroot}%{_datadir}/cmake
mv %{buildroot}%{_datadir}/elfio/cmake %{buildroot}%{_datadir}/cmake/elfio
rmdir %{buildroot}%{_datadir}/elfio
# FHSify
mv %{buildroot}%{_datadir}/docs %{buildroot}%{_docdir}
