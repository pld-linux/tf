# Often html doc files aren't sync with tf releases.
# New tf releases contains mostly bug fixes, so
# older docs should be ok.
%define		doc_ver 	50b5
Summary:	tf - TinyFugue - text-mode MUD client
Summary(pl):	tf - TinyFugue - tekstowy klient do MUD-ów
Name:		tf
Version:	50b5
Release:	1
License:	GPL
Group:		Applications/Games
Vendor:		Ken Keys (Hawkeye) <hawkeye@tf.tcp.com>
Source0:	ftp://ftp.mud.de/pub/software/clients/unix/tinyfugue/%{name}-%{version}.tar.gz
# Source0-md5:	6e6602f1618d31e40de24e46640f1ff8
Source1:	ftp://ftp.mud.de/pub/software/clients/unix/tinyfugue/%{name}-%{doc_ver}-help.tar.gz
# Source1-md5:	c2eb4e3fada91ea287f3b765aba3842b
Source2:	stest.tf
Source3:	http://www.ingwar.eu.org/downloads/tf.syntax.gz
# Source3-md5:	398aa4c28e83fb2ce688eade24c5fc88
Patch0:		%{name}-%{version}-multistatus.patch
URL:		http://tf.tcp.com/~hawkeye/tf/
BuildRequires:	autoconf
BuildRequires:	ncurses-devel
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
tar xzPf %{SOURCE1}
cp %{SOURCE2} .
cp %{SOURCE3} .
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

install %{name}-%{doc_ver}-help/topics/* $RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/topics
install %{name}-%{doc_ver}-help/commands/* $RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/commands
install %{name}-%{doc_ver}-help/index.html $RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/index.html

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "%{name}-%{version} is _beta_ release!"
echo "Some of your scripts may not work or work not properly."
echo "You have been warned."

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS README stest.tf tf.syntax.gz
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}-lib

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-doc-%{version}
