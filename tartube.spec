Name:		tartube
Version:	2.5.250
Release:	1
Summary:	GUI for youtube-dl and yt-dlp
License:	LGPL-2.1-or-later
Group:		Video/Players
Url:		https://github.com/axcore/tartube
# GitHub has no v2.5.250 tag. The sdist is published on PyPI.
Source0:	https://files.pythonhosted.org/packages/source/t/tartube/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(feedparser)
BuildRequires:	python%{pyver}dist(requests)
BuildRequires:	python%{pyver}dist(pygobject)

Requires:	python%{pyver}dist(feedparser)
Requires:	python%{pyver}dist(requests)
Requires:	python%{pyver}dist(pygobject)
Requires:	typelib(Gtk) = 3.0
Requires:	typelib(GdkPixbuf) = 2.0
Requires:	typelib(Pango) = 1.0
Requires:	aria2
Requires:	atomicparsley
Requires:	ffmpeg
Requires:	youtube-dl
Requires:	yt-dlp
Recommends:	streamlink
Recommends:	typelib(Notify) = 0.7

%description
A front-end GUI for youtube-dl and yt-dlp.
It is a fork of youtube-dl-gui.

%prep
%autosetup -p1

%build
# strict packaging mode installs icons, the desktop file, and the man page
# under /usr and disables youtube-dl self-updates.
export TARTUBE_PKG_STRICT=1
%py_build

%install
# setup.py install re-reads the environment. %build and %install are
# separate shells, so the strict path has to be set again here.
export TARTUBE_PKG_STRICT=1
%py_install
# setup.py also copies the gettext sources into the locale directory.
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/*.po

%files
%doc CHANGES README.rst
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/tartube/
%{_mandir}/man1/%{name}.1*
%{_datadir}/locale/*/LC_MESSAGES/tartube.mo
%{python_sitelib}/tartube/
%{python_sitelib}/tartube-%{version}*
