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
export T_BIN="$RPM_BUILD_ROOT/usr/bin"
export T_SHARE="$RPM_BUILD_ROOT/usr/share"
ans=y sh unixmake reconfigure
sh unixmake install
#cd /$RPM_BUILD_ROOT/usr/share/doc/tf-${TFVER}
gzip -9nf CHANGES COPYING CREDITS README
#cd $RPM_BUILD_ROOT/usr/bin/
%clean
sh unixmake clean

%post
cd /usr/bin
ln -s ./%name-%version ./tf

%postun 
rm /usr/bin/tf

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/%name-%version
/usr/share/%name-%version
%doc *.gz
#%doc CHANGES COPYING CREDITS README

%changelog                                                                      
* %{date} PLD Team <pld-list@pld.org.pl>                                        
All persons listed below can be reached at <cvs_login>@pld.org.pl

$Log: tf.spec,v $
Revision 1.1  2001-10-16 21:50:43  qwark
it's itial relase after some troubles with tf install script
 Added Files:
 	tf.spec

Revision 1.0  2001/10/17 23:50:53  qwark                                        
- initial release        
Based on spec written for RH
