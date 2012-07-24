%define       name    owncloud
%define       version 4.0.5
%define       release 1

Summary:      Open personal cloud
Name:         %{name}
Version:      %{version}
Release:      %{release}
Source0:      http://owncloud.org/releases/%{name}-%{version}.tar.bz2
License:      AGPLv3
Group:        Monitoring
Url:          http://owncloud.org/
BuildRequires: apache-base
Requires:     php >= 4.1
Requires:     apache-base
Requires:     apache-mod_php
BuildArch:    noarch

%description
A personal cloud server which runs on you personal server 
and enables accessing your data from everywhere and sharing 
with other people.

%files
%defattr(-,root,root)
%attr(-,apache,apache) %_datadir/%name
%config(noreplace) %_sysconfdir/httpd/conf/webapps.d/%{name}.conf

#--------------------------------------------------------------------


%prep
%setup -q -n %name 

%build
echo "Hello, i'm a build section"

%install
mkdir -p %buildroot%_datadir/owncloud
(
cd %buildroot%_datadir
tar xjf %{SOURCE0}
)


mkdir -p %buildroot%_sysconfdir/httpd/conf/webapps.d
cat > %buildroot%_sysconfdir/httpd/conf/webapps.d/%{name}.conf <<EOF
# %{name} configuration
Alias /%name %_datadir/%name
<Directory %_datadir/%name>
    Order allow,deny
    Allow from all
</Directory>

EOF
