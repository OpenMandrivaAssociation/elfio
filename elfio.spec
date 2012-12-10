%define name elfio
%define oname ELFIO
%define version 1.0.3
%define release %mkrel 5

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




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-5mdv2011.0
+ Revision: 618034
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.0.3-4mdv2010.0
+ Revision: 428553
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-3mdv2009.0
+ Revision: 244695
- rebuild
- fix spacing at top of description

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1mdv2008.1-current
+ Revision: 136403
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Jan 09 2007 Olivier Blin <oblin@mandriva.com> 1.0.3-1mdv2007.0
+ Revision: 106249
- remove invalid requirement
- initial ELFIO release
- Create elfio

