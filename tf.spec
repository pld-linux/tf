Summary:	tf - TinyFugue - text-mode MUD client
Summary(pl):	tf - TinyFugue - tekstowy klient do MUD-ów
Name:		tf
Version:	40s1
Release:	3
License:	GPL
Group:		Applications/Games
Vendor:		Ken Keys (Hawkeye) <hawkeye@tf.tcp.com>
Source0:	ftp://tf.tcp.com/pub/tinyfugue/%{name}-%{version}.tar.gz
# Source0-md5:  db6fa9a1aac0b7f199567d81c4b5c81d
Patch0:		%{name}-filenames.patch
Patch1:		%{name}-%{version}-mccp.patch.gz
URL:		http://tf.tcp.com/~hawkeye/tf/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TinyFugue is a MUD-Client (Multi User Dungeons) that allows the user
to dive into one the most fascinating
Multi-User-Non-Graphic-Fantasy-Role-Playing-Games. Just Enter "tf" and
enjoy your game. This client works in text mode and supports MCCP
compression.

%description -l pl
TinyFugue jest klientem MUD (Multi User Dungeons), który pozwala 
u¿ytkownikowi zag³êbiæ siê w najbardziej fascynuj±cy ¶wiat
Multi-User-Non-Graphic-Fantasy-Role-Playing-Games. Jest to po prostu
jeden z najlepszych, je¶li nie najlepszy klient do gry w MUD-y (wraz
z obs³ug± protoko³u kompresji MCCP). Oczywi¶cie dla trybu
tekstowego :).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
mv -f unix/Config unix/Config.orig
cat >> unix/Config << EOF
TF="\${T_BIN}/tf-\${TFVER}"
LIBDIR="\${T_SHARE}/tf"
#SYMLINK="$RPM_BUILD_ROOT%{_bindir}/tf"
MAILDIR="/var/mail"
MANPAGE="%{_mandir}/man1/tf.1"
MANTYPE="nroff"
CCFLAGS="%{rpmcflags}"
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
%{_datadir}/%{name}/tf-help*
%{_mandir}/man1/tf.1*
