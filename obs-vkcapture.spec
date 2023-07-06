%ifnarch %{ix86}
Name: obs-vkcapture
%else
Name: obs-vkcapture-32bit
%endif

Version: 1.4.0
Release: 1
Summary: OBS Linux Vulkan/OpenGL game capture
License: GPL-2.0-only

URL:    https://github.com/nowrep/obs-vkcapture
VCS:    {{{ git_dir_vcs }}}
Source: {{{ git_dir_pack }}}

BuildRequires: cmake gcc gcc-c++
BuildRequires: cmake(libobs)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-scanner)

%description
OBS plugin for Vulkan/OpenGL game capture on Linux.

%prep
{{{ git_dir_setup_macro }}}

%build
%cmake \
%ifarch %{ix86}
    -DBUILD_PLUGIN=OFF \
%endif
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install
%ifarch %{ix86}
rm -r %{buildroot}/%{_datadir} %{buildroot}/%{_bindir} %{buildroot}/%{_libdir}/obs-plugins
%endif

%files
%defattr(-,root,root,-)
%license LICENSE
%ifnarch %{ix86}
%dir %{_datadir}/obs/obs-plugins/linux-vkcapture
%{_datadir}/obs/obs-plugins/linux-vkcapture/locale/ja-JP.ini
%{_datadir}/obs/obs-plugins/linux-vkcapture/locale/cs-CZ.ini
%{_datadir}/obs/obs-plugins/linux-vkcapture/locale/fr-FR.ini
%{_datadir}/obs/obs-plugins/linux-vkcapture/locale/es-ES.ini
%{_datadir}/obs/obs-plugins/linux-vkcapture/locale/it-IT.ini
%{_datadir}/obs/obs-plugins/linux-vkcapture/locale/ru-RU.ini
%{_datadir}/obs/obs-plugins/linux-vkcapture/locale/de-DE.ini
%{_datadir}/obs/obs-plugins/linux-vkcapture/locale/en-US.ini
%{_datadir}/vulkan/implicit_layer.d/obs_vkcapture_64.json
%{_datadir}/vulkan/implicit_layer.d/obs_vkcapture_32.json
%{_bindir}/obs-vkcapture
%{_bindir}/obs-glcapture
%{_bindir}/obs-gamecapture
%{_libdir}/obs-plugins/linux-vkcapture.so
%endif
%{_libdir}/libVkLayer_obs_vkcapture.so
%{_libdir}/libobs_glcapture.so
