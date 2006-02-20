%include	/usr/lib/rpm/macros.php
%define		_class		Benchmark
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - benchmark PHP scripts or function calls
Summary(pl):	%{_pearname} - testowanie szybko¶ci skryptów i funkcji PHP
Name:		php-pear-%{_pearname}
Version:	1.2.5
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	94e6226ac48796d09c5b74b144037a21
URL:		http://pear.php.net/package/Benchmark/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Framework to benchmark PHP scripts or function calls.

In PEAR status of this package is: %{_status}.

%description -l pl
¦rodowisko do testowania szybko¶ci skryptów PHP i wywo³añ funkcji.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/doc/*
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
