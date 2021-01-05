Name:		tartube
Version:	2.3.042
Release:	%mkrel 1
Summary:	GUI for youtube-dl
License:	GPLv3
Group:		Video/Players
Url:		https://github.com/axcore/tartube
Source0:	https://github.com/axcore/tartube/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		tartube-2.1.0-no-pgi-and-playsound-modules.patch
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(twodict)
BuildRequires:	python3dist(wxpython)

Requires:	python3dist(wxpython)
Requires:	python3dist(twodict)
Requires:	youtube-dl
Recommends:	atomicparsley
Recommends:	ffmpeg
Recommends:	python3-moviepy
Provides:	youtube-dl-gui = %version-%release
Obsoletes:	youtube-dl-gui < 0.4-4

%description
A front-end GUI for the popular youtube-dl written in wxPython.
It's a fork of youtube-dl-gui which works with python3.

%prep
%autosetup -p1

%build
export TARTUBE_PKG_STRICT=1
%py3_build

%install
%py3_install

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
%{python3_sitelib}/tartube/
%{python3_sitelib}/tartube-%(sed -e 's/.0/./g' <<< %{version})-py%{python3_version}.egg-info
%{_mandir}/man1/*
