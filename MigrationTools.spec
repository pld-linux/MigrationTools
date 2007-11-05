# $Revision: 1.22 $Date: 2007-11-05 23:51:20 $
%include        /usr/lib/rpm/macros.perl
Summary:	LDAP Migration Tools
Summary(pl.UTF-8):	Narzędzia do migraacji do LDAP
Name:		MigrationTools
Version:	47
Release:	2
License:	BSD
Group:		Networking/Admin
Source0:	http://www.padl.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	3faf83eb8482e55979bda47f1d1e6501
# http://www.padl.com/download/MigrationTools.txt
Source1:	%{name}.txt
Patch0:		%{name}-instdir.patch
Patch1:		%{name}-mktemp.patch
Patch2:		%{name}-simple.patch
Patch3:		%{name}-suffix.patch
Patch4:		%{name}-schema.patch
Patch5:		%{name}-noaliases.patch
Patch6:		%{name}-noddp.patch
Patch7:		%{name}-unique-hosts.patch
Patch8:		%{name}-sysconfdir.patch
Patch9:		%{name}-noproto.patch
URL:		http://www.padl.com/OSS/MigrationTools.html
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MigrationTools are a set of Perl scripts for migrating users,
groups, aliases, hosts, netgroups, networks, protocols, RPCs, and
services from existing nameservices (flat files, NIS, and NetInfo) to
LDAP.

%description -l pl.UTF-8
MigrationTools to zestaw skryptów perlowych do migracji użytkowników,
grup, hostów, grup sieciowych, sieci, protokołów, RPC i serwisów z
istniejących serwisów nazw (zwykłych plików, NIS, NetInfo) do LDAP.

%package -n openldap-migration
Summary:	LDAP Migration Tools
Summary(pl.UTF-8):	Narzędzia do migraacji do LDAP
Group:		Base
Requires:	openldap
Obsoletes:	ldap-MigrationTools

%description -n openldap-migration
The MigrationTools are a set of Perl scripts for migrating users,
groups, aliases, hosts, netgroups, networks, protocols, RPCs, and
services from existing nameservices (flat files, NIS, and NetInfo) to
LDAP.

%description -n openldap-migration -l pl.UTF-8
MigrationTools to zestaw skryptów perlowych do migracji użytkowników,
grup, hostów, grup sieciowych, sieci, protokołów, RPC i serwisów z
istniejących serwisów nazw (zwykłych plików, NIS, NetInfo) do LDAP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
install %{SOURCE1} .

perl -pi -e 's|%%CONFDIR%%|%{_sysconfdir}/openldap/|g;\
	s|%%INSTDIR%%|%{_datadir}/openldap/migration/|g' *.pl *.sh README

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/openldap,%{_datadir}/openldap/migration}

install *.sh *.pl $RPM_BUILD_ROOT%{_datadir}/openldap/migration
install migrate_common.ph $RPM_BUILD_ROOT%{_sysconfdir}/openldap

%clean
rm -rf $RPM_BUILD_ROOT

%files -n openldap-migration
%defattr(644,root,root,755)
%doc MigrationTools.txt README
%dir %{_datadir}/openldap/migration
%attr(755,root,root) %{_datadir}/openldap/migration/*.sh
%attr(755,root,root) %{_datadir}/openldap/migration/*.pl
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/openldap/migrate_common.ph
