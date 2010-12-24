%define upstream_name    Alien-SeleniumRC
%define upstream_version 1.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Packaging up SeleniumRC java server
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Alien/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/selenium-rc

