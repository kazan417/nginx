#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x520A9993A1C052F8 (mdounin@mdounin.ru)
#
Name     : nginx
Version  : 1.16.1
Release  : 76
URL      : https://nginx.org/download/nginx-1.16.1.tar.gz
Source0  : https://nginx.org/download/nginx-1.16.1.tar.gz
Source1  : nginx-setup.service
Source2  : nginx.service
Source3  : nginx.tmpfiles
Source4 : https://nginx.org/download/nginx-1.16.1.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: nginx-bin = %{version}-%{release}
Requires: nginx-config = %{version}-%{release}
Requires: nginx-data = %{version}-%{release}
Requires: nginx-lib = %{version}-%{release}
Requires: nginx-license = %{version}-%{release}
Requires: nginx-services = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : openssl-dev
BuildRequires : pcre-dev
BuildRequires : zlib-dev
Patch1: build.patch
Patch2: 0001-Rework-nginx-configuration-directories.patch
Patch3: 0002-Enable-HTTP-2-by-default.patch

%description
Documentation is available at http://nginx.org

%package bin
Summary: bin components for the nginx package.
Group: Binaries
Requires: nginx-data = %{version}-%{release}
Requires: nginx-config = %{version}-%{release}
Requires: nginx-license = %{version}-%{release}
Requires: nginx-services = %{version}-%{release}

%description bin
bin components for the nginx package.


%package config
Summary: config components for the nginx package.
Group: Default

%description config
config components for the nginx package.


%package data
Summary: data components for the nginx package.
Group: Data

%description data
data components for the nginx package.


%package lib
Summary: lib components for the nginx package.
Group: Libraries
Requires: nginx-data = %{version}-%{release}
Requires: nginx-license = %{version}-%{release}

%description lib
lib components for the nginx package.


%package license
Summary: license components for the nginx package.
Group: Default

%description license
license components for the nginx package.


%package services
Summary: services components for the nginx package.
Group: Systemd services

%description services
services components for the nginx package.


%prep
%setup -q -n nginx-1.16.1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565805651
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --prefix=/var/www \
--conf-path=/usr/share/nginx/conf/nginx.conf \
--sbin-path=/usr/bin/nginx \
--pid-path=/run/nginx.pid \
--lock-path=/run/lock/nginx.lock \
--modules-path=/usr/lib64/nginx \
--http-log-path=syslog:server=unix:/dev/log \
--http-client-body-temp-path=/var/lib/nginx/client-body \
--http-fastcgi-temp-path=/var/lib/nginx/fastcgi \
--http-proxy-temp-path=/var/lib/nginx/proxy \
--http-scgi-temp-path=/var/lib/nginx/scgi \
--http-uwsgi-temp-path=/var/lib/nginx/uwsgi \
--user=httpd \
--group=httpd \
--with-threads \
--with-ipv6 \
--with-debug \
--error-log-path=stderr \
--with-file-aio \
--with-http_ssl_module \
--with-http_v2_module \
--with-poll_module \
--with-select_module \
--with-stream=dynamic \
--with-stream_ssl_module
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1565805651
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nginx
cp LICENSE %{buildroot}/usr/share/package-licenses/nginx/LICENSE
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/nginx-setup.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/nginx.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/tmpfiles.d/nginx.conf
## Remove excluded files
rm -f %{buildroot}/var/www/html/50x.html
rm -f %{buildroot}/var/www/html/index.html
## install_append content
rm -f %{buildroot}/usr/share/nginx/conf/*.default
install -m0644 conf/server.conf.example %{buildroot}/usr/share/nginx/conf/
install -m0644 conf/nginx.conf.example %{buildroot}/usr/share/nginx/conf/
mkdir -p %{buildroot}/usr/share/nginx/html
install -m0644 html/50x.html %{buildroot}/usr/share/nginx/html/
install -m0644 html/index.html %{buildroot}/usr/share/nginx/html/
mkdir -p %{buildroot}/usr/share/clr-service-restart
ln -sf /usr/lib/systemd/system/nginx.service %{buildroot}/usr/share/clr-service-restart/nginx.service
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nginx

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/nginx.conf

%files data
%defattr(-,root,root,-)
/usr/share/clr-service-restart/nginx.service
/usr/share/nginx/conf/fastcgi.conf
/usr/share/nginx/conf/fastcgi_params
/usr/share/nginx/conf/koi-utf
/usr/share/nginx/conf/koi-win
/usr/share/nginx/conf/mime.types
/usr/share/nginx/conf/nginx.conf
/usr/share/nginx/conf/nginx.conf.example
/usr/share/nginx/conf/scgi_params
/usr/share/nginx/conf/server.conf.example
/usr/share/nginx/conf/uwsgi_params
/usr/share/nginx/conf/win-utf
/usr/share/nginx/html/50x.html
/usr/share/nginx/html/index.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/nginx/ngx_stream_module.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nginx/LICENSE

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/nginx-setup.service
/usr/lib/systemd/system/nginx.service
