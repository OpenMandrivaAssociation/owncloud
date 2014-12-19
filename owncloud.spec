Summary:      The ownCloud Server - Private file sync and share server
Name:         owncloud
Version:      7.0.4
Release:      1
Source0:      http://owncloud.org/releases/%{name}-%{version}.tar.bz2
License:      AGPL-3.0
Group:        Monitoring
Url:          http://owncloud.org/
BuildRequires: apache-base
Requires:     php >= 4.1
Requires:     apache-base
Requires:     apache-mod_php
Requires:     php-mysql
Requires:     mysql
Requires:     php-gd
Requires:     php-iconv
Requires:     php-mbstring
Requires:     php-pdo_mysql
BuildArch:    noarch

%description
ownCloud Server provides you a private file sync and share
cloud. Host this server to easily sync business or private documents
across all your devices, and share those documents with other users of
your ownCloud server on their devices.

ownCloud - Your Cloud, Your Data, Your Way!  www.owncloud.org

%files
%defattr(-,root,root)
%attr(-,apache,apache) %_datadir/%name
%config(noreplace) %_sysconfdir/httpd/conf/webapps.d/%{name}.conf

#--------------------------------------------------------------------


%prep
%setup -q -n %name 

%build

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
    DirectoryIndex index.html index.php
    AllowOverride All
    Options FollowSymlinks
    Require all granted
</Directory>

EOF


%changelog
* Sun Nov 30 2014 Luthfi Emka <panahbiru@gmail.com> 7.0.2-1
+ Revision: 905788
- version update 7.0.2

* Fri Jun 15 2012 Alexander Khrukin <akhrukin@mandriva.org> 4.0.2-1
+ Revision: 805788
- version update 4.0.2

* Mon May 28 2012 Alexander Khrukin <akhrukin@mandriva.org> 4.0.0-1
+ Revision: 800984
- version update 4.0.0

* Fri Feb 03 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.0.0-1
+ Revision: 770847
- version update 3.0.0

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove old macros

* Fri Nov 26 2010 Funda Wang <fwang@mandriva.org> 1.1-1mdv2011.0
+ Revision: 601453
- 1.1 final

* Mon Aug 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.1-0.2mdv2011.0
+ Revision: 564901
- New snapshot

* Mon Jul 26 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.1-0.1mdv2011.0
+ Revision: 560853
- Update git snapshot ( pre 1.1 )

* Thu Apr 15 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0-0.6mdv2010.1
+ Revision: 535024
- Update to new git snapshot

* Tue Mar 30 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0-0.5mdv2010.1
+ Revision: 528969
- New owncloud snapshot

* Fri Mar 26 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0-0.4.1mdv2010.1
+ Revision: 527607
- Change versionning
- Update owncloud snapshot

* Wed Mar 24 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0-0.3f88fb9f.1mdv2010.1
+ Revision: 527202
- import owncloud

