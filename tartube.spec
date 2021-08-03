Name:		tartube
Version:	2.3.306
Release:	1
Summary:	GUI for youtube-dl
License:	GPLv3
Group:		Video/Players
Url:		https://github.com/axcore/tartube
Source0:	https://github.com/axcore/tartube/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(twodict)
#BuildRequires:	python3dist(wxpython)
BuildRequires:  python3dist(moviepy)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(feedparser)

#Requires:	python3dist(wxpython)
Requires:	python3dist(twodict)
Requires:	python3dist(moviepy)
Requires: python3dist(requests)
Requires: python3dist(pip)
Requires: python3dist(feedparser)
Requires: python3dist(playsound)
Requires: python3dist(matplotlib)
Requires: aria2
Requires:	atomicparsley
Requires:	ffmpeg
Requires:	youtube-dl

%description
A front-end GUI for the popular youtube-dl written in wxPython.
It's a fork of youtube-dl-gui which works with python3.

%prep
%autosetup -p1

%build
export TARTUBE_PKG_STRICT=1
%py_build

%install
%py_install

# (tv) fix installation (& thus startup):
mkdir -p %{buildroot}%{_datadir}/tartube/
mv %{buildroot}/tartube %{buildroot}%{_datadir}/

mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 pack/tartube.1 %{buildroot}%{_mandir}/man1

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 0644 pack/tartube.png %{buildroot}%{_datadir}/pixmaps

mkdir -p  %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Tartube
GenericName=YouTube-dl GUI
Comment=GUI front-end for youtube-dl
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Audio;Video;AudioVideo;
EOF

%files
%doc CHANGES README.rst
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/tartube/
%{python_sitelib}/tartube/
%{python_sitelib}/tartube-%{version}-py*.*.egg-info/
%{_mandir}/man1/*
