Summary:	Non-suid ping
Summary(pl.UTF-8):	ping bez suida
Name:		echoping
Version:	6.0.2
Release:	1
License:	GPL v2
Group:		Networking/Admin
Source0:	http://dl.sourceforge.net/echoping/%{name}-%{version}.tar.gz
# Source0-md5:	991478532b56ab3b6f46ea9fa332626f
URL:		http://echoping.sourceforge.net/
BuildRequires:	libidn-devel
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	openssl-devel
BuildRequires:	postgresql-devel
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"echoping" is a small program to test (approximatively) performances
of a remote host by sending it TCP "echo" (or other protocol, such as
HTTP) packets.

%description -l pl.UTF-8
echoping to mały program do sprawdzania (przybliżonej) wydajności
zdalnego hosta poprzez wysyłanie pakietów TCP "echo" (lub innego
protokołu, jak np. HTTP).

%prep
%setup -q

%build
%configure \
	--with-ssl \
	--without-gnutls \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/echoping/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DETAILS PLUGINS README TODO
%attr(755,root,root) %{_bindir}/echoping*
%dir %{_libdir}/echoping
%attr(755,root,root) %{_libdir}/echoping/*.so*
%{_mandir}/man1/echoping*
