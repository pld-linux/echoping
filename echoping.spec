Summary:	Non-suid ping
Summary(pl.UTF-8):	ping bez suida
Name:		echoping
Version:	6.0.2
Release:	10
License:	GPL v2
Group:		Networking/Admin
Source0:	http://dl.sourceforge.net/echoping/%{name}-%{version}.tar.gz
# Source0-md5:	991478532b56ab3b6f46ea9fa332626f
Patch0:		echoping-no-versioned-modules.patch
Patch1:		echoping-so.patch
Patch2:		gcc10.patch
URL:		http://echoping.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libidn-devel
BuildRequires:	libtool
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	openssl-devel
BuildRequires:	popt-devel
BuildRequires:	postgresql-devel
Obsoletes:	echoping-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for echoping library.

%description devel -l pl.UTF-8
Pliki nagłówkowe echoping library.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cd plugins
%{__libtoolize}
%{__aclocal} -I .
%{__autoconf}
%{__automake}
cd -
for d in dns ldap postgresql random whois ; do
	cd plugins/$d
	%{__libtoolize}
	%{__aclocal}
	%{__autoconf}
	%{__autoheader}
	%{__automake}
	cd -
done
%configure \
	--with-ssl \
	--without-gnutls \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/echoping/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DETAILS PLUGINS README TODO
%attr(755,root,root) %{_bindir}/echoping
%dir %{_libdir}/echoping
%attr(755,root,root) %{_libdir}/echoping/dns.so
%attr(755,root,root) %{_libdir}/echoping/ldap.so
%attr(755,root,root) %{_libdir}/echoping/postgresql.so
%attr(755,root,root) %{_libdir}/echoping/random.so
%attr(755,root,root) %{_libdir}/echoping/whois.so
%{_mandir}/man1/echoping*

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/echoping
%{_includedir}/echoping/*.h
