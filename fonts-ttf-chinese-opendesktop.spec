%define version 1.4.2
%define release 9

Summary:	OpenDesktop.Org.tw Font
Name:		fonts-ttf-chinese-opendesktop
Version:	%{version}
Release:	%{release}

Source:		ftp://ftp.opendesktop.org.tw/odp/ODOFonts/OpenFonts/opendesktop-fonts-%{version}.tar.gz
URL:		https://www.opendesktop.org.tw/
License:	Arphic Public License
Group:		System/Fonts/True type
BuildArch:	noarch
BuildRequires: fontconfig
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

%postun
if [ "$1" = "0" ]; then
  [ -x %{_bindir}/mkfontdir ] && %{_bindir}/mkfontdir %{_datadir}/fonts/TTF/chinese-opendesktop
  [ -x %{_bindir}/mkfontscale ] && %{_bindir}/mkfontscale %{_datadir}/fonts/TTF/chinese-opendesktop
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


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.4.2-8mdv2011.0
+ Revision: 675516
- br fontconfig for fc-query used in new rpm-setup-build

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.2-7mdv2011.0
+ Revision: 610725
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.4.2-6mdv2010.1
+ Revision: 494133
- fc-cache is now called by an rpm filetrigger

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.4.2-5mdv2010.0
+ Revision: 428827
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.4.2-4mdv2009.0
+ Revision: 245254
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.4.2-2mdv2008.1
+ Revision: 140730
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.4.2-2mdv2008.0
+ Revision: 48740
- fontpath.d conversion (#31756)
- minor cleanups


* Sat Mar 24 2007 Funda Wang <fundawang@mandriva.org> 1.4.2-1mdv2007.1
+ Revision: 148713
- New package fonts-ttf-chinese-opendesktop
- Created package structure for fonts-ttf-chinese-opendesktop.

