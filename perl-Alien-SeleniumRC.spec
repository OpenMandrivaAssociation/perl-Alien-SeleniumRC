%define upstream_name    Alien-SeleniumRC
%define upstream_version 1.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 2.93
Release:	1

Summary:	Packaging up SeleniumRC java server
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Alien/Alien-SeleniumRC-2.93.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
The Selenium RC home page is at the http://openqa.org/selenium-rc manpage

Selenium Remote Control is a test tool that allows you to write automated
web application UI tests in any programming language against any HTTP
website using any mainstream JavaScript-enabled browser.

Selenium Remote Control provides a Selenium Server, which can automatically
start/stop/control any supported browser. It works by using Selenium Core,
a pure-HTML+JS library that performs automated tasks in JavaScript.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/selenium-rc



%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.30.0-2mdv2011.0
+ Revision: 654203
- rebuild for updated spec-helper

* Fri Dec 24 2010 Shlomi Fish <shlomif@mandriva.org> 1.30.0-1mdv2011.0
+ Revision: 624660
- import perl-Alien-SeleniumRC


