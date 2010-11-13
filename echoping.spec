Summary:	Non-suid ping
Summary(pl.UTF-8):	ping bez suida
Name:		echoping
Version:	6.0.2
Release:	5
License:	GPL v2
Group:		Networking/Admin
Source0:	http://dl.sourceforge.net/echoping/%{name}-%{version}.tar.gz
# Source0-md5:	991478532b56ab3b6f46ea9fa332626f
URL:		http://echoping.sourceforge.net/
BuildRequires:	libidn-devel
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	openssl-devel
BuildRequires:	popt-devel
BuildRequires:	postgresql-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
"echoping" is a small program to test (approximatively) performances
of a remote host by sending it TCP "echo" (or other protocol, such as
HTTP) packets.

%description -l pl.UTF-8
echoping to mały program do sprawdzania (przybliżonej) wydajności
zdalnego hosta poprzez wysyłanie pakietów TCP "echo" (lub innego
protokołu, jak np. HTTP).

%package devel
Summary:	Header files for echoping library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki echoping
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for echoping library.

%description devel -l pl.UTF-8
Pliki nagłówkowe echoping library.

%package libs
Summary:	echoping libraries
Summary(pl.UTF-8):	Biblioteki echoping
Group:		Libraries

%description libs
echoping libraries.

%description libs -l pl.UTF-8
Biblioteki echoping.

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
%attr(755,root,root) %{_bindir}/echoping
%{_mandir}/man1/echoping*

%files devel
%defattr(644,root,root,755)
%{_libdir}/echoping/dns.so
%{_libdir}/echoping/ldap.so
%{_libdir}/echoping/postgresql.so
%{_libdir}/echoping/random.so
%{_libdir}/echoping/whois.so
%dir %{_includedir}/echoping
%{_includedir}/echoping/*.h

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/echoping
%attr(755,root,root) %{_libdir}/echoping/dns.so.*.*
%attr(755,root,root) %ghost %{_libdir}/echoping/dns.so.0
%attr(755,root,root) %{_libdir}/echoping/ldap.so.*.*
%attr(755,root,root) %ghost %{_libdir}/echoping/ldap.so.0
%attr(755,root,root) %{_libdir}/echoping/postgresql.so.*.*
%attr(755,root,root) %ghost %{_libdir}/echoping/postgresql.so.0
%attr(755,root,root) %{_libdir}/echoping/random.so.*.*
%attr(755,root,root) %ghost %{_libdir}/echoping/random.so.0
%attr(755,root,root) %{_libdir}/echoping/whois.so.*.*
%attr(755,root,root) %ghost %{_libdir}/echoping/whois.so.0
