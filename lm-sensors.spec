#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lm-sensors
Version  : 3.6.0
Release  : 7
URL      : https://github.com/lm-sensors/lm-sensors/archive/V3-6-0/lm-sensors-3.6.0.tar.gz
Source0  : https://github.com/lm-sensors/lm-sensors/archive/V3-6-0/lm-sensors-3.6.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: lm-sensors-bin = %{version}-%{release}
Requires: lm-sensors-lib = %{version}-%{release}
Requires: lm-sensors-license = %{version}-%{release}
Requires: lm-sensors-man = %{version}-%{release}
Requires: lm-sensors-services = %{version}-%{release}
BuildRequires : bison
BuildRequires : flex
BuildRequires : rrdtool-dev
Patch1: build.patch

%description
OVERVIEW OF THE LM-SENSORS PACKAGE
==================================
The lm-sensors package, version 3, provides user-space support for the
hardware monitoring drivers in Linux 2.6.5 and later. For older kernel
versions, you have to use lm-sensors version 2.

%package bin
Summary: bin components for the lm-sensors package.
Group: Binaries
Requires: lm-sensors-license = %{version}-%{release}
Requires: lm-sensors-services = %{version}-%{release}

%description bin
bin components for the lm-sensors package.


%package dev
Summary: dev components for the lm-sensors package.
Group: Development
Requires: lm-sensors-lib = %{version}-%{release}
Requires: lm-sensors-bin = %{version}-%{release}
Provides: lm-sensors-devel = %{version}-%{release}
Requires: lm-sensors = %{version}-%{release}

%description dev
dev components for the lm-sensors package.


%package doc
Summary: doc components for the lm-sensors package.
Group: Documentation
Requires: lm-sensors-man = %{version}-%{release}

%description doc
doc components for the lm-sensors package.


%package lib
Summary: lib components for the lm-sensors package.
Group: Libraries
Requires: lm-sensors-license = %{version}-%{release}

%description lib
lib components for the lm-sensors package.


%package license
Summary: license components for the lm-sensors package.
Group: Default

%description license
license components for the lm-sensors package.


%package man
Summary: man components for the lm-sensors package.
Group: Default

%description man
man components for the lm-sensors package.


%package services
Summary: services components for the lm-sensors package.
Group: Systemd services

%description services
services components for the lm-sensors package.


%prep
%setup -q -n lm-sensors-3-6-0
cd %{_builddir}/lm-sensors-3-6-0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642723598
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}  PREFIX=/usr LIBDIR=/usr/lib64


%install
export SOURCE_DATE_EPOCH=1642723598
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lm-sensors
cp %{_builddir}/lm-sensors-3-6-0/COPYING %{buildroot}/usr/share/package-licenses/lm-sensors/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/lm-sensors-3-6-0/COPYING.LGPL %{buildroot}/usr/share/package-licenses/lm-sensors/01a6b4bf79aca9b556822601186afab86e8c4fbf
%make_install PREFIX=/usr SBINDIR=/usr/bin LIBDIR=/usr/lib64 MANDIR=/usr/share/man PROG_EXTRA=sensord
## install_append content
mkdir -p %{buildroot}/usr/share/doc/lm-sensors/examples
cp -a %{buildroot}/etc %{buildroot}/usr/share/doc/lm-sensors/examples
install -D -m644 prog/init/*.service -t %{buildroot}/usr/lib/systemd/system
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fancontrol
/usr/bin/isadump
/usr/bin/isaset
/usr/bin/pwmconfig
/usr/bin/sensord
/usr/bin/sensors
/usr/bin/sensors-conf-convert
/usr/bin/sensors-detect

%files dev
%defattr(-,root,root,-)
/usr/include/sensors/error.h
/usr/include/sensors/sensors.h
/usr/lib64/libsensors.so
/usr/share/man/man3/libsensors.3

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/lm\-sensors/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsensors.so.5
/usr/lib64/libsensors.so.5.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lm-sensors/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/lm-sensors/06877624ea5c77efe3b7e39b0f909eda6e25a4ec

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/sensors.1
/usr/share/man/man5/sensors.conf.5
/usr/share/man/man5/sensors3.conf.5
/usr/share/man/man8/fancontrol.8
/usr/share/man/man8/isadump.8
/usr/share/man/man8/isaset.8
/usr/share/man/man8/pwmconfig.8
/usr/share/man/man8/sensord.8
/usr/share/man/man8/sensors-conf-convert.8
/usr/share/man/man8/sensors-detect.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/fancontrol.service
/usr/lib/systemd/system/lm_sensors.service
/usr/lib/systemd/system/sensord.service
