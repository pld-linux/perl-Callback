#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Callback
Summary:	Callback Perl module - object interface for function callbacks
Summary(pl):	Modu³ Perla Callback - interfejs obiektowy odwo³añ do funkcji
Name:		perl-Callback
Version:	1.06
Release:	1
License:	free to use
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Callback/Callback-%{version}.tar.gz
# Source0-md5:	cc2d976980ccd1ac8c75d46aa0ea977f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Callback Perl module provides a standard interface to register
callbacks. Those callbacks can be either purely functional (i.e. a
function call with arguments) or object-oriented (a method call on an
object).

%description -l pl
Modu³ Perla Callback udostêpnia prosty interfejs do rejestrowania
odwo³añ. Odwo³ania te mog± byæ czysto funkcyjne (tzn. funkcja wywo³ana
z argumentami) lub obiektowe (wywo³anie metody na obiekcie).

%prep
%setup -q -n Callback-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Callback.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Callback.pm
%{_mandir}/man3/*
