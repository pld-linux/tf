# Often html doc files aren't sync with tf releases.
# New tf releases contains mostly bug fixes, so
# older docs should be ok.
%define		doc_ver 	50b8
Summary:	tf - TinyFugue - text-mode MUD client
Summary(pl.UTF-8):	tf - TinyFugue - tekstowy klient do MUD-ów
Name:		tf
Version:	50b8
Release:	7
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/tinyfugue/%{name}-%{version}.tar.gz
# Source0-md5:	3e994e791966d274f63b0e61abf2ef59
Source1:	http://dl.sourceforge.net/tinyfugue/%{name}-%{doc_ver}-help.tar.gz
# Source1-md5:	26eb64b2f811c8143e9c08654d26d138
Source2:	http://www.ingwar.eu.org/downloads/%{name}.syntax.gz
# Source2-md5:	398aa4c28e83fb2ce688eade24c5fc88
Patch0:		pcre.patch
Patch1:		typedef-not-var.patch
URL:		http://sourceforge.net/projects/tinyfugue/
BuildRequires:	autoconf
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TinyFugue is a MUD-Client (Multi User Dungeons) that allows the user
to dive into one the most fascinating
Multi-User-Non-Graphic-Fantasy-Role-Playing-Games. Just Enter "tf" and
enjoy your game. This client works in text mode, supports MCCP
compression and multiline statusbar.

%description -l pl.UTF-8
TinyFugue jest klientem MUD (Multi User Dungeons), który pozwala
użytkownikowi zagłębić się w najbardziej fascynujący świat
Multi-User-Non-Graphic-Fantasy-Role-Playing-Games. Jest to po prostu
jeden z najlepszych, jeśli nie najlepszy klient do gry w MUD-y. Działa
w trybie tekstowym, obsługuje protokół kompresji MCCP oraz posiada
obsługę wieloliniowego statusu.

%package doc
Summary:	tf - TinyFugue - text-mode MUD client - HTML help files
Summary(pl.UTF-8):	tf - TinyFugue - tekstowy klient do MUD-ów - pliki pomocy w HTML
Group:		Applications/Games

%description doc
HTML help files.

%description doc -l pl.UTF-8
Pliki pomocy w HTML.

%prep
%setup -q
tar xzPf %{SOURCE1}
cp %{SOURCE2} .
%patch -P0 -p1
%patch -P1 -p1

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
%doc CHANGES CREDITS README tf.syntax.gz
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}-lib

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-doc-%{version}
