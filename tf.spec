Summary:	tf - TinyFugue - MUD client
Summary(pl):	tf - TinyFugue - tekstowy klient do MUD-ów
Name:		tf
Version:	40s1
Release:	1
License:	GPL
Group:		Applications/Games
Vendor:		Ken Keys (Hawkeye) <hawkeye@tf.tcp.com>
Source0:	ftp://tf.tcp.com/pub/tinyfugue/%{name}-%{version}.tar.gz
Patch0:		%{name}-filenames.patch
URL:		http://tf.tcp.com/~hawkeye/tf/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TinyFugue is a MUD-Client (Multi User Dungeons) that allows the user
to dive into one the most fascinating
Multi-User-Non-Graphic-Fantasy-Role-Playing-Games. Just Enter "tf" and
enjoy your game.

%description -l pl
Po prostu jeden z najlepszych, je¶li nie najlepszy klient do gry w
MUD-y. Oczywi¶cie dla trybu tekstowego :).

%prep
%setup -q
%patch0 -p1
mv -f unix/Config unix/Config.orig
cat << EOF >> unix/Config
TF="\${T_BIN}/tf-\${TFVER}"
LIBDIR="\${T_SHARE}/tf"
SYMLINK="$RPM_BUILD_ROOT%{_bindir}/tf"
MAILDIR="/var/mail"
MANPAGE="%{_mandir}/man1/tf.1"
MANTYPE="nroff"
CCFLAGS="$RPM_OPT_FLAGS"
EOF
cat unix/Config.orig >> unix/Config

%build
T_BIN="%{_bindir}"
T_SHARE="%{_datadir}"
export T_BIN T_SHARE
ans=y sh unixmake files

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/%{name}}
install src/tf  $RPM_BUILD_ROOT%{_bindir}/%{name}
install tf-lib/*  $RPM_BUILD_ROOT%{_datadir}/%{name}
install src/tf.1.nroffman $RPM_BUILD_ROOT%{_mandir}/man1/tf.1

cd $RPM_BUILD_ROOT%{_datadir}/%{name}
mv kb-bash.tf bind-bash.tf
mv kb-emacs.tf bind-emacs.tf
mv complete.tf completion.tf
mv factoral.tf factorial.tf
mv filexfer.tf file-xfer.tf
mv local-eg.tf local.tf.sample
mv psh.tf pref-shell.tf
mv spc-page.tf space_page.tf
mv spedwalk.tf speedwalk.tf
mv stack-q.tf stack-queue.tf
mv world-q.tf worldqueue.tf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS README
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*tf
%{_mandir}/man1/tf.1*
