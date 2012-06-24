%include	/usr/lib/rpm/macros.php
%define		_class		Benchmark
%define		_pearname	%{_class}
Summary:	%{_pearname} - benchmark PHP scripts or function calls
Summary(pl):	%{_pearname} - testowanie szybko�ci skrypt�w i funkcji PHP
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	47114bf9e7ff959d8806a70de9ef36b7
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Benchmark/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Framework to benchmark PHP scripts or function calls.

%description -l pl
�rodowisko do testowania szybko�ci skrypt�w PHP i wywo�a� funkcji.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/doc/*.php
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
