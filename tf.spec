Summary:	tf - TinyFugue - MUD client
Summary(pl):	tf - TinyFugue - tekstowy klient do MUD-ów
Name:		tf
Version:	40s1
Release:	1
License:	GPL
Group:		Applications/Games
Vendor:		Ken Keys (Hawkeye) <hawkeye@tf.tcp.com>
Source0:	ftp://tf.tcp.com/pub/tinyfugue/%{name}-%{version}.tar.gz
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
mv -f unix/Config unix/Config.orig
cat << EOF >> unix/Config
TF="\${T_BIN}/tf-\${TFVER}"
LIBDIR="\${T_SHARE}/tf-\${TFVER}"
SYMLINK="/$RPM_BUILD_ROOT/usr/bin/tf"
MANTYPE="nroff"
MANPAGE="/usr/man/man1/tf.1"
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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}-%{version}}
install src/tf  $RPM_BUILD_ROOT%{_bindir}/%{name}
install tf-lib/*  $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

(cd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
ln -sf kb-bash.tf bind-bash.tf
ln -sf kb-emacs.tf bind-emacs.tf
ln -sf complete.tf completion.tf
ln -sf factoral.tf factorial.tf
ln -sf filexfer.tf file-xfer.tf
ln -sf local-eg.tf local.tf.sample
ln -sf psh.tf pref-shell.tf
ln -sf spc-page.tf space_page.tf
ln -sf spedwalk.tf speedwalk.tf
ln -sf stack-q.tf stack-queue.tf
ln -sf world-q.tf worldqueue.tf
)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}-%{version}
