#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x520A9993A1C052F8 (mdounin@mdounin.ru)
#
Name     : nginx
Version  : 1.14.0
Release  : 61
URL      : https://nginx.org/download/nginx-1.14.0.tar.gz
Source0  : https://nginx.org/download/nginx-1.14.0.tar.gz
Source1  : nginx.service
Source2  : nginx.tmpfiles
Source3  : webroot-setup.service
Source99 : https://nginx.org/download/nginx-1.14.0.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: nginx-bin
Requires: nginx-config
Requires: nginx-data
BuildRequires : openssl-dev
BuildRequires : pcre-dev
BuildRequires : zlib-dev
Patch1: build.patch
Patch2: 0001-Rework-nginx-configuration-directories.patch

%description
Documentation is available at http://nginx.org

%package bin
Summary: bin components for the nginx package.
Group: Binaries
Requires: nginx-data
Requires: nginx-config

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


%prep
%setup -q -n nginx-1.14.0
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523987259
%configure --disable-static --prefix=/var/www \
--conf-path=/usr/share/nginx/conf/nginx.conf \
--sbin-path=/usr/bin/nginx \
--pid-path=/run/nginx.pid \
--lock-path=/run/lock/nginx.lock \
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
--with-select_module
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1523987259
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/nginx.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/webroot-setup.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/tmpfiles.d/nginx.conf
## make_install_append content
rm -f %{buildroot}/usr/share/nginx/conf/*.default
install -m0644 conf/server.conf.example %{buildroot}/usr/share/nginx/conf/
install -m0644 conf/nginx.conf.example %{buildroot}/usr/share/nginx/conf/
mkdir -p %{buildroot}/usr/share/nginx/html
mv %{buildroot}/var/www/html/* %{buildroot}/usr/share/nginx/html/
mkdir -p %{buildroot}/usr/share/clr-service-restart
ln -sf /usr/lib/systemd/system/nginx.service %{buildroot}/usr/share/clr-service-restart/nginx.service
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nginx

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/nginx.service
/usr/lib/systemd/system/webroot-setup.service
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
