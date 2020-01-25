%define		status		stable
%define		pearname	Benchmark
Summary:	%{pearname} - benchmark PHP scripts or function calls
Summary(pl.UTF-8):	%{pearname} - testowanie szybkości skryptów i funkcji PHP
Name:		php-pear-%{pearname}
Version:	1.2.9
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	ba08061a854b1c7cd7a18d0928c44b8b
URL:		http://pear.php.net/package/Benchmark/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Suggests:	php-bcmath
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Framework to benchmark PHP scripts or function calls.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Środowisko do testowania szybkości skryptów PHP i wywołań funkcji.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/Benchmark/README .
install -d examples
mv docs/%{pearname}/doc/*.php examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc install.log
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/Benchmark
%{php_pear_dir}/Benchmark/*.php
%{_examplesdir}/%{name}-%{version}
