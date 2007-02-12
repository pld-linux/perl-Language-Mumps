%include	/usr/lib/rpm/macros.perl
%define		pdir	Language
%define		pnam	Mumps
Summary:	Language::Mumps perl module
Summary(pl.UTF-8):   Moduł perla Language::Mumps
Name:		perl-Language-Mumps
Version:	1.07
Release:	2
License:	free use, but modifications must be notified to the author
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	22da04777ada302d116214cd4ba32f9f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package implements a MUMPS to Perl compiler. A script for
interpreting and running MUMPS programs is now supplied. The standard
library is based on MumpsVM, another free MUMPS implementation.

%description -l pl.UTF-8
Ten pakiet jest implementacją MUMPS. Dołączony jest także skrypt do
interpretowania i uruchamiania programów w MUMPS. Standardowa
biblioteka jest bazowana na MumpsVM, innej wolnodostępnej
implementacji MUMPS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README examples/*
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Language/Mumps.pm
%{_mandir}/man[13]/*
