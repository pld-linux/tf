Summary:	tf - TinyFugue - MUD client
Summary(pl):	tf - TinyFugue - tekstowy klient do MUDow
Name:		tf
Version:	40s1
Release:	1
License:	GPL
Group:		Aplications/games
Group(pl):	Aplikacje/gry
Vendor:		Ken Keys (Hawkeye) <hawkeye@tf.tcp.com>
URL:		http://tf.tcp.com/~hawkeye/tf/  
Source0:	ftp://tf.tcp.com/pub/tinyfugue/%{name}-%{version}.tar.gz 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/bin

%description
TinyFugue is a MUD-Client (Multi User Dungeons) that allows the user to dive 
into one the most fascinating 
Multi-User-Non-Graphic-Fantasy-Role-Playing-Games.
Just Enter "tf" and enjoy your game. 
%description -l pl
Po prostu jeden z najlepszych , jesli nie najlepszy klient do gry w MUDy.
Oczywiscie dla trybu tekstowego :) .
%prep

%setup -n %name-%version
mv unix/Config unix/Config.orig
cat << EOF >> unix/Config
TF="\${T_BIN}/tf-\${TFVER}"
LIBDIR="\${T_SHARE}/tf-\${TFVER}"
SYMLINK="/$RPM_BUILD_ROOT/usr/bin/tf"
MANTYPE="nroff"
MANPAGE="/usr/man/man1/tf.1"
CCFLAGS="$RPM_OPT_FLAGS"
EOF
cat unix/Config.orig >> unix/Config  
export T_BIN="/usr/bin"
export T_SHARE="/usr/share"
%build
export T_BIN="/usr/bin"
export T_SHARE="/usr/share"
ans=y sh unixmake files

%install
if [ -d $RPM_BUILD_ROOT ]; then 
 rm -rf $RPM_BUILD_ROOT
fi
mkdir $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT/usr
mkdir $RPM_BUILD_ROOT/usr/bin
mkdir $RPM_BUILD_ROOT/usr/share
mkdir $RPM_BUILD_ROOT/usr/share/%name-%version 
export T_BIN="$RPM_BUILD_ROOT/usr/bin"
export T_SHARE="$RPM_BUILD_ROOT/usr/share"
cp $RPM_BUILD_DIR/%name-%version/src/tf  $RPM_BUILD_ROOT/usr/bin/%name-%version
cp $RPM_BUILD_DIR/%name-%version/tf-lib/*  $RPM_BUILD_ROOT/usr/share/%name-%version/
gzip -9nf CHANGES COPYING CREDITS README
cd $RPM_BUILD_ROOT/usr/bin/
ln -s %name-%version %name
cd $RPM_BUILD_ROOT/usr/share/%name-%version
ln -s kb-bash.tf bind-bash.tf
ln -s kd-emacs.tf bind-emacs.tf
ln -s complete.tf completion.tf
ln -s factoral.tf factorial.tf
ln -s filexfer.tf file-xfer.tf
ln -s local.eg.tf local.tf.sample
ln -s psh.tf pref-shell.tf
ln -s spc-page.tf space_page.tf
ln -s spedwalk.tf speedwalk.tf
ln -s stack-q.tf stack-queue.tf
ln -s world-q.tf worldqueue.tf
%clean
sh unixmake clean

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/%name-%version
%attr(755,root,root) /usr/bin/%name
/usr/share/%name-%version
%doc *.gz

%changelog                                                                      
* %{date} PLD Team <pld-list@pld.org.pl>                                        
All persons listed below can be reached at <cvs_login>@pld.org.pl

$Log: tf.spec,v $
Revision 1.2  2001-10-17 07:30:46  qwark
hopefully  this is the end of trouble with install script (some workaround)

Revision 1.2  2001/10/17 09:30:43  qwark

Revision 1.1  2001/10/16 21:50:43  qwark
it's itial relase after some troubles with tf install script
 Added Files:
 	tf.spec

Revision 1.0  2001/10/17 23:50:53  qwark                                        
- initial release        
Based on spec written for RH
