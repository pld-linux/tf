Summary:	tf - TinyFugue - text-mode MUD client
Summary(pl):	tf - TinyFugue - tekstowy klient do MUD-ów
Name:		tf
Version:	50b3
Release:	0.1
License:	GPL
Group:		Applications/Games
Vendor:		Ken Keys (Hawkeye) <hawkeye@tf.tcp.com>
Source0:	ftp://ftp.tcp.com/pub/mud/Clients/tinyfugue/%{name}-%{version}.tar.gz
# Source0-md5:	dd33896dcb5d841f6b5f4e07fa517af1
Source1:	ftp://ftp.tcp.com/pub/mud/Clients/tinyfugue/%{name}-%{version}-help.tar.gz
# Source1-md5:	79faceed502b867f1bf1263efd5e41a8
Source2:	stest.tf
Patch0:		status_height.patch
URL:		http://tf.tcp.com/~hawkeye/tf/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TinyFugue is a MUD-Client (Multi User Dungeons) that allows the user
to dive into one the most fascinating
Multi-User-Non-Graphic-Fantasy-Role-Playing-Games. Just Enter "tf" and
enjoy your game. This client works in text mode, supports MCCP
compression and multiline statusbar.

%description -l pl
TinyFugue jest klientem MUD (Multi User Dungeons), który pozwala
u¿ytkownikowi zag³êbiæ siê w najbardziej fascynuj±cy ¶wiat
Multi-User-Non-Graphic-Fantasy-Role-Playing-Games. Jest to po prostu
jeden z najlepszych, je¶li nie najlepszy klient do gry w MUD-y. Dzia³a 
w trybie tekstowym, obs³uguje protokó³ kompresji MCCP oraz posiada 
obs³ugê wieloliniowego statusu.

%package doc
Summary:        tf - TinyFugue - text-mode MUD client - HTML help files
Summary(pl):    tf - TinyFugue - tekstowy klient do MUD-ów - pliki pomocy w HTML
Group:          Applications/Games

%description doc
HTML help files.

%description doc -l pl
Pliki pomocy w HTML.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
tar xfz %{SOURCE1}
cp %{SOURCE2} .
%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}/tf-lib
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/topics
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/commands


install tf-lib/* $RPM_BUILD_ROOT%{_libdir}/tf-lib
install src/tf $RPM_BUILD_ROOT%{_bindir}

install %{name}-%{version}-help/tf-help $RPM_BUILD_ROOT%{_libdir}/tf-lib
install %{name}-%{version}-help/topics/* $RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/topics
install %{name}-%{version}-help/commands/* $RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/commands
install %{name}-%{version}-help/index.html $RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/index.html

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "%{name}-%{version} is _beta_ release!"
echo "Some of your scripts may not work or work not properly."
echo "You have been warned."

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS README stest.tf
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}-lib

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-doc-%{version}
