Summary:	GNU Core-utils - basic command line utilities
Name:		coreutils
Version:	8.18
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	http://ftp.gnu.org/gnu/coreutils/%{name}-%{version}.tar.xz
# Source0-md5:	74712fbb0e0dfcb883c90eab91982780
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
Provides:	fileutils
Provides:	mktemp = %{version}-%{release}
Provides:	sh-utils
Provides:	stat
Provides:	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These are the GNU core utilities. This package is the union of the GNU
fileutils, sh-utils, and textutils packages.

Most of these programs have significant advantages over their Unix
counterparts, such as greater speed, additional options, and fewer
arbitrary limits.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

sed -i -e 's|GNU/Linux|Freddix|' m4/host-os.m4

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules					\
	--enable-no-install-program=hostname,kill,uptime	\
	--enable-pam
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/bin,/sbin,%{_bindir},%{_sbindir},/etc/pam.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# unwanted
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
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/coreutils
%attr(755,root,root) %{_libdir}/coreutils/libstdbuf.so

%{_mandir}/man1/*
%{_infodir}/coreutils.info*

