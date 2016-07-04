#global git 3095952c1eb6

Name:		arc-theme
# Version from $(date +%s)
Version:	20160605
Release:	2%{?dist}
Summary:	Arc is a theme for GTK 3, GTK 2 and GNOMEShell
Group:		User Interface/Desktops
Epoch:		1

License:	GPLv3
URL:		https://github.com/horst3180/Arc-theme

Source0:	https://github.com/horst3180/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	autoconf automake gtk3-devel

Requires:	gtk-murrine-engine
Requires:	gnome-themes-standard

BuildArch:	noarch

%description
Arc is a flat theme with transparent elements for GTK 3,
GTK 2 and Gnome-Shell. It supports GTK 3 and GTK 2 based
desktop environments like GNOME, Cinnamon, MATE and Xfce.

%package plank
Summary:	Arc theme for Plank

%description plank
Arc theme for Plank

%prep
%setup -q

%build
autoreconf -vfi
%configure
%{make_build}

%install
%{make_install}
mkdir -p %{buildroot}%{_datadir}/plank/themes
cp -r extra/Arc-Plank %{buildroot}%{_datadir}/plank/themes/

%files
%doc AUTHORS README.md
%license COPYING
%{_datadir}/themes/Arc/
%{_datadir}/themes/Arc-Darker/
%{_datadir}/themes/Arc-Dark/

%files plank
%{_datadir}/plank/themes/Arc-Plank/*

%changelog
* Mon Jul 04 2016 Leigh Scott <leigh123linux@googlemail.com> 20160605-2
- spec file clean up
- fix release tag, 20160605 is a release (not git)
- fix source tag
- don't use autogen as it misses the configure flags

* Sun Jun 26 2016 Chris Smart <csmart@kororaproject.org> 20160605-1.git3095952c1eb6
- Build latest version from tag.

* Thu May 12 2016 Chris Smart <csmart@kororaproject.org> 1463048461-1.git5ec25f42e639
- Convert upstream spec file for use with kp build system
- Build package for Korora 24

