# $Revision: 1.11 $Date: 2003-07-14 17:22:01 $
%include        /usr/lib/rpm/macros.perl
Summary:	LDAP Migration Tools
Summary(pl):	Narzêdzia do migraacji do LDAP
Name:		ldap-MigrationTools
Version:	44
Release:	1
License:	custom
Group:		Base
Source0:	http://www.padl.com/download/MigrationTools.tgz
# Source0-md5:	2cc51cbf0276c161724626c70b59f0b1
Source1:	http://www.padl.com/download/MigrationTools.txt
URL:		http://www.padl.com/tools.html
Patch0:		MigrationTools-38-instdir.patch
Patch1:		MigrationTools-36-mktemp.patch
Patch2:		MigrationTools-27-simple.patch
Patch3:		MigrationTools-26-suffix.patch
Patch4:		MigrationTools-44-schema.patch
BuildRequires:	rpm-perlprov
Requires:	openldap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MigrationTools are a set of Perl scripts for migrating users,
groups, aliases, hosts, netgroups, networks, protocols, RPCs, and
services from existing nameservices (flat files, NIS, and NetInfo) to
LDAP.

%description -l pl
MigrationTools to zestaw skryptów perlowych do migracji u¿ytkowników,
grup, hostów, grup sieciowych, sieci, protoko³ów, RPC i serwisów z
istniej±cych serwisów nazw (zwyk³ych plików, NIS, NetInfo) do LDAP.

%prep
%setup -qn MigrationTools-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
install %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/MigrationTools
install *.sh *.pl *.ph $RPM_BUILD_ROOT%{_datadir}/MigrationTools

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc MigrationTools.txt README
%dir %{_datadir}/MigrationTools
%attr(755,root,root) %{_datadir}/MigrationTools/*.sh
%attr(755,root,root) %{_datadir}/MigrationTools/*.pl
%{_datadir}/MigrationTools/*.ph
