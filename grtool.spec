Summary:	Utility for grsecurity RBAC policy files
Summary(pl):	Narzêdzie do plików polityki dla grsecurity RBAC
Name:		grtool
Version:	0.2
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://linuxcc.de/grtool/%{name}-%{version}.tar.gz
# Source0-md5:	13da38240eeec84e99269bc2a71862d5
URL:		http://linuxcc.de/grtool/
Requires:	bash
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
grtool is a small utility useful for people who are dealing with
learning logs and policy files created by and maintained for the
grsecurity RBAC system.

%description -l pl
grtool jest ma³ym narzêdziem u¿ytecznym dla ludzi zajmuj±cych siê
logami z uczenia siê oraz plikami polityki stworzonymi i utrzymywanymi
dla systemu grsecurity RBAC.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}
install grtool $RPM_BUILD_ROOT%{_sbindir}
install grtool.8* $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
