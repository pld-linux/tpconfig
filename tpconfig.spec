Name:		tpconfig
Version:	3.1.3
Release:	1
Summary:	Synaptics/ALPS TouchPad configuration tool
Summary(pl):	Narz�dzie do konfiguracji Synaptics/ALPS TouchPad
License:	GPL
Group:		Applications/System
Source0:	http://www.compass.com/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a configuration tool for the Synaptics TouchPad and the ALPS
Glidepad/Stickpointer used on many PC laptops.

%description -l pl
Narz�dzie do konfiguracji TouchPad'�w Synaptics i ALPS
Glidepad/Stickpointer u�ywanych w wielu komputerach przeno�nych.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS COPYING INSTALL NEWS ChangeLog
%attr(755,root,root) %{_bindir}/tpconfig

%clean
rm -rf $RPM_BUILD_ROOT