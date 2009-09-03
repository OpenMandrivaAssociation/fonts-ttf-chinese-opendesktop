%define version 1.4.2
%define release %mkrel 5

Summary:	OpenDesktop.Org.tw Font
Name:		fonts-ttf-chinese-opendesktop
Version:	%{version}
Release:	%{release}

Source:		ftp://ftp.opendesktop.org.tw/odp/ODOFonts/OpenFonts/opendesktop-fonts-%{version}.tar.gz
URL:		http://www.opendesktop.org.tw/
License:	Arphic Public License
Group:		System/Fonts/True type
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%name-%version-%release-root
Requires(post): mkfontdir, mkfontscale
Requires(postun): mkfontdir, mkfontscale
Obsoletes:	fonts-ttf-chinese-compat
Provides:	fonts-ttf-chinese-compat = %{version}-%{release}

%description
OpenDesktop.Org.tw Font -- Simplified and Traditional Chinese and Japanese
Ming and Kai Face, based on Chinese and Japanese TTF Fonts donated by
Arphic company.

%prep
%setup -q -n opendesktop-fonts-%{version} 
 
%build

%install
rm -fr %{buildroot}

install -d %{buildroot}/%{_datadir}/fonts/TTF/chinese-opendesktop/
install -m 644 odosung.ttc %{buildroot}/%{_datadir}/fonts/TTF/chinese-opendesktop/
install -m 644 odosung-ExtB.ttf %{buildroot}/%{_datadir}/fonts/TTF/chinese-opendesktop/
install -m 644 odokai.ttf %{buildroot}/%{_datadir}/fonts/TTF/chinese-opendesktop/
install -m 644 odokai-ExtB.ttf %{buildroot}/%{_datadir}/fonts/TTF/chinese-opendesktop/

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/chinese-opendesktop \
    %{buildroot}%_sysconfdir/X11/fontpath.d/chinese-opendesktop:pri=50

%post
[ -x %{_bindir}/mkfontdir ] && %{_bindir}/mkfontdir %{_datadir}/fonts/TTF/chinese-opendesktop
[ -x %{_bindir}/mkfontscale ] && %{_bindir}/mkfontscale %{_datadir}/fonts/TTF/chinese-opendesktop
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache

%postun
if [ "$1" = "0" ]; then
  [ -x %{_bindir}/mkfontdir ] && %{_bindir}/mkfontdir %{_datadir}/fonts/TTF/chinese-opendesktop
  [ -x %{_bindir}/mkfontscale ] && %{_bindir}/mkfontscale %{_datadir}/fonts/TTF/chinese-opendesktop
  [ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache
fi

%clean
rm -fr %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc Changelog Changelog.zh_TW AUTHORS COPYRIGHT license
%dir %{_datadir}/fonts/TTF/chinese-opendesktop/
%{_datadir}/fonts/TTF/chinese-opendesktop/*.ttf
%{_datadir}/fonts/TTF/chinese-opendesktop/*.ttc
%{_sysconfdir}/X11/fontpath.d/chinese-opendesktop:pri=50
