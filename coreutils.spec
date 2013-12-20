Summary:	GNU Core-utils - basic command line utilities
Name:		coreutils
Version:	8.22
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	http://ftp.gnu.org/gnu/coreutils/%{name}-%{version}.tar.xz
# Source0-md5:	8fb0ae2267aa6e728958adc38f8163a2
Patch0:		%{name}-uname-cpuinfo.patch
Patch1:		%{name}-mem.patch
URL:		http://www.gnu.org/software/coreutils/
BuildRequires:	acl-devel
BuildRequires:	attr-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
BuildRequires:	help2man
BuildRequires:	libcap-devel
BuildRequires:	pam-devel
BuildRequires:	texinfo
BuildRequires:	xz
Requires:	pam
Requires:	core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These are the GNU core utilities. This package is the union of the GNU
fileutils, sh-utils, and textutils packages.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i -e "s|GNU/Linux|Freddix|" m4/host-os.m4
%{__sed} -i -e "s|COLUMNS||" tests/envvar-check

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	DEFAULT_POSIX2_VERSION=200112 alternative=199209	\
	--disable-silent-rules					\
	--enable-install-program=arch				\
	--enable-no-install-program=hostname,kill,uptime
%{__make}

%if 0
%check
%{__make} -j1 RUN_EXPENSIVE_TESTS=yes tests check
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/bin,/sbin,%{_bindir},%{_sbindir},/etc/pam.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# provided by other packages
rm -f $RPM_BUILD_ROOT%{_mandir}/*/man1/{hostname,kill,uptime}.1
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/kk/LC_TIME

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS THANKS-to-translators TODO
%attr(755,root,root) %{_bindir}/[
%attr(755,root,root) %{_bindir}/arch
%attr(755,root,root) %{_bindir}/base64
%attr(755,root,root) %{_bindir}/basename
%attr(755,root,root) %{_bindir}/cat
%attr(755,root,root) %{_bindir}/chcon
%attr(755,root,root) %{_bindir}/chgrp
%attr(755,root,root) %{_bindir}/chmod
%attr(755,root,root) %{_bindir}/chown
%attr(755,root,root) %{_bindir}/chroot
%attr(755,root,root) %{_bindir}/cksum
%attr(755,root,root) %{_bindir}/comm
%attr(755,root,root) %{_bindir}/cp
%attr(755,root,root) %{_bindir}/csplit
%attr(755,root,root) %{_bindir}/cut
%attr(755,root,root) %{_bindir}/date
%attr(755,root,root) %{_bindir}/dd
%attr(755,root,root) %{_bindir}/df
%attr(755,root,root) %{_bindir}/dir
%attr(755,root,root) %{_bindir}/dircolors
%attr(755,root,root) %{_bindir}/dirname
%attr(755,root,root) %{_bindir}/du
%attr(755,root,root) %{_bindir}/echo
%attr(755,root,root) %{_bindir}/env
%attr(755,root,root) %{_bindir}/expand
%attr(755,root,root) %{_bindir}/expr
%attr(755,root,root) %{_bindir}/factor
%attr(755,root,root) %{_bindir}/false
%attr(755,root,root) %{_bindir}/fmt
%attr(755,root,root) %{_bindir}/fold
%attr(755,root,root) %{_bindir}/groups
%attr(755,root,root) %{_bindir}/head
%attr(755,root,root) %{_bindir}/hostid
%attr(755,root,root) %{_bindir}/id
%attr(755,root,root) %{_bindir}/install
%attr(755,root,root) %{_bindir}/join
%attr(755,root,root) %{_bindir}/link
%attr(755,root,root) %{_bindir}/ln
%attr(755,root,root) %{_bindir}/logname
%attr(755,root,root) %{_bindir}/ls
%attr(755,root,root) %{_bindir}/md5sum
%attr(755,root,root) %{_bindir}/mkdir
%attr(755,root,root) %{_bindir}/mkfifo
%attr(755,root,root) %{_bindir}/mknod
%attr(755,root,root) %{_bindir}/mktemp
%attr(755,root,root) %{_bindir}/mv
%attr(755,root,root) %{_bindir}/nice
%attr(755,root,root) %{_bindir}/nl
%attr(755,root,root) %{_bindir}/nohup
%attr(755,root,root) %{_bindir}/nproc
%attr(755,root,root) %{_bindir}/numfmt
%attr(755,root,root) %{_bindir}/od
%attr(755,root,root) %{_bindir}/paste
%attr(755,root,root) %{_bindir}/pathchk
%attr(755,root,root) %{_bindir}/pinky
%attr(755,root,root) %{_bindir}/pr
%attr(755,root,root) %{_bindir}/printenv
%attr(755,root,root) %{_bindir}/printf
%attr(755,root,root) %{_bindir}/ptx
%attr(755,root,root) %{_bindir}/pwd
%attr(755,root,root) %{_bindir}/readlink
%attr(755,root,root) %{_bindir}/realpath
%attr(755,root,root) %{_bindir}/rm
%attr(755,root,root) %{_bindir}/rmdir
%attr(755,root,root) %{_bindir}/runcon
%attr(755,root,root) %{_bindir}/seq
%attr(755,root,root) %{_bindir}/sha1sum
%attr(755,root,root) %{_bindir}/sha224sum
%attr(755,root,root) %{_bindir}/sha256sum
%attr(755,root,root) %{_bindir}/sha384sum
%attr(755,root,root) %{_bindir}/sha512sum
%attr(755,root,root) %{_bindir}/shred
%attr(755,root,root) %{_bindir}/shuf
%attr(755,root,root) %{_bindir}/sleep
%attr(755,root,root) %{_bindir}/sort
%attr(755,root,root) %{_bindir}/split
%attr(755,root,root) %{_bindir}/stat
%attr(755,root,root) %{_bindir}/stdbuf
%attr(755,root,root) %{_bindir}/stty
%attr(755,root,root) %{_bindir}/sum
%attr(755,root,root) %{_bindir}/sync
%attr(755,root,root) %{_bindir}/tac
%attr(755,root,root) %{_bindir}/tail
%attr(755,root,root) %{_bindir}/tee
%attr(755,root,root) %{_bindir}/test
%attr(755,root,root) %{_bindir}/timeout
%attr(755,root,root) %{_bindir}/touch
%attr(755,root,root) %{_bindir}/tr
%attr(755,root,root) %{_bindir}/true
%attr(755,root,root) %{_bindir}/truncate
%attr(755,root,root) %{_bindir}/tsort
%attr(755,root,root) %{_bindir}/tty
%attr(755,root,root) %{_bindir}/uname
%attr(755,root,root) %{_bindir}/unexpand
%attr(755,root,root) %{_bindir}/uniq
%attr(755,root,root) %{_bindir}/unlink
%attr(755,root,root) %{_bindir}/users
%attr(755,root,root) %{_bindir}/vdir
%attr(755,root,root) %{_bindir}/wc
%attr(755,root,root) %{_bindir}/who
%attr(755,root,root) %{_bindir}/whoami
%attr(755,root,root) %{_bindir}/yes

%dir %{_libdir}/coreutils
%attr(755,root,root) %{_libdir}/coreutils/libstdbuf.so

%{_mandir}/man1/*
%{_infodir}/coreutils.info*

