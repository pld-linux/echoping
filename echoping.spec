Summary:	Non-suid ping
Name:		echoping
Version:	6.0
Release:	0.BETA.0.1
License:	GPL v2
Group:		Networking/Admin
Source0:	ftp://ftp.internatif.org/pub/unix/echoping/%{name}-%{version}-BETA.tar.gz
# Source0-md5:	a8d10ec94a6dfc42bd978a1e99d00efa
URL:		http://echoping.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bind-devel
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"echoping" is a small program to test (approximatively) performances of a remote host by sending it TCP "echo" (or other protocol, such as HTTP) packets.

%prep
%setup -q -n %{name}-%{version}-BETA

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc ChangeLog README
#%attr(755,root,root) %{_bindir}/*
#%{_mandir}/man*/*
