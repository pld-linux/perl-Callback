%include	/usr/lib/rpm/macros.perl
Summary:	Callback perl module
Summary(pl):	Modu³ perla Callback
Name:		perl-Callback
Version:	1.04
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Callback/Callback-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Callback perl module provides a simple interface for function
callbacks.

%description -l pl
Modu³ perla Callback udostêpnia prosty interfejs dla odwo³añ funkcji.

%prep
%setup -q -n Callback-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Callback.pm
%{_mandir}/man3/*
