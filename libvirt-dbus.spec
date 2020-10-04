# TODO: system user (libvirtdbus or use -Dsystem_user to change)

%global glib2_ver		1:2.44.0
%global libvirt_ver		3.0.0
%global libvirt_glib_ver	0.0.7

Summary:	libvirt D-Bus API binding
Summary(pl.UTF-8):	API D-Bus do libvirt
Name:		libvirt-dbus
Version:	1.4.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://libvirt.org/sources/dbus/%{name}-%{version}.tar.xz
# Source0-md5:	2fb11a73d7da59bf0e81c44c877fbcde
URL:		https://libvirt.org/
BuildRequires:	glib2-devel >= %{glib2_ver}
BuildRequires:	libvirt-devel >= %{libvirt_ver}
BuildRequires:	libvirt-glib-devel >= %{libvirt_glib_ver}
BuildRequires:	meson >= 0.49.0
BuildRequires:	ninja >= 1.5
BuildRequires:	python3-docutils
BuildRequires:	rpmbuild(macros) >= 1.736
Requires:	dbus
Requires:	glib2 >= %{glib2_ver}
Requires:	libvirt-glib >= %{libvirt_glib_ver}
Requires:	libvirt-libs >= %{libvirt_ver}
Requires:	polkit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides D-Bus API for libvirt.

%description -l pl.UTF-8
Ten pakiet udostępnia API D-Bus do libvirt.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.rst NEWS.rst README.rst
%attr(755,root,root) %{_sbindir}/libvirt-dbus
%{_datadir}/dbus-1/services/org.libvirt.service
%{_datadir}/dbus-1/system-services/org.libvirt.service
%{_datadir}/dbus-1/system.d/org.libvirt.conf
%{_datadir}/dbus-1/interfaces/org.libvirt.*.xml
%{_datadir}/polkit-1/rules.d/libvirt-dbus.rules
%{_mandir}/man8/libvirt-dbus.8*
