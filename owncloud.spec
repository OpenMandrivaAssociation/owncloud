Summary:      Open personal cloud
Name:         owncloud
Version:      7.0.3
Release:      1
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
    Require all denied
</Directory>

EOF


%changelog
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

